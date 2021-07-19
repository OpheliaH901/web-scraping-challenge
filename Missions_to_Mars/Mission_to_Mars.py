#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[4]:


# Save the browser's html attribute and clean it using BeautifulSoup

news_soup = BeautifulSoup(browser.html, 'html.parser')
news_soup.find('div',class_='content_title').text


# In[5]:


#scraping the title from div
news_title = news_soup.find('div',class_='content_title').text
news_title


# In[6]:


#scraping the title from div
news_p = news_soup.find('div',class_='article_teaser_body').text
news_p


# ### JPL Space Images Featured Image

# In[7]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[8]:


# Save the browser's html attribute and clean it using BeautifulSoup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[9]:


#scrape image of mars
imgtag = img_soup.find('img', class_='headerimage')

relative_image_url_scraped_from_site = imgtag['src']

# Use the base url to create an absolute url or "current source"
featured_image_url = f'https://spaceimages-mars.com/{relative_image_url_scraped_from_site}'
featured_image_url 


# ### Mars Facts

# In[10]:


# WHEN USING THE pd.read_html function, WHY DO YOU THINK WE HAD TO GET THE ZERO-th INDEX?
# HINT: Peak around the website below to perhaps understand why...
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df


# In[11]:


# WRITE YOUR OWN CODE TO CLEAN THIS DATAFRAME; rename column names
new_index_df = df.set_index(0)
new_index_df


# In[12]:


header_row = 0

new_index_df.columns = new_index_df.iloc[header_row]


# In[13]:


new_index_df


# In[14]:


drop_row1_df = new_index_df.iloc[0: , :]
drop_row1_df 


# In[15]:


# CONVERT TO HTML :)
# YAY PAND
mars_facts = df.to_html()
mars_facts


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


hem_url = 'https://marshemispheres.com/'
browser.visit(hem_url)

# Save the browser's html attribute and clean it using BeautifulSoup

hemispheres_soup = BeautifulSoup(browser.html, 'html.parser')
hem_image_path = hemispheres_soup.find('div', class_='collapsible results').find_all('a', class_='itemLink product-item')
hem_image_path


# In[17]:


# capture one hemisphere link
hemisphere = hem_image_path[0]
browser.visit(f"{hem_url}{hemisphere['href']}")

hemisphere_soup = BeautifulSoup(browser.html, 'html.parser')
hemisphere_img_link = f"{hem_url}{hemisphere_soup.find('img', class_='wide-image')['src']}"

hemisphere_soup.find('h2', class_='title').text
# hemisphere_img_link




# In[18]:


# Create a list to hold the images and titles.
hemisphere_image_urls = []

# Write a for loop to retrieve the image urls and titles for each hemisphere in the url above.
for hemisphere in hem_image_path:
    try:
        browser.visit(f"{hem_url}{hemisphere['href']}")

        hemisphere_soup = BeautifulSoup(browser.html, 'html.parser')
        hemisphere_img_link = f"{hem_url}{hemisphere_soup.find('img', class_='wide-image')['src']}"


        # Store data in a dictionary
        hemisphere_data = {
            'hem_title': hemisphere_soup.find('h2', class_='title').text,
            'hem_img_url': hemisphere_img_link
        }
    
        if hemisphere_data not in hemisphere_image_urls:
            hemisphere_image_urls.append(hemisphere_data)
        
        
    except:
        print("pass")
        
(hemisphere_image_urls)


# In[19]:


# Finally, close the Google Chrome window...
browser.quit()

