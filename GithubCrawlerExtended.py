#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
import json
from time import sleep

class NoProxyAvailable(Exception):
	def __init__(self):
		Exception.__init__(self,"No available proxies") 

class TypeNotSupported(Exception):
	def __init__(self):
		Exception.__init__(self,"Type not supported") 

class GithubCrawlerExtended(object):

	TYPE_REPOSITORIES = 'Repositories'
	TYPE_ISSUES = 'Issues'
	TYPE_WIKI = 'Wikis'

	TYPE_REPOSITORIES_HTML = 'repo'
	TYPE_ISSUES_HTML = 'issue'
	TYPE_WIKI_HTML = 'wiki'

	GITHUB_BASE_URL = 'https://github.com'

	DEFAULT_PARSER = 'html.parser'

	def __init__(self, keywords, proxies, git_type, more_info=False):
		self.proxies = proxies
		self.keywords = keywords
		self.git_type = git_type
		self.more_info = more_info
		self.last_p = 0
		self.result = []

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
					if 'You have triggered an abuse detection mechanism.' not in r.text: #Not abort in case of abuse detection
						return r.text
					else:
						print ('Proxy #{} detected for abuse, trying new one'.format(self.last_p))
						self.last_p += 1
				except requests.exceptions.ProxyError:
					print ('Error Proxy #{}, trying new one'.format(self.last_p))
					self.last_p += 1
				except requests.exceptions.RequestException as e:
					print (e) #log exception in production, maybe github not available
					raise e

			else:
				raise NoProxyAvailable()


	def crawl(self):
		if self.git_type == self.TYPE_REPOSITORIES:
			git_url_type = self.TYPE_REPOSITORIES_HTML
		elif self.git_type == self.TYPE_ISSUES:
			git_url_type = self.TYPE_ISSUES_HTML
		elif self.git_type == self.TYPE_WIKI:
			git_url_type = self.TYPE_WIKI_HTML
		else:
			raise TypeNotSupported()

		url_keywords = '+'.join(self.keywords)
		search_url = '{}/search?q={}&type={}&utf8=%E2%9C%93'.format(self.GITHUB_BASE_URL, url_keywords, self.git_type)
		r = self.using_requests(search_url)

		soup = BeautifulSoup(r, self.DEFAULT_PARSER)

		items = soup.findAll('div',{'class': '{}-list-item'.format(git_url_type)})

		for item in items:
			if self.git_type == self.TYPE_REPOSITORIES:
				link = self.GITHUB_BASE_URL + item.div.h3.a['href']
			elif self.git_type == self.TYPE_ISSUES:
				link = self.GITHUB_BASE_URL + item.div.h3.a['href']
			elif self.git_type == self.TYPE_WIKI:
				link = self.GITHUB_BASE_URL + item.div.a['href']

			res = {'url':link}

			if self.more_info and self.git_type == self.TYPE_REPOSITORIES:
				res['extra'] = {}
				res['extra']['owner'] = link.split('/')[3]
				res['extra']['language_stats'] = {}

				r = self.using_requests(link)
				if 'This repository is empty.' not in r: #put language_stats empty in case repository is empty
					soup = BeautifulSoup(r, self.DEFAULT_PARSER)
					div = soup.find('div',{'class':'repository-lang-stats-graph'})
					language_color_list = div.findAll('span',{'class':'language-color'})
					for l in language_color_list:
						lang_tmp = l['aria-label'].replace('%','')
						lang, percentage = lang_tmp.split()
						res['extra']['language_stats'][lang] = float(percentage)


			self.result.append(res)

		print (json.dumps(self.result, indent=2))
		return str(self.result) #for testing purposes


