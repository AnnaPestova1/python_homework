from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
results = []
try:
    driver.get('https://owasp.org/www-project-top-ten/')

    body = driver.find_element(By.CSS_SELECTOR,'body') 
    # print('body', body)

    section = body.find_element(By.ID, 'sec-main')
    # # print('section', section)

    ul_with_vulnerabilities = section.find_element(By.XPATH, 'ul[2]')
    # print('ul_with_vulnerabilities', ul_with_vulnerabilities)

    links = ul_with_vulnerabilities.find_elements(By.CSS_SELECTOR, 'a')
    # print('links', links)

    for link in links:
        title = link.text.strip()
        # print(name)
        url = link.get_attribute("href")
        # print(url)
        if title and url:
            results.append({"title": title, "link": url})
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")
finally:
     driver.quit()

print(results)

with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for result in results:
        writer.writerow([result["title"], result["link"]])