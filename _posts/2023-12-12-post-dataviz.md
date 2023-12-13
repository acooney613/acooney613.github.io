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

I then created level variables for the different postseason categories so I could look at the teams that made it farther than others. To do this I used:

```python
---
numbering = {'World Series' : 4, 'NLCS' : 3, 'ALCS' : 3, 'ALDS' : 2, 'NLDS' : 2, 'NLWC' : 1, 'ALWC' : 1, 'Missed Postseason' : 0}
df['code'] = df['series'].map(numbering)
---
```

## Exploration

The first thing I decided to look at when exploring the data was a correlation matrix between the numeric variables in and attendance. I wanted to see if there were some variables that would be more interesting to explore before I dove in. 

<img src = '/assets/images/heatmap.png'>

Looking at the heatmap, we can see that both payroll and wins are correlated the same with proportion of stadium capacity filled. They both have a fairly strong positive correlation with this fan attendance metric. 
