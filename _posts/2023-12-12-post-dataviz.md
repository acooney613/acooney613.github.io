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

If you have not checked out my previous post <a href="https://acooney613.github.io/2023/12/10/post-dataclean.html" target = "_blank">Contributing Factors for MLB Fan Attendance (Data Collection and Cleaning) </a> I encourage you to take a look as it explains the motivation behind using this data and dives into the collection and cleaning process that I used for the dataset we will explore below. 

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
df['postseason'] = df['series'].map(numbering)

# variable to give the end result of the season
df['series_result'] = df['result'] + ' ' + df['series']
df['series_result'] = df['series_result'].fillna('missed postseason')

# make variable to indicate if they made postseason
df['made postseason'] = np.where(df['series'] != 'Missed Postseason', 'Yes', 'No')
---
```

## Exploration

### Initial Exploration

Before I dove fully into my data, I decided to use a correlation matrix to see if there were any relationships between the variables that I wanted to explore more. I created a heatmap (as shown below) of the correlation values for each of the relationships. 

<div align = 'center'>
<img src = '/assets/images/heatmap.png'>
</div>

The largest correlation value if between wins and postseason, which makes sense given that in order to make the postseason a team has to win more games, so the relationship should be extremely positive and correlated.

The top two correlation values, other than wins and postseason, are both 0.45 and show that there is potentially positive correlation between fan attendance and both wins and payroll. Postseason also has a fairly positive correlation with fan attendance with a value of 0.37. Postseason is a variable which describes how far a team got in the postseason (i.e. lost ALCS). In this blog post I will explore some of the relationships found in the heatmap above. 

### Playoff Success and Fan Attendance

After getting the values from the correlation matrix I wanted to take a deeper dive into postseason success and various factors that may be contributing to a teams overall success. I first made a barchart between the end of season result and the overall fan attendance as shown below. 

The first thing I wanted to explore was the potential relationship between fan attendance numbers and a teams overall success measured by their postseason run. Looking at the image below we can see that, on average, teams that make the posteason filled more of their stadium than teams that missed the postseason. One of the largest bars belonged to teams that would go on to win the world series, while the second smallest bar belonged to teams that missed the playoffs entirely. 

<div align = 'center'>
<img src = '/assets/images/result.png'>
</div>

Looking at the image above we can see that, on average, teams that make the posteason filled more of their stadium than teams that missed the postseason. One of the largest bars belonged to teams that would go on to win the world series, while the second smallest bar belonged to teams that missed the playoffs entirely. This relationship does look consistent with what we found in the correlation matrix above as we received a correlation coefficient value of 0.37 meaning that teams that make it farther in the playoffs also tend to have higher fan attendance. This relationship could potentially show the importance of fan attendance numbers for a team looking at making a deeper playoff run, and speaks to the 'homefield advantage' that most teams strive for. 

I dove deeper into this thought of fan attendance and decided to create a barchart using the World Series resultss from 2012 to 2022 (excluding 2020 as there is no attendance data) to see if there was a common trend.

<div align = 'center'>
<img src = '/assets/images/winner.png'>
</div>

Looking at this plot we can see that, on average, the team that ended up winning the world series had a larger average fan attendance for the season than the teams that ended up losing the world series. The two largest gaps in this data come in the years 2014 and 2016, where the winners clearly had a much higher fan attendance rate than the loser. In years such as 2013, 2017, and 2019 however, the losing team had a larger fan attendance proportion than the winner. Overall this plot appears to agree with the correlation matrix in saying that teams that have greater fan attendance also tend to do better in the postseason than teams with less fan attendance. 


### Playoff Success and Player Payroll
Is fan attendance the only metric for postseason success however? To answer this question I looked at the relationship between postseason success and team payroll. Looking at the plot below we can see that on average the teams that missed the postseason entirely spent far less on players than the teams that made the playoffs. 

<div align = 'center'>
<img src = '/assets/images/barchart.png'>
</div>

The bar for world series won contains one of the higher values once again and the smallest bar belongs to teams that missed the postseason entirely. This is fairly consistent with the relationship found in the heatmap since both show there is a positive relationship between payroll and postseason success.  

### Factors Contributing to Fan Attendance

The final piece I will explore in this blog is the effects of wins and payroll on fan attendance. The correlation matrix showed that these two variables had the strongest relationships with fan attendance, so in the plots below we will explore this idea further. 

Looking first at a scatterplot for fan attendance by win-loss percentage, we can see that there does appear to be a fairly positive trend in the data.

<div align = 'center'>
<img src = '/assets/images/proportion.png'>
</div>

As the win-loss variable increases, the total proportion of stadium filled also increases on average. The trend line in the center displays this relationship as it contains a positive slope, showing an increase in y (stadium filled) with an increase in x (win-loss). This is consistent with the correlation matrix, as both show a positive correlation between win-loss percentage and proportion of fan attendance. 

Looking next at a scatterplot for log of team payroll and proportion of stadium filled colored by whether or not a team made the postseason. The overall plot shows a fairly positive trend for both teams that made the postseason and teams that did not.

<div align = 'center'>
<img src = '/assets/images/postseason.png'>
</div>

The plot shows that, on average, teams that made the postseason tended to have higher stadium attendance for the same payroll value compared to teams that did not make the postseason. This is consistent with the previous findings, as teams we found earlier that teams that do better tend to also have a greater fan attendance. 

Finally, I took a look at a team's win-loss percentage by the team's payroll to see if there was actually a relationship between the two.
<div align = 'center'>
<img src = '/assets/images/wins_payroll.png'>
</div>

The plot above shows that there is a potential positive linear relationship between a team's payroll and their record. As the payroll value goes up, a team's record also tends to increase. This is also consistent with the correlation value found in the heatmap earlier in the blog, which returned 0.34 as the correlation coefficient between these variables. 

## Conclusion

Using the plots above I was able to learn more about the data I gathered and some potential relationships that may exist within the numbers. I learned that a team's postseason success may be influenced by their fan attendance and a team's payroll and season's wins may be related to the number of fans they have on average. It is important to understand that this anaylsis is limited by the data that was collected. There are potentially other variables and metrics that could be used to explore the data further, and I encourage you to test out whatever you can find!

Feel free to use the data that I have collected and gathered in my other blog post (<a href="https://acooney613.github.io/2023/12/10/post-dataclean.html" target = "_blank">link here</a>) and do your own exploratory anaylsis! 

Here is the link to my <a href="https://github.com/acooney613/stat386-mlb_attendance" target = "_blank">full repo</a>, as well as the link to the file I performed my eda in (<a href = 'https://github.com/acooney613/stat386-mlb_attendance/blob/main/EDA.py' target = "_blank">link here</a>) 