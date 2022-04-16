#!/usr/bin/env python
# coding: utf-8


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
# get_ipython().system('pip install flask_pymongo')
from flask_pymongo import PyMongo
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# Set up Splinter



# # Step 1 - Scraping
# # NASA Mars News
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
# Assign the text to variables that you can reference later.

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # URL of page to be scraped -- Latest news
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    # Scrape page with Beautiful Soup
    html=browser.html
    soup=bs(html,'html.parser')


    # Extract article title and paragraph
    new_title = soup.find('div', class_="content_title").get_text(strip=True)
    news_p = soup.find("div", class_="article_teaser_body").get_text(strip=True)
    # article


    # # JPL Mars Space Images - Featured Image
    # URl for images
    image_url="https://spaceimages-mars.com/"
    browser.visit(image_url)
    time.sleep(1)


    # Create soup object from HTML
    html=browser.html
    # Parse HTML
    soup=bs(html,"html.parser")
    # Retrieve image url
    relative_image_path=soup.find('img', class_="headerimage fade-in")["src"]
    featured_image_url= image_url + relative_image_path
    featured_image_url


    # # Mars Facts
    # ULR for Mars Facts webpage 
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    time.sleep(1)


    # Create soup object from HTML
    html=browser.html


    # Pandas to scrape the table containing facts about Mars
    table = pd.read_html(facts_url)
    mars_facts = table[1]

    # Rename columns
    mars_facts.columns = ['Description','Value']

    # Reset Index to be description
    mars_facts.set_index('Description', inplace=True)
    mars_facts

    # Use Pandas to convert to a HTML table
    fact_table=mars_facts.to_html('table.html')


    # # Mars Hemispheres
    # Visit URL to get Mars hemisphere images
    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)


    #Container to hold  our loop iterations
    all_urls = []

    #Iterate through the 4 links to get the images needed
    for x in range(4):
        html = browser.html
        soup = bs(html, "html.parser")
        
        title = soup.find_all("h3")[x].get_text()
        browser.find_by_tag("h3")[x].click()
        
        html = browser.html
        soup = bs(html, "html.parser")
        
        img_url = soup.find("img", class_="wide-image")["src"]
        all_urls.append({
            "title":title,
            "img_url": hemi_url+img_url
        })
        browser.back()
    all_urls
    browser.quit()
    
    mars_report = {
        "new_title": new_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "all_urls": all_urls
    }
    return mars_report


#     # create soup object from html
#     html = browser.html
#     report = BeautifulSoup(html, "html.parser")
#     mars_report = report.find_all("p")
#     # add it to our surf data dict
# def build_report(mars_report):
#     final_report = ""
#     for p in mars_report:
#         final_report += " " + p.get_text()
#         print(final_report)
#     return final_report
    
    # print(final_report)

# mars_data= build_report(mars_report)
#     return mars_data
    

# return our surf data dict
# helper function to build surf report
