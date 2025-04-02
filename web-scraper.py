import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com'
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

title_elements = soup.select('span.titleline > a')
titles = [title.text for title in title_elements]
links = [el.get('href') for el in title_elements]
upvotes = [int(score.text.split()[0]) for score in soup.select('span.score')]

for title, link in zip(titles, links):
    print(f'- [{title}]({link}) - Upvotes: {upvotes.pop(0)}')