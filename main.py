import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome 
from selenium.webdriver import ChromeOptions
import time
from urllib.parse import urljoin

options = ChromeOptions()
options.headless = True
driver = Chrome(executable_path='chromedriver.exe', options=options)


def getSoup(url):
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html,'lxml')
    return soup

def getAllReviews(url):
    reviews_list = []
    count = 0
    limit = 15
    while count < limit:
        count += 1
        soup = getSoup(url)
        reviews = soup.find_all("div",attrs={
            "class" : "a-section celwidget"
        })
        reviews_list.extend(reviews)

        next_button = soup.find("li",attrs={
            "class" : "a-last"
        }).find("a")

        if next_button:
            next_page_url = next_button.get("href")
            url = urljoin(url,next_page_url)
        else:
            break

    return reviews_list


def getReviewText(soup):
    text = soup.find("span",attrs={
        "class" : "a-size-base review-text review-text-content"
    }).text

    return text.strip()

if __name__  == "__main__":
    start_time = time.time()
    url = "https://www.amazon.in/OPPO-Fantastic-Purple-128GB-Storage/dp/B08VB34KJ1/ref=sr_1_3?keywords=mobile&sr=8-3&th=1"
    
    soup = getSoup(url)

    link = soup.find_all("div",attrs={
        "class" : "a-row a-spacing-medium"
    })[-1].find("a")

    review_link = link.get("href")

    review_link = urljoin(url,review_link)

    all_reviews = getAllReviews(review_link)

    for count,review in enumerate(all_reviews):
        text = getReviewText(review)
        file_name = f"Reviews/review_{count}.txt"
        with open(file_name,"w",encoding="utf-8") as F:
            F.write(text)
    
    print("\n---------------------------------------------------\n")
    print(f"Execution time : {time.time() - start_time}")
    print("\n---------------------------------------------------\n")