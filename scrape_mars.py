# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Save the browser's html attribute and clean it using BeautifulSoup

news_soup = BeautifulSoup(browser.html, 'html.parser')
news_soup.find('div',class_='content_title').text

#scraping the title from div
news_title = news_soup.find('div',class_='content_title').text
#scraping the title from div
news_p = news_soup.find('div',class_='article_teaser_body').text

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Save the browser's html attribute and clean it using BeautifulSoup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

#scrape image of mars
imgtag = img_soup.find('img', class_='headerimage')

relative_image_url_scraped_from_site = imgtag['src']

# Use the base url to create an absolute url or "current source"
featured_image_url = f'https://spaceimages-mars.com/{relative_image_url_scraped_from_site}'