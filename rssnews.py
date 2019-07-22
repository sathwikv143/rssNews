#!/usr/bin/python3

# Required Modules
import feedparser, re, textwrap
from datetime import date, timedelta
from dateutil import parser

# Get Dates of Present and Previous Day's
today = date.today()
yesterday = today - timedelta(1)

# Display the Parsed News
def display_news(title,summary,link):
	print(50*"=")
	print(title+"\n")
	for line in (textwrap.wrap(summary,width=70)): print(line)
	print("\n"+link)

# Get the date published of an Entry
def get_date(entries):
	dop = entries['published']
	dop_to_date = parser.parse(dop,ignoretz=True)
	dop_date = dop_to_date.date()
	return dop_date

# Get the title, link and summary of the news
def get_news(entries,noe,parsed_url):
	for i in range(0,noe):
		dop_date = get_date(entries[i])
		if dop_date == today:
			title = entries[i]['title']
			link = entries[i]['link']
			summary = re.sub('<[^<]+?>','',str(entries[i]['summary']).replace('\n',''))
			display_news(title,summary,link)

# Parse the URL's with feedparser
def parse_url(urls):
	for i in urls:
		parsed_url = feedparser.parse(i)
		entries = parsed_url.entries
		noe = len(entries)
		get_news(entries,noe,parsed_url)

# main
if __name__ == "__main__":
	urls = [
		'https://feeds.feedburner.com/TheHackersNews',
		# 'https://www.darknet.org.uk/feed/',
		'http://blog.extremehacking.org/feed/',
		'https://latesthackingnews.com/feed/',
		'https://www.hackread.com/feed',
		'https://www.zdnet.com/topic/security/rss.xml',
		# 'https://www.zdnet.com/news/rss.xml',
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
		'https://nakedsecurity.sophos.com/feed/'
	]
	parse_url(urls)
