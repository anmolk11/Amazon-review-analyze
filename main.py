import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome 
from selenium.webdriver import ChromeOptions
import time
from urllib.parse import urljoin

options = ChromeOptions()
options.headless = True
driver = Chrome(executable_path='chromedriver.exe', options=options)


data = {
    "review" : [],
    "stars" : []
}

def getSoup(url):
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html,'lxml')
    return soup

def getAllReviews(url):
    reviews_list = []
    count = 0
    limit = 50
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

def getStars(soup):
    stars = soup.find("a",attrs={
        "class"  : "a-link-normal"
    }).find("span",attrs={
        "class" : "a-icon-alt"
    }).text    
    stars = float(stars.split()[0])
    return stars

if __name__  == "__main__":
    url = "https://www.amazon.in/Campus-OXYFIT-Walking-Shoes-India/dp/B09RPVZK5S/ref=sr_1_1?keywords=shoes%2Bfor%2Bmen&qid=1679773036&sprefix=shoes%2Cspecialty-aps%2C229&sr=8-1&th=1&psc=1"
    
    soup = getSoup(url)

    link = soup.find_all("div",attrs={
        "class" : "a-row a-spacing-medium"
    })[-1].find("a")

    review_link = link.get("href")

    review_link = urljoin(url,review_link)

    all_reviews = getAllReviews(review_link)

    for count,review in enumerate(all_reviews):
        stars = getStars(review)
        text = getReviewText(review)
        data["review"].append(text)
        data["stars"].append(stars)
    
    
    df = pd.DataFrame(data)
    df.to_csv("reviews.csv")
    df.to_csv("reviews.csv")