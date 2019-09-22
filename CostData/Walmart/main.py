
walmart_base_url = 'https://www.walmart.com'
walmart_search_url = walmart_base_url+'/search/?cat_id=0&query=I+Can%27t+Believe+It%27s+Butter'

def generate_search_url(product_name:str):
	search_url=walmart_search_url
	raw_search_html=mathematicians.simple_get(target_search_url)
	return search_url


raw_search_html=mathematicians.simple_get(target_search_url)
target_calls.filter_html_data(raw_search_html)


## Walmart Specfic functions

product_page_url=mathematicians.filter_HTMLdata(raw_search_html)
raw_product_html=mathematicians.simple_get('https://www.walmart.com'+product_page_url)
mathematicians.filter_HTMLproduct(raw_product_html)
