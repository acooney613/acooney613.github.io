---
layout: post
title: Contributing Factors for MLB Fan Attendance (Data Collection and Cleaning)
author: Aidan Cooney
description: How to scrape and clean several datasets to explore contributing factors to MLB fan attendance 
image: "/assets/images/baseball.png"
markdown: kramdown
kramdown:
  parse_block_html: true
---

## Introduction

Major League Baseball (MLB) is one of the four major U.S. sports, and has recently been experiencing a decline in popularity. Attendance numbers appear to be dropping at rapid rates across the league news spreads of the MLB's sudden loss of popularity to sports like basketbal and football. Teams like the Oakland Athletics who appear to be experiencing extremely low fan attendance numbers have looked at moving locations to areas where a new fanbase could be created to increase attendance numbers. 

With the MLB experiencing this decline, I decided to look into some potential factors that contribute to fan attendance for any given team. I gathered and scraped data from 2003 to 2022 in my attempt to dive into this issue further. Through this blog post I will demonstrate the code that I used to create my dataset, and in my next post I will dive into my analysis of the data collected.

In total I created and combined 5 seperate datasets. I created a payroll, an attendance, a season, a stadium, and a population dataset in order to get all the information I felt would be most useful in exploring this topic. I used python's pandas and BeautifulSoup to collect and clean the data. I gathered data from multiple different webistes and location as we will explore below. For each of the datasets described below I have linked both the CSV file created from my python code as well as the full code I used to scrape and clean that dataset.

## Data Collection

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/attendance.csv">attendance</a> data that I collected contains columns for team, year, and average attendance. The average attendance is the teams average home attendance for the year specified. 
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/attendance.py">attendance code</a>

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/payroll.csv">payroll</a> data that I collected contains columns for team, year, and payroll. The payroll is the amount of money spent on players for the year specified. 
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/payroll.py">payroll code</a>

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/season.csv">season</a> data that I collected contains columns for team, wins, losses, win-loss percentage, year, farthest series made in the postseason, and the result of the final series they made. If a team did not make the postseason, I specified by inserting "Missed Postseason" into the series column.
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/season.py">season code</a>

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/stadium.csv">stadium</a> data that I collected contains columns for team, location of the stadium, name of the stadium, the total fan capacity of the stadium, the year the stadium opened, and the year the stadium closed (if any). 
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/stadiums.py"> stadiums code</a>

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/population.csv">population</a> data that I collected contains columns for location, year, and the population of that area for the given year. 
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/population.py">population code</a>

