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

Or you can use the "sample.py" file to test both of the tasks

Sample.py Output
-------------

```
[
  {
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
  }
]
[
  {
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage",
    "extra": {
      "owner": "atuldjadhav",
      "language_stats": {
        "CSS": 52.0,
        "JavaScript": 47.2,
        "HTML": 0.8
      }
    }
  }
]
```