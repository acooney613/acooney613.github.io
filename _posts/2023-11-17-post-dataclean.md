---
layout: post
title: MLB Team Payroll and its Affects on Fan Attendance (Data Cleaning)
author: Aidan Cooney
description: How to scrape and clean data for MLB Team Payroll and Attendance 
image: "/assets/images/baseball.png"
markdown: kramdown
kramdown:
  parse_block_html: true
---

## Background

As a fan of the major league baseball team the Oakland Athletics, I have seen and heard all of the news surrounding the pending move of the team to Las Vegas. The Oakland Athletics first moved to Oakland in 1968 and have been there ever since. With the rumors of the move, I wondered what potential causes of this move could be. I have heard rumors that a lack of fans is a major reason for the move, and decided I wanted to explore that further. I wanted to know what factors would contribute to overall fan attendance to see what the potential root of the "lack of fan support" could be.  

I gathered and scraped several different websites and created 5 seperate datasets that I combined into one large dataset in the hopes of exploring this question further. 

## Data Collection

To collect this data, I created 5 different classes to create the 5 different datsets that I hoped to combine. I scraped and gathered <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/attendance.py">attendance data</a>, <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/payroll.py"> payroll data</a>, <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/season.py"> season data</a>, <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/stadium.py"> stadium data</a>, and <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/population.py"> population data</a> for each MLB team from 2003 until 2022. I used various python libraries such as pandas and BeautifulSoup to scrape and clean most of the data. 


## Attendance Data

The first step in my data collection process was to scrape and clean fan attendance data from espn. To collect this data I used the python package pandas with pd.read_html. I attempted to scrape this webiste using python's BeautfulSoup and requests, but the HTTP request was denied. 

I looped through each year (2003 - 2023) and scraped the attendance data for each MLB season. I then cleaned the data to ensure that the format of each of the elements would match the other datasets we will merge with later.

*** IMPORTANT NOTE ***

It is important to note that due to COVID-19, the MLB did not have any fan attendance for the year of 2020. 
It is also important to note that some of the teams have diffferent names for different websites, so I changed some of the team names to match better with those later on (i.e. Cleveland Indians = Cleveland Guardians)

<li class="masthead__menu-item">
    <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/attendance.py">Attendance Full Code</a>
</li>


## Payroll Data

The next step for the data collection involves grabbing the team payroll data for each year we wish to look at. I aslso used pd.read_html for this, as Beautiful had struggles. I used information from thebaseballcube to gather this data. 

I scraped this data for each year in a very similar way to the previous data, editing the year of the url I grabbed the data from. I then cleaned the data by selecting the team, year, and payroll column from the scraped and combined information. It is important to note that for this data as well changing the name of the teams is crucial for combining the data later. 

<li class="masthead__menu-item">
    <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/payroll.py">Payroll Full Code</a>
</li>


## Stadium Data

Next, I gathered data for each of the MLB stadiums and their total capacity. To do this I used python's BeautifulSoup to scrape data off of ballparksofbaseball.com. I gathered data from past and present ballparks in order to accurately combine this information with the others gathered. 

For this data, the website I scraped did not contain a dataset, and instead just had a collection of ballparks with various information. This meant that the scraping process was a little trickier to grab all of the information that I needed. Cleaning the data was also not so simple. I used several regular expressions to extract the important pieces of information to create my final and complete stadium dataset. 

Additionally, each of the ballparks on the main page of the website contain links to a new webpage with information specific to that ballpark. This means that for each of the ballparks, a new BeautifulSoup object has to be created and the new webpage scraped, as shown in the code below. 

<li class="masthead__menu-item">
    <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/stadium.py">Stadium Full Code</a>
</li>


## Season Data

The next step in the data collection process is to scrape the complete MLB season data and outcomes from 2003 through 2023. To do this I used baseball-reference and pd.read_html. Since baseball-reference is a smaller website, BeautifulSoup had several issues scraping this data. Also, be mindful of how many requests you send to the website itself when collecting the data as it is not equipped to handle too many requests from one location. 





