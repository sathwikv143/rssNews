#!/usr/bin/python3

# Modules required
import feedparser, re, textwrap
from datetime import date, timedelta
from dateutil import parser

# RSS Feed URLS to parse news from
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

# Code to Parse URL's at random and Display in output
for url in urls:
	parsed_url = feedparser.parse(url) # parsing URL
	entries = parsed_url.entries # list of all entries in a URL
	noe = len(entries) # get number of entries
	today = date.today() # get present day date
	yesterday = today - timedelta(1) # get yesterday date 
	for i in range(0,noe):
			dop = entries[i]['published'] # get of publishing in str
			dop_to_date = parser.parse(dop,ignoretz=True) # change dop to date
			if dop_to_date.date() == today or yesterday: # check for dop if is is present date or yesterday
				title = entries[i]['title'] # get title
				link = entries[i]['link'] # gget link
				summary = re.sub('<[^<]+?>','',str(entries[i]['summary']).replace('\n','')) # get summary
				print(50*"=") # print 50 equal's symbol to differentiate
				print(title+"\n") # print title
				for line in (textwrap.wrap(summary,width=70)): print(line) # wrap summary to length of 70
				print("\n"+link) # print link
