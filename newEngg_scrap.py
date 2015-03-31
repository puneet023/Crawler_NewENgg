# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:27:10 2015

@author: Puneet
"""
#Note: 1> This should not be used for commercial purpose
#      2> The website might have some restrictions for crawling, read it and adhere to it.

#importing urllib, beautifulsoup and csv
import urllib 
from bs4 import BeautifulSoup
import csv
import re

count =0 
#creating a file
with open('NewEngg_data_test2_page3.csv','wb') as f1:
    writer=csv.writer(f1, delimiter=',', lineterminator = '\n')
    #Header Row

    writer.writerow(["PDT_NAME","Hyperlink", "brand", "Category", "reviewer1", "reviewer2", "review1", "review2"])
    #Starting Url to grab all the links
    htmltext = urllib.urlopen("http://www.newegg.com/global/sg/Product/ProductList.aspx?Submit=ENE&N=100056443&IsNodeId=1&bop=And&SpeTabStoreType=270&Pagesize=90&Page=3").read()
    soup = BeautifulSoup(htmltext)
    
    #To get a better readability
    print(soup.prettify())

    # Crawling all the links and names from starting page
    g_data = soup.find_all('div', {"class":"wrapper"})
    for item in g_data:
        count = count + 1
        #Using tag "a" and title class to extract information
        link = item.find_all('a', {"title":"View Details"})
        
        #Extracting link for each phone for more information
        full_link = [x.get("href") for x in link]
        
        #Product Name- from tag span and class businees_school_name
        PDT_NAME = item.find('span', {"class":"itemDescription"}).text.strip()
        #print   pdt name, full_link[0]
        
        # For each pdt link, again parse html page
        htmltext1 = urllib.urlopen(full_link[0]).read()
        soup1 = BeautifulSoup(htmltext1)
        
        #Check "row =" line to understand use of dictionary
        
        stat = {}
                
        #brand name
        a = soup1.find_all('div', {"id":"detailSpecContent"})[0]
        try:
            brandName = a.find_all('dd')[0].text
        except:
            brandName = "NA"   
            
        #product category
        a = soup1.find_all('div', {"id":"detailSpecContent"})[0]
        try:
            pdtCat = a.find_all('dd')[4].text
        except:
            pdtCat = "NA"
    
        
        #review
        try:
            a = soup1.find_all('table', {"class":"grpReviews"})[0]
            try:
                reviewer1 = a.find_all('em')[0].text
            except:
                reviewer1 = "NA"
        except:
            reviewer1 = "NA"
    
        try:
            a2 = soup1.find_all('th', {"class":"reviewer"})[1]
            try:
                reviewer2 = a2.find_all('em')[0].text
            except:
                reviewer2 = "NA"
        except:
            reviewer2 = "NA"
    
        try:
            a3 = soup1.find_all('table', {"class":"grpReviews"})[0]
            try:
                review1 = a3.find_all('h3')[1].text
            except:
                review1 = "NA"
        except:
            review1 = "NA"
        
        try:
            a3 = soup1.find_all('table', {"class":"grpReviews"})[0]
            try:
                review2 = a3.find_all('h3')[2].text
            except:
                review2 = "NA"
        except:
            review2 = "NA"
        
    
        #Making a list of tupules             
        row = [(PDT_NAME),(full_link[0]), (brandName), (pdtCat) ,(reviewer1), (reviewer2), (review1), (review2)]
        print row
        #writing to file
        writer.writerow(row)
        print count
        
