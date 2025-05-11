from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import re
import pandas as pd
import csv
import json

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# robots_url = 'https://durhamcountylibrary.org/robots.txt'
# driver.get(robots_url)
# print(driver.page_source)
# driver.quit()
driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')

body = driver.find_element(By.CSS_SELECTOR,'body') 
# print('body', body)
li_with_results = body.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
# print('li_with_result', li_with_results, len(li_with_results))
results = []

for li_result in li_with_results:
    element_with_title = li_result.find_element(By.CSS_SELECTOR, 'span.cp-screen-reader-message')
    # print('element_with_title', element_with_title)
    title = element_with_title.text
    # print('title', title)
   
    elements_with_authors = li_result.find_elements(By.CLASS_NAME, 'author-link')
    # print('elements_with_authors', elements_with_authors)
    authors = []
    for each_author in elements_with_authors:
         authors.append(each_author.text)
    # print('authors', authors)
    author = '; '.join(authors)
    # print('author', author)

    ''' in the current case there are some spans with the class 'cp-screen-reader-message' 
    so I need more complex selectors if I want use them, which would target span with format and year
    complex targeting is not necessary for span with class "display-info-primary"'''

    # div_with_format_and_year = li_result.find_element(By.CSS_SELECTOR, 'div.manifestation-item-format-info-wrap')
    # span_with_format_and_year = div_with_format_and_year.find_element(By.CSS_SELECTOR, 'span.cp-screen-reader-message')
    span_with_format_and_year = li_result.find_element(By.CSS_SELECTOR, 'span.display-info-primary')
    # print('span_with_format_and_year', span_with_format_and_year)
    format_and_year = span_with_format_and_year.text
    # print('format_and_year', format_and_year)
    # want to remove language, because it is out of scope of assignment
    format_and_year = re.sub(r'\s\|.*', '', format_and_year)
    # print('format_and_year', format_and_year)
    
    # append dictionary with the single book to the all books
    results.append({'Title': title, 'Author': author, 'Format-Year':format_and_year})
# print('results', results, len(results))
driver.quit()

df_results = pd.DataFrame(results)
print(df_results)

df_results.to_csv('get_books.csv', index=False)  

# Save data to a JSON file
with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)