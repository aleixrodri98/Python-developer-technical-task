import pytest
from GithubCrawlerExtended import GithubCrawlerExtended, NoProxyAvailable, TypeNotSupported


class TestGithubCrawler:
	DEFAULT_PROXIES = [
		"83.40.144.105:3128", #this one is mine, so it always works
		"194.126.37.94:8080",
		"13.78.125.167:8080",
		"223.19.85.16:8118"
	]
	DEFAULT_KEYWORDS_1 = ["openstack","nova","css"]
	DEFAULT_KEYWORDS_2 = ["python", "django-rest-framework", "jwt"]
	DEFAULT_TYPE = "Repositories"
	GIT_TYPES = ["Repositories", "Issues", "Wikis"]

	def test_example_1(self):
		"""Testing non extended version with first sample"""
		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,self.DEFAULT_PROXIES,self.GIT_TYPES[0])
		res = crawler.crawl()
		expected_repo = "[{'url': 'https://github.com/atuldjadhav/DropBox-Cloud-Storage'}]"
		assert res == expected_repo

		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,self.DEFAULT_PROXIES,self.GIT_TYPES[1])
		res = crawler.crawl()
		expected_issues = "[{'url': 'https://github.com/hellowj/blog/issues/37'}, {'url': 'https://github.com/altai/nova-billing/issues/1'}, {'url': 'https://github.com/novnc/websockify/issues/180'}, {'url': 'https://github.com/zioc/contrail-devstack-plugin/issues/27'}, {'url': 'https://github.com/rcbops/rpc-openstack/pull/2257'}, {'url': 'https://github.com/aaronkurtz/gourmand/pull/35'}, {'url': 'https://github.com/sphinx-doc/sphinx/issues/3782'}, {'url': 'https://github.com/python/core-workflow/issues/6'}, {'url': 'https://github.com/rcbops/horizon-extensions/pull/10'}, {'url': 'https://github.com/ansible/ansible-modules-extras/pull/2208'}]"
		assert res == expected_issues

		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,self.DEFAULT_PROXIES,self.GIT_TYPES[2])
		res = crawler.crawl()
		expected_wiki = "[{'url': 'https://github.com/vault-team/vault-website'}, {'url': 'https://github.com/iiwaziri/wiki_learn'}, {'url': 'https://github.com/marcosaletta/Juno-CentOS7-Guide'}, {'url': 'https://github.com/MirantisDellCrowbar/crowbar'}, {'url': 'https://github.com/dellcloudedge/crowbar'}, {'url': 'https://github.com/vinayakponangi/crowbar'}, {'url': 'https://github.com/rhafer/crowbar'}, {'url': 'https://github.com/jamestyj/crowbar'}, {'url': 'https://github.com/eryeru12/crowbar'}, {'url': 'https://github.com/opencit/opencit'}]"
		assert res == expected_wiki

		"""Testing extended version with first sample"""
		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,self.DEFAULT_PROXIES,self.GIT_TYPES[0], more_info=True)
		res = crawler.crawl()
		expected_repo_more = "[{'url': 'https://github.com/atuldjadhav/DropBox-Cloud-Storage', 'extra': {'owner': 'atuldjadhav', 'language_stats': {'CSS': 52.0, 'JavaScript': 47.2, 'HTML': 0.8}}}]"
		assert res == expected_repo_more

		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,self.DEFAULT_PROXIES,self.GIT_TYPES[1], more_info=True)
		res = crawler.crawl()
		assert res == expected_issues

		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,self.DEFAULT_PROXIES,self.GIT_TYPES[2], more_info=True)
		res = crawler.crawl()
		assert res == expected_wiki

	def test_example_2(self):
		"""Testing non extended version with first sample"""
		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_2,self.DEFAULT_PROXIES,self.GIT_TYPES[0])
		res = crawler.crawl()
		
		expected_repo = "[{'url': 'https://github.com/GetBlimp/django-rest-framework-jwt'}, {'url': 'https://github.com/lock8/django-rest-framework-jwt-refresh-token'}, {'url': 'https://github.com/City-of-Helsinki/tunnistamo'}, {'url': 'https://github.com/chessbr/rest-jwt-permission'}, {'url': 'https://github.com/pyaf/djangular'}, {'url': 'https://github.com/thmarra/django-api'}, {'url': 'https://github.com/vaibhavkollipara/ChatroomApi'}]"
		assert res == expected_repo
		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_2,self.DEFAULT_PROXIES,self.GIT_TYPES[1])
		res = crawler.crawl()
		expected_issues = "[{'url': 'https://github.com/juanifioren/django-oidc-provider/issues/78'}, {'url': 'https://github.com/talons/talons/issues/35'}, {'url': 'https://github.com/ErickAgrazal/control-de-estaciones/pull/54'}, {'url': 'https://github.com/kavdev/bidr_project/pull/214'}, {'url': 'https://github.com/GetBlimp/django-rest-framework-jwt/issues/92'}, {'url': 'https://github.com/GetBlimp/django-rest-framework-jwt/issues/89'}, {'url': 'https://github.com/chriscauley/txrx.org/issues/114'}, {'url': 'https://github.com/sahlinet/tumbo-server/issues/1'}, {'url': 'https://github.com/django-json-api/django-rest-framework-json-api/issues/298'}, {'url': 'https://github.com/jhuapl-boss/boss-oidc/issues/3'}]"
		assert res == expected_issues

		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_2,self.DEFAULT_PROXIES,self.GIT_TYPES[2])
		res = crawler.crawl()
		expected_wiki = "[{'url': 'https://github.com/JeongTaekLim/TIL'}, {'url': 'https://github.com/kevindo0/djangoPython'}, {'url': 'https://github.com/xiuyanduan/xiuyanduan.github.io'}, {'url': 'https://github.com/findbyanswers/findbyanswers_management'}, {'url': 'https://github.com/trishaechual/doubletrouble-chat'}, {'url': 'https://github.com/swinton/django-rest-framework'}, {'url': 'https://github.com/Liu3420175/wiki'}, {'url': 'https://github.com/heytrav/drs-ops'}, {'url': 'https://github.com/westurner/wiki'}, {'url': 'https://github.com/ReCodEx/wiki'}]"
		assert res == expected_wiki

		"""Testing extended version with first sample"""
		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_2,self.DEFAULT_PROXIES,self.GIT_TYPES[0], more_info=True)
		res = crawler.crawl()
		print ([res])
		expected_repo_more = "[{'url': 'https://github.com/GetBlimp/django-rest-framework-jwt', 'extra': {'owner': 'GetBlimp', 'language_stats': {'Python': 100.0}}}, {'url': 'https://github.com/lock8/django-rest-framework-jwt-refresh-token', 'extra': {'owner': 'lock8', 'language_stats': {'Python': 96.4, 'Makefile': 3.6}}}, {'url': 'https://github.com/City-of-Helsinki/tunnistamo', 'extra': {'owner': 'City-of-Helsinki', 'language_stats': {'Python': 96.0, 'HTML': 2.7, 'CSS': 1.3}}}, {'url': 'https://github.com/chessbr/rest-jwt-permission', 'extra': {'owner': 'chessbr', 'language_stats': {'Python': 100.0}}}, {'url': 'https://github.com/pyaf/djangular', 'extra': {'owner': 'pyaf', 'language_stats': {'JavaScript': 99.0, 'Other': 1.0}}}, {'url': 'https://github.com/thmarra/django-api', 'extra': {'owner': 'thmarra', 'language_stats': {}}}, {'url': 'https://github.com/vaibhavkollipara/ChatroomApi', 'extra': {'owner': 'vaibhavkollipara', 'language_stats': {'Python': 100.0}}}]"
		assert res == expected_repo_more

		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_2,self.DEFAULT_PROXIES,self.GIT_TYPES[1], more_info=True)
		res = crawler.crawl()
		assert res == expected_issues

		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_2,self.DEFAULT_PROXIES,self.GIT_TYPES[2], more_info=True)
		res = crawler.crawl()
		assert res == expected_wiki


	def test_crawler_raises_exception_on_not_working_proxy_list(self):
		proxies = ["51.15.222.119:80","194.126.37.94:8080"]
		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,proxies,self.DEFAULT_TYPE)
		with pytest.raises(NoProxyAvailable):
			crawler.crawl()

	def test_crawler_raises_exception_on_invalid_type(self):
		crawler = GithubCrawlerExtended(self.DEFAULT_KEYWORDS_1,self.DEFAULT_PROXIES,'InvalidType')
		with pytest.raises(TypeNotSupported):
			crawler.crawl()


TestGithubCrawler().test_example_2()