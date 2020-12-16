import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setup chrome driver for Chrome tool
def init_browser():
    #executable_path = {"executable_path": "C:/chromedriver/chromedriver"}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

# Scrape function grabbed from jupyter notebook
def scrape():
    
    # ------------------------------PART 1 START-------------------------------#
    """ NASA Mars Latest News Title and Content """
    # Setup splinter
    browser = init_browser()
    #browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    news_url = "https://mars.nasa.gov/news/"

    browser.visit(news_url)

    # Store the html object
    news_html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    mars_news_soup = BeautifulSoup(news_html, 'html.parser')

    # Could'nt grab title so grabbing content instead
    news_title = mars_news_soup.find('div', class_='list_text').find('a').text

    news_content = mars_news_soup.find('div', class_='article_teaser_body').text

    # Close Browser.
    browser.quit()
    
    print(news_title + '\n' + news_content)
    
    # ------------------------------PART 1 END-------------------------------#
    
    """ JPL Mars Space Images - Featured Image """
    # Setup splinter
    browser = init_browser()
    
    jpl_mars_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_mars_img_url)
    
    # https://splinter.readthedocs.io/en/latest/api/driver-and-element-api.html
    # use click_link_by_partial_text
    browser.click_link_by_partial_text("FULL IMAGE")
    
    # Have to click more info to open up bigger image, use find_link_by_partial_text again. Really useful function
    browser.is_element_present_by_text("more info", wait_time=1)
    bigger_img_elem = browser.find_link_by_partial_text("more info")
    bigger_img_elem.click()
    
    # Store the html object
    img_html = browser.html
    
    # Time to strip the image and store
    mars_img_soup = BeautifulSoup(img_html, 'html.parser')
    
    mars_img_url = mars_img_soup.find("figure", class_="lede").a["href"]
    
    featured_image_url = f'https://www.jpl.nasa.gov{mars_img_url}'
    
    # Close Browser.
    browser.quit()
    
    print(featured_image_url)
    
    # ------------------------------PART 2 END-------------------------------#
    
    # ------------------------------PART 3 START-------------------------------#
    
    """ Mars Facts """
    # Much easier since just scraping a table, and we did a ton of that in the simpsons analysis for ETL project
    mars_facts_url = "https://space-facts.com/mars/"
    
    # use read_html
    mars_facts_tables = pd.read_html(mars_facts_url)
    
    mars_facts_df = mars_facts_tables[0]
    
    # Set first column to Description as the prompt shows, and the second is Measurement/Units
    mars_facts_df.columns = ['Description', 'Measurement/Units']
    
    # mars_facts_df
    
    
    # To use on website we need it in html format
    # Remove header just use html to produce header as it looks nicer
    mars_facts_df.to_html('Resources/mars_facts.html', index=False, header=False)
    mars_facts = mars_facts_df.to_html(index=False, header=False)
    
    # ------------------------------PART 3 END-------------------------------#
    
    # ------------------------------PART 4 START-------------------------------#
    
    """ Mars Hemispheres """
    browser = init_browser()
    
    mars_hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    mars_hemis_homepage = "https://astrogeology.usgs.gov";
    
    browser.visit(mars_hemis_url)
    
    # store into html object again
    hemis_html = browser.html
    
    hemis_soup = BeautifulSoup(hemis_html, 'html.parser')
    
    # Grabs all 4 divs of the hemispheres
    hemis_url = hemis_soup.find_all("div", class_="item")
    
    # Store them as seperate html objects
    hemis_url_all = []
    
    for hemisphere in hemis_url:
        curr_hemis_url = hemisphere.find('a')['href']
        hemis_url_all.append(curr_hemis_url)
    
    # Close Browser.
    browser.quit()
    
    print(hemis_url_all)
    
    # Go through each link and store title and full link in a dict
    mars_hemis_urls = []
    
    for hemisphere in hemis_url_all:
        
        # create full link
        mars_url_full = mars_hemis_homepage + hemisphere
        
        # Abuse splinter again
        browser = init_browser()
        browser.visit(mars_url_full)
        
        hemis_html = browser.html
        hemis_soup = BeautifulSoup(hemis_html, 'html.parser')
        
        # Grab title
        hemis_title = hemis_soup.find("h2", class_="title").text
        
        # Grab the full.jpg for all the Hemispheres, aka the large size
        hemis_img_url = hemis_soup.find("li").a['href']
        
        mars_hemis_urls.append({'title': hemis_title, 'img_url': hemis_img_url})
        
        # Close Browser.
        browser.quit()
    
    print(mars_hemis_urls)

# ------------------------------PART 4 END-------------------------------#

# ------------------------------PART 5 START-------------------------------#

    # Step 2 - MongoDB and Flask Application
    mission_to_mars_data = {}
    
    # Store all data
    mission_to_mars_data['news_title'] = news_title
    mission_to_mars_data['news_content'] = news_content
    mission_to_mars_data['featured_image_url'] = featured_image_url
    mission_to_mars_data['mars_facts'] = mars_facts
    mission_to_mars_data['mars_hemisphere_urls'] = mars_hemis_urls
    
    print(mission_to_mars_data)
    
    print("Scraping Finished...")
    return mission_to_mars_data


