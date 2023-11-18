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

As a fan of the major league baseball team the Oakland Athletics, I have seen and heard all of the controversy surrounding the pending move to Las Vegas. A lack of fan support and spending by the owners to get and keep players have been a major points of controversy. There have been public statements by ownership as well as reverse boycotts leading to the MLB approval of the move to Las Vegas. 

This got me thinking, does a team that spend more money on it's players tend to bring in more fans?

To answer this question I decided to put together a dataset from several different websites to see what I could discover.

To scrape this data I used python tools such as BeautifulSoup, requests, and pandas to scrape and clean the necessary data for this project. There are other python tools that could be helpful in the data cleaning and scraping process, and I encourage you to try what works best for you. 

## Payroll Data

The first step to create this data set was to scrape and clean data for each teams payroll. I chose to scrape payroll data from 2003 through 2022. Below I will demonstrate some sample code I used to scrape and clean the payroll data. I used information found on 'thebaseballcube' website for this project.

### Scraping the Data

Using the url I used pandas to grab this data, as it was just a simple table on the website. Since using pandas returns a list of the tables on the webpage, I selected the first one.

```python
---
import pandas as pd

# read the data using pandas
df = pd.read_html(url)

# grab the first dataset
df = df[0]
---
```

Now that we got the payroll data, we need to clearn it.

### Cleaning the Data

To clean this specific dataset is simple. 

The first row of this dataset should be the header instead. 

We also want to select the columns with the teams and the payroll information. 

Finally, we need to add a column for the year so that combining the data in the final steps is far easier.

```python
---
# this code chunk selects the current year, but year can be set to whatever year you want to look at
import datetime
day = datetime.date.today()
year = day.year

# this grabs the first and the fifth column from the dataset
df = df.iloc[:, [1, 5]]

# this renames the columns to be the information contained in the first row
df.columns = df.loc[0]

# this selects rows 1 to 30
df = df.loc[1:30]

# this creates the column year, and sets the value to be a string of year
df['year'] = f'{year}'
---
```

<details>
<summary> Full Code and Class Implementation </summary>

### Here is the full code 

```python
---
print('hello world')
---
```

</details>