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

## Exploration

The first thing I decided to look at when exploring the data was a correlation matrix between the numeric variables in and attendance. I wanted to see if there were some variables that would be more interesting to explore before I dove in. 

<img src = '/assets/images/heatmap.png'>

Looking at the heatmap, we can see that both payroll and wins are correlated the same with proportion of stadium capacity filled. They both have a fairly strong positive correlation with this fan attendance metric. 
