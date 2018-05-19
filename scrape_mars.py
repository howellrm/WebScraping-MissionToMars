from splinter import Browser
from bs4 import BeautifulSoup
import pymongo
from splinter import Browser
import tweepy
import time
import pandas as pd
import requests

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    scrape_mars_dict = {}
    return mars_news_function()

# NASA Mars News

def mars_news_function():
    mars_weather_dict = {}

    # Set Up for NASA Mars News
    url_Mars_News = "https://mars.nasa.gov/news/"

    browser.visit(url_Mars_News)

    # find news title

    news_title = browser.find_by_css('.content_title').first.text

    mars_weather_dict['news_title'] = news_title

    # find news paragraph

    news_para = browser.find_by_css('.article_teaser_body').first.text
    mars_weather_dict['news_para'] = news_para

    # JPL Mars Space Images - Featured Image
    
    url_Mars_Space_Images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url_Mars_Space_Images)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')


    # find the newest image for this site https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    mars_image_results = soup.find("footer")
    mars_image = mars_image_results.find('a')['data-fancybox-href']

    feature_image = "https://www.jpl.nasa.gov" + mars_image


    # Set Up for Mars Weather

    url_Mars_Weather = "https://twitter.com/marswxreport?lang=en"

    browser.visit(url_Mars_Weather)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')

    print("after twitter")

    # Locate Mars Weather
    weather_info_list = []

    for weather_info in soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        weather_info_list.append(weather_info.text)

    # Variable for latest Mars Information
    Latest_Mars_Weather = weather_info_list[0]
    mars_weather_dict['latest_mars_weather'] = weather_info_list

    mars_weather_dict["mar_weather"] = Latest_Mars_Weather

    return mars_weather_dict




# Mars Facts

def Mars_Facts_table_function():
    
    browser = init_browser()

    df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")

    df_Mars_Facts = df_Mars_Facts[0]

    df_Mars_Facts.rename_axis({0:"Parameters", 1:"Values"},axis=1, inplace=True)

    df_Mars_Facts_table = df_Mars_Facts.to_html("Mars_Facts_Table.html")

    df_Mars_Facts_dict = {"df_Mars_Facts": df_Mars_Facts_table}

    return df_Mars_Facts_dict




# Mars hemisphere
def hemisphere_images():
    image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    full_hemisphere_dict = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}

    return full_hemisphere_dict

