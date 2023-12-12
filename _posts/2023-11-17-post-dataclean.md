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

## Background

As a fan of the major league baseball team the Oakland Athletics, I have seen and heard all of the news surrounding the pending move of the team to Las Vegas. The Oakland Athletics first moved to Oakland in 1968 and have been there ever since. With the rumors of the move, I wondered what potential causes of this move could be. I have heard rumors that a lack of fans is a major reason for the move, and decided I wanted to explore that further. I wanted to know what factors would contribute to overall fan attendance to see what the potential root of the "lack of fan support" could be.  

I gathered and scraped several different websites and created 5 seperate datasets that I combined into one large dataset in the hopes of exploring this question further. 

## Data Collection

To collect this data, I created 5 different classes to create the 5 different datsets that I hoped to combine. I scraped and gathered attendance, payroll, season, <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/stadium.py"> stadium data</a>, and <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/population.py"> population data</a> data for each MLB team from 2003 until 2022. I used various python libraries such as pandas and BeautifulSoup to scrape and clean most of the data. 

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

