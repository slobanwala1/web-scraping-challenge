from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

# Setup chrome driver for Chrome tool
def init_browser():
    #executable_path = {"executable_path": "C:/chromedriver/chromedriver"}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

# Scrape function grabbed from jupyter notebook
def scrape():
    
    # Setup splinter
    browser = init_browser()
    #browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    mars_news_soup = BeautifulSoup(response.text, 'html.parser')

    # Grab title and content of the latest mars news
    news_title = mars_news_soup.find("div", class_="content_title").find('a').text

    news_content = mars_news_soup.find("div", class_="rollover_description_inner").text

    # Close Browser.
    browser.quit()
    

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
