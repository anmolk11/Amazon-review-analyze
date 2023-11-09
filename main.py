from bs4 import BeautifulSoup
from selenium.webdriver import Chrome 
from selenium.webdriver import ChromeOptions
from urllib.parse import urljoin

options = ChromeOptions()
options.add_argument("--headless=new")
driver = Chrome(options=options)

def start_app(F):
    def wraper(self):
        global driver
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = Chrome(options=options)    
        # print('before')
        F(self)
        driver.quit()
        # print('after')
    return wraper



def writeHTML(html,file_name = 'sample.html'):
    with open(file_name,'w',encoding = 'utf-8') as F:
        F.write(html.prettify())
    print(f'HTML written in {file_name}')

def getSoup(url):
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html,'lxml')
    return soup

def getAllReviews(url):
    reviews_list = []
    count = 0
    limit = 1
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


class Reviews():
    def __init__(self,url) -> None:
        # print(" ******** \n\n I am called \n\n ********")
        self.url = url
    
    # @start_app    {this decorator is NOT working !!}
    def getReviews(self):
        review_list = []
        stars_list = []
        soup = getSoup(self.url)
        link = soup.find_all("div",attrs={
            "class" : "a-row a-spacing-medium"
        })[-1].find("a")

        review_link = link.get("href")

        review_link = urljoin(self.url,review_link)

        all_reviews = getAllReviews(review_link)

        for review in all_reviews:
            stars = getStars(review)
            text = getReviewText(review)
            review_list.append(text)
            stars_list.append(stars)

        driver.quit()
        print('\n\ndone\n\n')
        return review_list,stars_list

if __name__  == "__main__": 
    rvs = Reviews('https://www.amazon.in/dp/B071CP6HQH/ref=s9_acsd_al_bw_c2_x_0_i?th=1')
    print(rvs.getReviews())

