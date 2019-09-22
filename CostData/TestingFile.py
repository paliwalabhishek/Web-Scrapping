import mathematicians
import Target.main as target_call
import Walmart.main as walmart_call

product_name="i can't believe it's not butter"

target_search_url=target_call.generate_search_url(product_name)
target_result=target_call.getTargetData(target_search_url, product_name)

walmart_search_url=walmart_call.generate_search_url(product_name)


