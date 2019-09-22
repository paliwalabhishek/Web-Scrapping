import json
from bs4 import BeautifulSoup
import re

def filter_html_data(rawHtml,product_name):
	parsed_html=BeautifulSoup(rawHtml,'html.parser')

	result=parsed_html.findAll("a")

	search_list=[]
	buy_url="buy_url"
	for ele in result:
		temp=str(ele).lower()
		if(re.search(product_name,temp)):
			if(re.search(buy_url,temp)):
				search_list.append(ele)
	bs = BeautifulSoup(str(search_list[0]),"html.parser")
	return bs.find("a")[buy_url]

def get_product_details(rawHtml):
	parsed_html=BeautifulSoup(rawHtml,'html.parser')
	result=parsed_html.find("span",{"data-test":"product-price"}).text
	print(result)
	