###b_kh
###ali_coder
import requests
respons=requests.get('http://quera.ir')
print(respons.status_code)
print(respons.request.headers)
print(respons.url)
print(respons.reason)
print(respons.text)