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

*** Important Note ***

When cleaning this data, in order to combine the data with the other data sets we will scrape shortly the names of some of the teams must be changed (i.e. Cleveland Guardians)

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

<div markdown="1">

```python
---
# class I used to get the payroll data
class payroll():
    def __init__(self, base_url):
        # get the base url, we will add the year later
        self.base_url = base_url

        # create an empty instance of the dataframe
        self.pay = pd.DataFrame(columns = ['Team Name', 'Team Payroll', 'year'])
    
    def get_data(self):
        # get the current year and subtract one to get previous years data (as that will most likely be updated)
        day = datetime.date.today()
        year = day.year - 1

        # call the function to scrape the data
        self.payroll(year)

        # rename the columns of our dataset
        self.pay.columns = ['team', 'payroll', 'year']

        # here are the teams that we have to rename in order to combine later
        self.pay['team'] = self.pay['team'].str.replace(' Devil', '')
        self.pay['team'] = self.pay['team'].str.replace('Los Angeles Angels of Anaheim', 'Los Angeles Angels')
        self.pay['team'] = self.pay['team'].str.replace('Anaheim Angels', 'Los Angeles Angels')
        self.pay['team'] = self.pay['team'].str.replace('Los Angeles Angels of Anaheim', 'Los Angeles Angels')
        self.pay['team'] = self.pay['team'].str.replace('Florida', 'Miami')
        self.pay['team'] = self.pay['team'].str.replace('Montreal Expos', 'Washington Nationals')
        self.pay['team'] = self.pay['team'].str.replace('Oakland Athletics', 'Oakland A’s')
        self.pay['team'] = self.pay['team'].str.replace('Indians', 'Guardians')

        # return the cleaned data
        return self.pay

    def payroll(self, year):
        # create our new url using the current year we are looking at
        url = self.base_url + f'{year}'

        # get the data
        df = pd.read_html(url)

        # select the first table
        pay = df[0]

        # grab columns 1 and 5
        pay = pay.iloc[:, [1, 5]]

        # renames the columns to be the first row
        pay.columns = pay.loc[0]

        # selects rows 1 through 30
        pay = pay.loc[1:30]

        # creates a year column and populates with a string of year
        pay['year'] = f'{year}'

        # add this years data to the data we have already collected 
        self.pay = pd.concat([self.pay, pay], ignore_index = True)

        # if the year we are currently looking at is 2003, we stop
        if year > 2003:
            self.payroll(year - 1)

# create a payroll variable
x = payroll('https://www.thebaseballcube.com/page.asp?PT=payroll_year&ID=')

# get the payroll data
df_payroll = x.get_data()
---
```
</div>
</details>