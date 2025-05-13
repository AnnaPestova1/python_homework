from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import re
import math
from time import sleep
import pandas as pd
import json

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
results = []
search_string = 'learning%20spanish'
# robots_url = 'https://durhamcountylibrary.org/robots.txt'
# driver.get(robots_url)
# print(driver.page_source)
# driver.quit()

try:
    driver.get(f'https://durhamcounty.bibliocommons.com/v2/search?query={search_string}&searchType=smart')

    body = driver.find_element(By.CSS_SELECTOR,'body') 
    # print('body', body)

    # # amount of paged to paginate
    pagination = body.find_element(By.CLASS_NAME, 'pagination--compact')
    # print('pagination', pagination)
    pagination_label = pagination.find_element(By.CSS_SELECTOR, 'span.cp-pagination-label')
    # print('pagination_label', pagination_label)
    pagination_result = pagination_label.text
    print('pagination_result', pagination_result)
    pagination_total_results = re.compile(r'(\d+) to (\d+) of (\d+)').match(pagination_result)
    # print('pagination_total_results', pagination_total_results)
    per_page = int(pagination_total_results.group(2))
    total = int(pagination_total_results.group(3))
    # print(per_page, total)
    # I do not want to paginate more than 20 pages
    rounded_pages = math.floor(total/per_page) if math.floor(total/per_page) < 20 else 20
    # print('rounded_pages', rounded_pages)
    pages = rounded_pages+1 if (rounded_pages < 20 and total % per_page != 0) else rounded_pages
    # print("pages", pages)
    for i in range(pages):
        # print("pages", pages)
        # print('body', body)
        sleep(3)
        print(i)
        if i > 0: 
            driver.get(f'https://durhamcounty.bibliocommons.com/v2/search?query={search_string}&searchType=smart&page={i+1}')
            body = driver.find_element(By.CSS_SELECTOR,'body') 
        li_with_results = body.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
        # print('li_with_result', li_with_results, len(li_with_results))
        for li_result in li_with_results:
            element_with_title = li_result.find_element(By.CSS_SELECTOR, 'span.cp-screen-reader-message')
            print('element_with_title', element_with_title)
            full_title = element_with_title.text
            # remove format of book from title
            title = re.sub(r', [\w ]+$', '', full_title)
            print('title', title)
        
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
            # I want to remove language, from format_and_year variable, because it is out of scope of assignment
            format_and_year = re.sub(r'\s\|.*', '', format_and_year)
            # print('format_and_year', format_and_year)
            
            # append dictionary with the single book to the all books
            results.append({'Title': title, 'Author': author, 'Format-Year':format_and_year})

            print('results', results, len(results))
    # print('results', results, len(results))
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")
finally:
     driver.quit()
        

print('results', len(results))

df_results = pd.DataFrame(results)
print(df_results)

df_results.to_csv('get_books.csv', index=False)  

# Save data to a JSON file
with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)