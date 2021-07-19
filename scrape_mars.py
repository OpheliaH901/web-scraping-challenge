# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt

# Set the executable path and initialize Splinter
from webdriver_manager.chrome import ChromeDriverManager

def scrape_mars_websites():
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

    # WHEN USING THE pd.read_html function, WHY DO YOU THINK WE HAD TO GET THE ZERO-th INDEX?
    # HINT: Peak around the website below to perhaps understand why...
    df = pd.read_html('https://galaxyfacts-mars.com')[0]

    # WRITE YOUR OWN CODE TO CLEAN THIS DATAFRAME; rename column names
    new_index_df = df.set_index(0)

    header_row = 0

    new_index_df.columns = new_index_df.iloc[header_row]
    drop_row1_df = new_index_df.iloc[0: , :]

    # CONVERT TO HTML :)
    # YAY PAND
    mars_facts = df.to_html()

    hem_url = 'https://marshemispheres.com/'
    browser.visit(hem_url)

    # Save the browser's html attribute and clean it using BeautifulSoup

    hemispheres_soup = BeautifulSoup(browser.html, 'html.parser')
    hem_image_path = hemispheres_soup.find('div', class_='collapsible results').find_all('a', class_='itemLink product-item')




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
            



    # Finally, close the Google Chrome window...
    browser.quit()

    scraped_data = {
            "news_title": news_title,
            "news_paragraph": news_p,
            "featured_image": featured_image_url ,
            "facts": mars_facts,
            "hemispheres": hemisphere_image_urls,
            "last_modified": dt.datetime.now()
        }

    return scraped_data