
# coding: utf-8

# <h1>Mission to Mars</h1>
# 
# In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.
# 

# <h3>Step 1 - Scraping</h3>
# 
# Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
# 
# Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. 
# 
# The following outlines what you need to scrape.

# <h3>Import Dependencies</h3>
# 
# Import BeautifulSoup for parsing and splinter for site navigation.

# In[49]:


from bs4 import BeautifulSoup
from splinter import Browser

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser("chrome", **executable_path, headless=False)


# <h3>NASA Mars News</h3>
# 
# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragragh Text. Assign the text to variables that you can reference later.
# 

# In[79]:


url_Mars_News = "https://mars.nasa.gov/news/"

browser.visit(url_Mars_News)

html = browser.html
soup = BeautifulSoup(html,'html.parser')


# In[80]:


# find news headings 

article_heading_list = []

for article_heading in soup.find_all('div',class_="content_title"):
    article_heading_list.append(article_heading.find('a').text)
    
    

# find information about new articles 

article_details_list = []

for article_details in soup.find_all('div',class_="article_teaser_body"):
    article_details_list.append(article_details.text)
    
    
    
# Varibles for Latest New Articles and Titles
    
latest_News_Title = article_heading_list[0]

latest_News_Details = article_details_list[0]

News_dict = {"Headline": latest_News_Title,"Details": latest_News_Details}

News_dict['Headline']

print("Title:",latest_News_Title)
print('-'*60)
print("Latest News Details:",latest_News_Details)


# In[56]:


# # save the most recent article, title and date
# article = soup.find("div", class_="list_text")
# news_p = article.find("div", class_="article_teaser_body").text
# news_title = article.find("div", class_="content_title").text
# news_date = article.find("div", class_="list_date").text
# print(news_date)
# print(news_title)
# print(news_p)


# <h3>JPL Mars Space Images - Featured Image</h3>
# 
# Visit the url for JPL's Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# 
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# 
# Make sure to find the image url to the full size `.jpg` image.
# 
# Make sure to save a complete url string for this image.
# 

# In[73]:


url_Mars_Space_Images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

browser.visit(url_Mars_Space_Images)
time.sleep(1)

html = browser.html

soup = BeautifulSoup(html,'html.parser')


# In[74]:


# find the newest image for this site https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

featured_image_list = []

for image in soup.find_all('div',class_="img"):
    featured_image_list.append(image.find('img').get('src'))


# In[75]:


#feature image
feature_Image = featured_image_list[0]

#feature image url 
feature_Image_url = "https://www.jpl.nasa.gov/" + feature_Image

feature_Image_dict = {"image": feature_Image_url}

# print feature image url 

print("Feature Image URL:", feature_Image_url)


# In[57]:


# Visit the JPL Mars URL
# url_spc_img = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
# browser.visit(url_spc_img)


# In[58]:


# Scrape the browser into soup and use soup to find the image of mars
# Save the image url to a variable called `img_url`
# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')
# image = soup.find("img", class_="thumb")["src"]
# img_url = "https://jpl.nasa.gov"+image
# featured_image_url = img_url


# In[59]:


# # Use the requests library to download and save the image from the `img_url` above
# import requests
# import shutil

# response = requests.get(img_url, stream=True)
# with open('img.jpg', 'wb') as out_file:
#     shutil.copyfileobj(response.raw, out_file)


# In[60]:


# # Display the image with IPython.display
# from IPython.display import Image

# Image(url='img.jpg')


# <h3>Mars Weather</h3>
# 
# Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.

# In[61]:


# # Visit the Mars Weather twitter account and scrap the lates 
# # Mars weather tweet.
# import tweepy
# # Twitter API Keys
# from config import (consumer_key, 
#                     consumer_secret, 
#                     access_token, 
#                     access_token_secret)

# # Setup Tweepy API Authentication
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# target_user = "marswxreport"
# full_tweet = api.user_timeline(target_user , count = 1)
# mars_weather=full_tweet[0]['text']
# mars_weather


# In[62]:


url_Mars_Weather = "https://twitter.com/marswxreport?lang=en"

browser.visit(url_Mars_Weather)
time.sleep(1)

html = browser.html

soup = BeautifulSoup(html,'html.parser')

weather_info_list = []

for weather_info in soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
    weather_info_list.append(weather_info.text)

Latest_Mars_Weather = weather_info_list[0]

mars_weather_dict = {"mar_weather": Latest_Mars_Weather }

# print mars info

print('Latest Mars Weather:',Latest_Mars_Weather)


# <h3>Mars Facts</h3>
# 
# Visit the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# 
# Use Pandas to convert the data to a HTML table string.

# In[39]:


# Visit the Mars facts webpage and scrape table data into Pandas
# url_facts = "http://space-facts.com/mars/"
# browser.visit(url_facts)


# In[63]:


# place data into a dataframe, clean it up and 
# output it into an HTML table

# import pandas as pd 

# grab=pd.read_html(url_facts)
# mars_data=pd.DataFrame(grab[0])
# mars_data.columns=['Mars','Data']
# mars_table=mars_data.set_index("Mars")
# marsdata = mars_table.to_html(classes='marsdata')
# marsdata=marsdata.replace('\n', ' ')
# marsdata


# In[64]:


import pandas as pd

df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")

df_Mars_Facts = df_Mars_Facts[0]

df_Mars_Facts.rename_axis({0:"Parameters", 1:"Values"},axis=1, inplace=True)

