import json
from GithubCrawler import GithubCrawler
from GithubCrawlerExtended import GithubCrawlerExtended
import sys

json_inp = '''{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
  	"51.15.222.119:80",
    "194.126.37.94:8080",
    "83.40.144.105:3128",
    "13.78.125.167:8080",
    "223.19.85.16:8118"
  ],
  "type": "Repositories"
}
'''

#json_inp = sys.argv[1] not working on windows 

j = json.loads(json_inp)

GithubCrawler(j['keywords'],j['proxies'],j['type'])

GithubCrawlerExtended(j['keywords'],j['proxies'],j['type'], more_info=True)
