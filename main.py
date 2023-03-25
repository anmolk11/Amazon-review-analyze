from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


header = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})


if __name__ == "__main__":
    url = "https://www.amazon.in/Campus-OXYFIT-Walking-Shoes-India/dp/B09RPVZK5S/ref=sr_1_1?keywords=shoes%2Bfor%2Bmen&qid=1679773036&sprefix=shoes%2Cspecialty-aps%2C229&sr=8-1&th=1&psc=1"

    html = requests.get(url,headers=header)

    soup = BeautifulSoup(html.content,'lxml')

    link = soup.find_all("div",attrs={
        "class" : "a-row a-spacing-medium"
    })[1].find("a")

    all_review = link.get("href")

    all_review = urljoin(url,all_review)


    
    