# Python-developer-technical-task
Techical task for Red Points recruitment process


Example Usage for GithubCrawlerExtended
-------------

```python
from GithubCrawlerExtended import GithubCrawlerExtended

keywords = ["openstack", "nova", "css"]
proxies = ["194.126.37.94:8080", "13.78.125.167:8080"]
type = 'Repositories'

GithubCrawlerExtended(keywords,proxies,type)

GithubCrawlerExtended(keywords,proxies,type, more_info=True) #for more info pass more_info as true
```
