# Scrapping file 
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
#Initiate headless driver for deployment.  set your executable path for scraping changed headless=False which allows to see scraping taking place
#       see the word "browser" here twice, one is the name of the variable passed into the function and the other is the name of a parameter.
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
   #set our news title and paragraph variables  FUNCTION CALL 
    news_title, news_paragraph = mars_news(browser)

    # CAll all scraping functions and store results in a dictionary  Python
    # added the hemispheres from line 118 
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

# Stop webdriver and return data
    browser.quit()
    return data


# 10.5.2 Insert function
def mars_news(browser):

#Scrape Mars News  
# Visit the mars nasa news site
    # url = 'https://redplanetscience.com' changed at Module 10.5.3
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

# Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')

# Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

#  Featured Image.  Scrape the featured image from another Mars website #JPL Space Images

def featured_image(browser):

# Visit URL
    # url = 'https://spaceimages-mars.com'  url changed in Module 10.5.2
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)


# Find and click the full image button.  The browsser finds an element by its tag

    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

# Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

# Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

# Use the base URL to create an absolute URL
    #img_url = f'https://spaceimages-mars.com/{img_url_rel}'   url changed in Module 10.5.2
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
    return img_url

# # MARS FACTS - scraping from tables Adding BaseException to our except block for error handling
# Visit URL url = 'https://galaxyfacts-mars.com/'
#import pandas as pd

def mars_facts():
    # add try/except for error handling  Panda read html
    try:
    # use 'read_html" to scrape the facts table into a dataframe    
        #df = pd.read_html('https://galaxyfacts-mars.com')[0]    url changed in Module 10.5.2
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
    except BaseException:
        return None
# Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
        #df


# Convert dataframe into HTML format, add bootstrap  Changed in Module 10.5.2
    #return df.to_html()
    return df.to_html(classes="table table-striped")

# Delverable 2
def hemispheres(browser):

    # Visit the URL 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Parse the resulting html with soup
    hemi_html = browser.html
    hemi_soup = soup(hemi_html, 'html.parser')


    # Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # Write code to retrieve the image urls and titles for each hemisphere.
    items = hemi_soup.find_all('div', class_='item')

    main_url = "https://astrogeology.usgs.gov/"

    # Create loop to scrape through all hemisphere information
    for x in items: 
    
        hemisphere = {}
        titles = x.find('h3').text
        # create link for full image
        link_ref = x.find('a', class_='itemLink product-item')['href']
        # Use the base URL to create an absolute URL and browser visit
        browser.visit(main_url + link_ref)
        # parse the data
        image_html = browser.html
        image_soup = soup(image_html, 'html.parser')
        download = image_soup.find('div', class_= 'downloads')
        img_url = download.find('a')['href']
    
        print(titles)
        print(img_url)
    
        # append list
        hemisphere['img_url'] = img_url
        hemisphere['title'] = titles
        hemisphere_image_urls.append(hemisphere)
        browser.back()  
    
   # Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls

#browser.quit()
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())


