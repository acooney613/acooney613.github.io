---
layout: post
title: Contributing Factors for MLB Fan Attendance (Data Visualization and Interpretation)
author: Aidan Cooney
description: Visualizing MLB Fan Attendance Data
image: "/assets/images/baseball.png"
markdown: kramdown
kramdown:
  parse_block_html: true
---

*** Important Note ***

If you have not checked out my previous post <a href="https://acooney613.github.io/2023/11/17/post-dataclean.html" target = "_blank">Contributing Factors for MLB Fan Attendance (Data Collection and Cleaning) </a> I encourage you to take a look as it explains the motivation behind using this data and dives into the collection and cleaning process that I used for the dataset we will explore below. 

## Introduction

As explained in my previous the previous post, I am looking at potential contributing factors for MLB fan attendance numbers from 2003 to 2022. The dataset that I created contains columns for information on player payroll, year, team, location, stadium's fan capacity, population of surrounding area, season wins, season losses, win-loss percentage, and season results. In this post we will explore some of these variables and see just what they may have to tell us about MLB fan attendance. 

## Before Exploration

Before I started diving into the data I decided to create several new columns to better explore this data. I created columns to tell me the proportion of the stadium that was filled on average for a given season, columns that indicated playoff appearances, as well as how far they made it in the playoffs. The code I used for this can be found below:

```python
---
# read in the data
df = pd.read_csv('mlb_attendance.csv')
# get proportion of stadium filled
df['proportion'] = df['average attendance'] / df['capacity']

# add the numbering and map to the series made in the series variable
numbering = {'World Series' : 4, 'NLCS' : 3, 'ALCS' : 3, 'ALDS' : 2, 'NLDS' : 2, 'NLWC' : 1, 'ALWC' : 1, 'Missed Postseason' : 0}
df['postseason_code'] = df['series'].map(numbering)

# variable for if they made the postseason or not
df['postseason'] = np.where(df['series'] != 'Missed Postseason', True, False)

# variable to give the end result of the season
df['series_result'] = df['result'] + ' ' + df['series']
df['series_result'] = df['series_result'].fillna('missed postseason')
---
```

## Exploration

The first thing I wanted to explore was the potential relationship between fan attendance numbers and a teams overall success measured by their postseason run. Looking at the image below we can see that, on average, teams that make the posteason filled more of their stadium than teams that missed the postseason. One of the largest bars belonged to teams that would go on to win the world series, while the second smallest bar belonged to teams that missed the playoffs entirely. 

<img src = '/assets/images/result.png'>

This relationship could potentially show the importance of fan attendance numbers for a team looking at making a deeper playoff run, and speaks to the 'homefield advantage' that most teams strive for. Is fan attendance the only metric for postseason success however?

To answer this question I looked at the relationship between postseason runs and a teams payroll. Looking at the plot below we can see that the teams that missed the postseason entirely spent far less on players on average than teams that made the playoffs. 

<img src = 'assets/images/barchart.png'>

The world series bar once again has one of the higher numbers, with the largest bar coming from the ALCS loser. With those missing the postseason having such a low payroll however, this chart does show that teams that spend more tend to also go a lot farther than teams that spend less. 