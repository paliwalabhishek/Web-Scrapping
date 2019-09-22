from selenium import webdriver
import Target.calls as calls
import time



def getTargetData(searchUrl:str, product_name:str):
	browser = webdriver.Chrome('Drivers/76/chromedriver.exe')
	url = "https://www.target.com/s?searchTerm=i+can%27t+believe+it%27s+not+butter" # searchUrl
	browser.get(url)
	time.sleep(10)
	innerHtml = browser.execute_script("return document.body.innerHTML")
	product_url=calls.filter_html_data(innerHtml,product_name)
	print(product_url)
	browser.get(product_url)
	time.sleep(5)
	product_html=browser.execute_script("return document.body.innerHTML")
	calls.get_product_details(product_html)
	browser.close()

def generate_search_url(productName:str):
	search_url=""
	return search_url