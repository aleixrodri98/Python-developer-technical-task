#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

class GithubCrawler(object):

	TYPE_REPOSITORIES = 'Repositories'
	TYPE_ISSUES = 'Issues'
	TYPE_WIKI = 'Wikis'

	TYPE_REPOSITORIES_HTML = 'repo'
	TYPE_ISSUES_HTML = 'issue'
	TYPE_WIKI_HTML = 'wiki'

	GITHUB_BASE_URL = 'https://github.com'

	def __init__(self, keywords, proxies, git_type):
		self.proxies = proxies
		self.keywords = keywords
		self.git_type = git_type
		self.last_p = 0
		self.result = []
		self.crawl()

	def using_requests(self, request_url):
		while True:
			if self.last_p != len(self.proxies):
				proxy_r = {
				'http': 'http://{}'.format(self.proxies[self.last_p]),
				'https': 'http://{}'.format(self.proxies[self.last_p]),
				}
				try:
					url_keywords = '+'.join(self.keywords)
					r = requests.get(request_url, proxies=proxy_r) #I would put a timeout just in case, to not hang forever
					return r.text
				except requests.exceptions.ProxyError:
					print ('Error Proxy #{}, trying new one'.format(self.last_p))
					self.last_p += 1
				except requests.exceptions.RequestException as e:
					print (e) #log exception in production, maybe github not available
					return False

			else:
				print ('No available proxies')#log error proxy in production
				return False

	def crawl(self):
		if self.git_type == self.TYPE_REPOSITORIES:
			git_url_type = self.TYPE_REPOSITORIES_HTML
		elif self.git_type == self.TYPE_ISSUES:
			git_url_type = self.TYPE_ISSUES_HTML
		elif self.git_type == self.TYPE_WIKI:
			git_url_type = self.TYPE_WIKI_HTML
		else:
			print ('Type not supported')
			return

		url_keywords = '+'.join(self.keywords)
		search_url = '{}/search?q={}&type={}&utf8=%E2%9C%93'.format(self.GITHUB_BASE_URL, url_keywords, self.git_type)

		r = self.using_requests(search_url)
		if not r:
			return

		soup = BeautifulSoup(r, "html.parser")

		items = soup.findAll('div',{'class': '{}-list-item'.format(git_url_type)})

		for item in items:
			if self.git_type == self.TYPE_REPOSITORIES:
				link = self.GITHUB_BASE_URL + item.div.h3.a['href']
			elif self.git_type == self.TYPE_ISSUES:
				link = self.GITHUB_BASE_URL + item.div.h3.a['href']
			elif self.git_type == self.TYPE_WIKI:
				link = self.GITHUB_BASE_URL + item.div.a['href']

			self.result.append({'url':link})

		print (self.result)


