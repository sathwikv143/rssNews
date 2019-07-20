#!/usr/bin/python3

import feedparser, re, textwrap, random
from datetime import date, timedelta
from dateutil import parser

urls = [
	'https://feeds.feedburner.com/TheHackersNews',
	# 'https://www.darknet.org.uk/feed/',
	'http://blog.extremehacking.org/feed/',
	'https://latesthackingnews.com/feed/',
	'https://www.hackread.com/feed',
	'https://www.zdnet.com/topic/security/rss.xml',
	'https://www.zdnet.com/news/rss.xml',
	'https://gbhackers.com/feed/',
	'https://www.darkreading.com/rss_simple.asp',
	'https://www.darkreading.com/rss_simple.asp?f_n=644&f_ln=Attacks/Breaches',
	'https://www.darkreading.com/rss_simple.asp?f_n=645&f_ln=Application%20Security',
	'https://www.darkreading.com/rss_simple.asp?f_n=646&f_ln=Database%20Security',
	'https://www.darkreading.com/rss_simple.asp?f_n=647&f_ln=Cloud',
	'https://www.darkreading.com/rss_simple.asp?f_n=648&f_ln=Endpoint',
	'https://www.darkreading.com/rss_simple.asp?f_n=649&f_ln=Authentication',
	'https://www.darkreading.com/rss_simple.asp?f_n=650&f_ln=Privacy',
	'https://www.darkreading.com/rss_simple.asp?f_n=651&f_ln=Mobile',
	'https://www.darkreading.com/rss_simple.asp?f_n=652&f_ln=Perimeter',
	'https://www.darkreading.com/rss_simple.asp?f_n=653&f_ln=Risk',
	'https://www.darkreading.com/rss_simple.asp?f_n=654&f_ln=Compliance',
	'https://www.darkreading.com/rss_simple.asp?f_n=657&f_ln=Identity%20and%20Access%20Management',
	'https://www.darkreading.com/rss_simple.asp?f_n=658&f_ln=Analytics',
	'https://www.darkreading.com/rss_simple.asp?f_n=659&f_ln=Threat%20Intelligence',
	'https://www.darkreading.com/rss_simple.asp?f_n=660&f_ln=Security%20Monitoring',
	'https://www.darkreading.com/rss_simple.asp?f_n=661&f_ln=Vulnerabilities%20/%20Threats',
	'https://www.darkreading.com/rss_simple.asp?f_n=662&f_ln=Advanced%20Threats',
	'https://www.darkreading.com/rss_simple.asp?f_n=663&f_ln=Insider%20Threats',
	'https://www.darkreading.com/rss_simple.asp?f_n=664&f_ln=Vulnerability%20Management',
	# 'https://exploit.kitploit.com/feeds/posts/default?alt=rss',
	'https://threatpost.com/feed/',
	'https://blog.knowbe4.com/rss.xml',
	'https://hackercombat.com/feed/',
	'https://securityaffairs.co/wordpress/feed',
	'https://www.helpnetsecurity.com/feed/',
	'https://www.theregister.co.uk/security/headlines.atom',
	'https://feeds.feedburner.com/securityweek',
	'https://www.itsecurityguru.org/feed/',
	'https://nakedsecurity.sophos.com/feed/',
]

# for url in urls:
# 	parsed_url = feedparser.parse(url)
# 	# n_o_entries = len(parsed_url.entries)
# 	for i in range(0,11):
# 		title = parsed_url.entries[i]['title']
# 		link = parsed_url.entries[i]['link']
# 		summary = re.sub('<[^<]+?>','',str(parsed_url.entries[i]['summary']).replace('\n',''))
# 		print(50*"=")
# 		print(title+"\n\n"+summary+"\n\nLink:"+link)

for url in random.sample(urls, len(urls)):
	parsed_url = feedparser.parse(url)
	entries = parsed_url.entries
	noe = len(entries)
	today = date.today()
	yesterday = today - timedelta(1)
	for i in range(0,noe):
			dop = entries[i]['published']
			dop_to_date = parser.parse(dop,ignoretz=True)
			if dop_to_date.date() == today or yesterday:
				title = entries[i]['title']
				link = entries[i]['link']
				summary = re.sub('<[^<]+?>','',str(entries[i]['summary']).replace('\n',''))
				print(50*"=")
				print(title+"\n")
				for line in (textwrap.wrap(summary,width=70)): print(line)
				print("\n"+link)