df_Mars_Facts


# In[65]:


df_Mars_Facts_table = df_Mars_Facts.to_html("df_Mars_Facts_Table.html",index=False)
df_Mars_Facts_dict = {"df_Mars_Facts": df_Mars_Facts_table}


# <h3>Mars Hemisperes</h3>
# 
# Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
# 
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# Save both the image url string for the full resolution hemipshere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# 
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# In[67]:


# Visit the USGS Astogeology site and scrape pictures of the hemispheres
url_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_hemi)


# In[68]:


# Use splinter to loop through the 4 images and load them into a dictionary
import time 
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
# mars_hemis=[]


# In[69]:


mars_hemisperes_title_list = []

for img_title in soup.find_all('div',class_="description"):
    mars_hemisperes_title_list.append(img_title.find('h3').text)

    
mars_hemisphere_image_url = []

for image in soup.find_all('div',class_="item"):
    
    url = "https://astrogeology.usgs.gov/"
    
    mars_hemisphere_image_url.append(url + image.find('img').get('src'))

mars_hemisphere_image_url


# In[70]:


full_image_url = []

for each_url in mars_hemisphere_image_url:
    
    split_url = each_url.split(".tif_thumb.png")[0]
    
    image_url = split_url + ".tif/full.jpg"
    
    full_image_url.append(image_url)

full_image_url


# In[71]:


mars_hemisperes_title_list


# In[72]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": full_image_url[3]},
    {"title": "Cerberus Hemisphere", "img_url": full_image_url[0]},
    {"title": "Schiaparelli Hemisphere", "img_url": full_image_url[1]},
    {"title": "Syrtis Major Hemisphere", "img_url": full_image_url[2]},
]


# In[66]:


image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

full_image = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}

full_image['image_one']


# In[26]:


# # loop through the four tags and load the data to the dictionary

# for i in range (4):
#     time.sleep(5)
#     images = browser.find_by_tag('h3')
#     images[i].click()
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
#     partial = soup.find("img", class_="wide-image")["src"]
#     img_title = soup.find("h2",class_="title").text
#     img_url = 'https://astrogeology.usgs.gov'+ partial
#     dictionary={"title":img_title,"img_url":img_url}
#     mars_hemis.append(dictionary)
#     browser.back()


# In[27]:


# print(mars_hemis)


# <h3>Step 2 - MongoDB and Flask Application</h3>
# 
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
# 
# Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
# 
# Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
# 
# Store the return value in Mongo as a Python dictionary.
# 
# Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
# 
# Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

# In[41]:


from splinter import Browser
from bs4 import BeautifulSoup
import time 
import pandas as pd


# In[42]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser("chrome", **executable_path, headless=False)


# In[43]:


# NASA Mars News

def mars_news_function():

    browser = init_browser()

    # Set Up for NASA Mars News
    url_Mars_News = "https://mars.nasa.gov/news/"

    browser.visit(url_Mars_News)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')

    # find news headings 

    article_heading_list = []

    for article_heading in soup.find_all('div',class_="content_title"):
        article_heading_list.append(article_heading.find('a').text)

    # find information about new articles 

    article_details_list = []

    for article_details in soup.find_all('div',class_="article_teaser_body"):
        
        article_details_list.append(article_details.text)
        
    # Varibles for Latest New Articles and Titles

    latest_News_Title = article_heading_list[0]

    latest_News_Details = article_details_list[0]

    News_dict = {"Headline": latest_News_Title,"Details": latest_News_Details}


    return News_dict


# In[44]:


# JPL Mars Space Images - Featured Image
def Feature_Image_function():
    
    browser = init_browser()

    url_Mars_Space_Images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url_Mars_Space_Images)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')


    # find the newest image for this site https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    featured_image_list = []

    for image in soup.find_all('div',class_="img"):
        featured_image_list.append(image.find('img').get('src'))


    #feature image
    feature_Image = featured_image_list[0]

    #feature image url 
    feature_Image_url = "https://www.jpl.nasa.gov/" + feature_Image

    feature_Image_dict = {"image": feature_Image_url}

    return feature_Image_dict


# In[45]:


# Mars Weather
def Weather_function():
    
    browser = init_browser()

    # Set Up for Mars Weather

    url_Mars_Weather = "https://twitter.com/marswxreport?lang=en"

    browser.visit(url_Mars_Weather)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')

    # Locate Mars Weather
    weather_info_list = []

    for weather_info in soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        weather_info_list.append(weather_info.text)

    # Variable for latest Mars Information
    Latest_Mars_Weather = weather_info_list[0]

    mars_weather_dict = {"mar_weather": Latest_Mars_Weather }

    return mars_weather_dict


# In[46]:


# Mars Facts

def Mars_Facts_table_function():
    
    browser = init_browser()

    df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")

    df_Mars_Facts = df_Mars_Facts[0]

    df_Mars_Facts.rename_axis({0:"Parameters", 1:"Values"},axis=1, inplace=True)

    df_Mars_Facts_table = df_Mars_Facts.to_html("Mars_Facts_Table.html")

    df_Mars_Facts_dict = {"df_Mars_Facts": df_Mars_Facts_table}

    return df_Mars_Facts_dict


# In[47]:


# Mars hemisphere
def hemisphere_images():
    image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    full_hemisphere_dict = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}

    return full_hemisphere_dict


# <h3>Hints</h3>
# 
# Use splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
# 
# Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.
# 
# Use Bootstrap to structure your HTML template.
