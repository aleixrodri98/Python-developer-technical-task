# Python Developer Technical Task
Techical task for Red Points recruitment process


Example Usage for GithubCrawlerExtended (non extended version)
-------------

```python
from GithubCrawlerExtended import GithubCrawlerExtended

keywords = ["openstack", "nova", "css"]
proxies = ["194.126.37.94:8080", "13.78.125.167:8080"]
git_type = 'Repositories'

crawler = GithubCrawlerExtended(keywords,proxies,git_type)

crawler.crawl()
```

<<<<<<< HEAD
Example Usage for GithubCrawlerExtended (extended version)
-------------

```python
from GithubCrawlerExtended import GithubCrawlerExtended

keywords = ["openstack", "nova", "css"]
proxies = ["194.126.37.94:8080", "13.78.125.167:8080"]
git_type = 'Repositories'

crawler = GithubCrawlerExtended(keywords,proxies,git_type, more_info=True) #for more info pass more_info as true

crawler.crawl()
```
=======
Or you can use the "test.py" file to test both of the tasks
>>>>>>> 300682fa1f29297510ed0e79e971d2ee3c11f204
