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

Major League Baseball (MLB) is one of the four major U.S. sports, and has recently been experiencing a decline in popularity. Attendance numbers appear to be dropping at rapid rates across the league news spreads of the MLB's sudden loss of popularity to sports like basketball and football. Teams like the Oakland Athletics who appear to be experiencing extremely low fan attendance numbers have looked at moving locations to areas where a new fan base could be created to increase attendance numbers. 

With the MLB experiencing this decline, I decided to look into some potential factors that contribute to fan attendance for any given team. I gathered and scraped data from 2003 to 2022 in my attempt to dive into this issue further. Through this blog post I will demonstrate the code that I used to create my dataset, and in my next post I will dive into my analysis of the data collected.

In total I created and combined 5 separate datasets. I created a payroll, an attendance, a season, a stadium, and a population dataset in order to get all the information I felt would be most useful in exploring this topic. I used python's pandas and BeautifulSoup to collect and clean the data. I gathered data from multiple different websites and locations as we will explore below. For each of the datasets described below I have linked both the CSV file created from my python code as well as the full code I used to scrape and clean that dataset.

## Data Collection

When thinking about answering the question of what factors affect fan attendance the most, I landed on several key variables that I felt could be useful in my exploration. 

I first wanted to make sure that I had team attendance numbers for all of the years I was going to be looking at. I used espn to gather the data I needed for this.

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/attendance.csv" target = "_blank">attendance</a> data that I collected contains columns for team, year, and average attendance. The average attendance is the team's average home attendance for the year specified.
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/attendance.py" target = "_blank">attendance code</a>

Next I wanted to get the teams player payroll data so that I could look at how much teams are spending on players for any given season.

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/payroll.csv" target = "_blank">payroll</a> data that I collected contains columns for team, year, and payroll. The payroll is the amount of money spent on players for the year specified.
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/payroll.py" target = "_blank">payroll code</a>

I then wanted to get the information from the MLB season itself to see if a teams potential success in the current year and years previous had any sort of influence on the fan attendance. 

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/season.csv" target = "_blank">season</a> data that I collected contains columns for team, wins, losses, win-loss percentage, year, farthest series made in the postseason, and the result of the final series they made. If a team did not make the postseason, I specified by inserting "Missed Postseason" into the series column.
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/season.py" target = "_blank">season code</a>

Next I wanted to find the stadium data for each of the MLB teams for the year I was looking at so that I could figure out how many people they allowed in for games to fairly compare across teams. 

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/stadium.csv" target = "_blank">stadium</a> data that I collected contains columns for team, location of the stadium, name of the stadium, the total fan capacity of the stadium, the year the stadium opened, and the year the stadium closed (if any). 
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/stadiums.py" target = "_blank"> stadiums code</a>

Finally I wanted to look at the population data of a team's location to see if the surrounding population size had any effect on the fan attendance.

The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/DATA/population.csv" target = "_blank">population</a> data that I collected contains columns for location, year, and the population of that area for the given year. 
Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/population.py" target = "_blank">population code</a>

## Combining The Data

Once I scraped and cleaned all of the data for each subsection, I combined them all into one larger dataset with all of the information I felt was most relevant. The <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/mlb_attendance.csv" target = "_blank"> MLB Attendance</a> dataset that I created contains columns for team, year, average home attendance, stadium name, location of the stadium, fan capacity for the stadium, population of the surrounding area, payroll for that season, team's wins for that season, team's losses for that season, win-loss percentage for that season, final series made that season, and the result of the final series they made. 

While combining the data it is important to note that some factors such as team name and location had to be modified in the previous datasets in order to make a merge of the datasets possible. It is also important to note that for the year 2020 there are no MLB attendance numbers due to COVID-19, so the attendance numbers for that year should be blank. 

Full Code: <a href="https://github.com/acooney613/stat386-mlb_attendance/blob/main/combine.py" target = "_blank"> combination code</a>

## Conclusion

While this dataset may not be perfect, I believe it is a good start at exploring some potential contributing factors for attendance numbers across the league. In a future blog post I will discuss some of the potential findings in the data along with key graphics to display some of the relationships that may exist with the variables that I have chosen to look at. If you truly enjoyed this topic I encourage you to try some on your own, and update and change the dataset to perform your own exploration of baseball or any topic of your choice! Below is the link to my full repo if you would like to look at my full project!

<a href="https://github.com/acooney613/stat386-mlb_attendance/tree/main" target = "_blank"> FULL REPO</a>