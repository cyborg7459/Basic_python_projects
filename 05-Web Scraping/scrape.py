import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def display_posts(dict):
    return sorted(dict, key = lambda k:k['votes'], reverse=True)

def create_custom_hm(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title' : title, 'link': href, 'votes': points})
    return hn

pprint.pprint(display_posts(create_custom_hm(links,subtext)))