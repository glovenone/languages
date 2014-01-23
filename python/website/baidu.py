import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

url ='http://www.baidu.com/s'
values ={'wd':'tennis'}
encoded_param = urllib.parse.urlencode(values)
full_url = url +'?'+ encoded_param
response = urllib.request.urlopen(full_url)
soup =BeautifulSoup(response)
soup.find_all('a')
