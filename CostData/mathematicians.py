from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import json
from json_extraction import extract_values

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)

def filter_HTMLdata(rawHtml):
    html=BeautifulSoup(rawHtml,'html.parser')
    raw_json=html.find("script",{"id":"searchContent"}).text
    search_json=json.loads(raw_json)
    first_item = search_json['searchContent']['preso']['items'][0]
    product_page_url = first_item['productPageUrl']
    return product_page_url

def filter_HTMLproduct(rawHtml):
    html=BeautifulSoup(rawHtml,'html.parser')
    raw_json=html.find("script",{"id":"item"}).text
    product_json=json.loads(raw_json)
    product_price=product_json["item"]["product"]["midasContext"]["price"]
    print("Walmart Price --> $"+product_price)



    