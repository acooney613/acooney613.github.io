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

As a fan of the major league baseball team the Oakland Athletics, I have seen and heard all of the news surrounding the pending move to Las Vegas. Some argue that the lack of fan support lead to the teams inevitable move while others argue that it is poor ownership. It is no secret that lately the Oakland athletics seem to be spending next to nothing on player personnel. This got me thinking, what sorts of factors have an influence on overall fan attendance? 

Through this blog post, I will show you a potential first step in answering this question. I will go through my data collection process, and in a later post will go through some analysis of the data gathered. 

This post will contain 6 different sections, 5 of which involve scraping several websites to gather the data, and 1 to combine each of the 5 datasets into one complete one. 

## Attendance Data

The first step in my data collection process was to scrape and clean fan attendance data from espn. To collect this data I used the python package pandas with pd.read_html. I attempted to scrape this webiste using python's BeautfulSoup and requests, but the HTTP request was denied. 

I looped through each year (2003 - 2023) and scraped the attendance data for each MLB season. I then cleaned the data to ensure that the format of each of the elements would match the other datasets we will merge with later.

*** IMPORTANT NOTE ***

It is important to note that due to COVID-19, the MLB did not have any fan attendance for the year of 2020. 
It is also important to note that some of the teams have diffferent names for different websites, so I changed some of the team names to match better with those later on (i.e. Cleveland Indians = Cleveland Guardians)

In this dropdown below is the full code I used to gather the MLB attendance data:

<details>
<summary style = 'color: blue;'> 
Full Code and Class Implementation 
</summary>

<div markdown="1">

```python
---
# required python packages
import pandas as pd
import datetime

# I used a class to implement but it is not required
class attendance():
    def __init__(self, base_url):
        # create the global variables for the url and our final dataframe
        self.base_url = base_url
        self.data = pd.DataFrame()

    def get_data(self):
        # gather the data
        self.gather()
        # create a dummy column for the 2020 attendance data to be used later
        self.data['2020'] = -1

        # rotate the data 
        self.data = self.data.melt(id_vars = 'TEAM', 
                                   value_vars = ['2023', '2022', '2021', '2020', '2019', '2018', '2017',
                                                 '2016', '2015', '2014', '2013', '2012',
                                                  '2011', '2010', '2009', '2008', '2007', '2006',
                                                   '2005', '2004', '2003' ],
                                    value_name = 'average attendance',
                                    var_name = 'year')
        # remove any missing values
        self.data = self.data.dropna()
        # replace all for the year 2020 with empty value
        self.data = self.data.replace(-1, pd.NA)
        # write to a csv 
        self.data.to_csv('DATA/attendance.csv', index = False)
        # return the data
        return self.data


    def collect(self, url, year):
        table = pd.read_html(url)
        df = table[0]
        df.columns = df.iloc[0]
        df = df.iloc[1:].reset_index(drop = True)
        df = df[[f'{year} Attendance', 'Home']]
        df.columns = df.iloc[0]
        df = df.iloc[1:].reset_index(drop = True)
        df = df.rename(columns = {'AVG' : f'{year}' })
        
        df = df[['TEAM', f'{year}']]
        df['TEAM'] = df['TEAM'].str.replace('Florida', 'Miami')
        df['TEAM'] = df['TEAM'].str.replace('Anaheim', 'LA Angels')

        if self.data.empty:
            self.data = df
        else:
            self.data = pd.merge(self.data, df, on = 'TEAM', how = 'outer').rename_axis(None).reset_index(drop = True)

    def gather(self):
        # grab the current year which is where we will start from
        dt = datetime.date.today()
        year = dt.year

        # start our while loop and end when we reach 2002
        while year > 2002:
            # this code skips over the year 2020
            if year == 2020:
                year -= 1
            # collect the attendance data for the current year
            if year == dt.year:
                self.collect(self.base_url, year)
                year -= 1
            # edit url and to grab the data from the new year
            else:
                extend = f'/_/year/{year}'
                self.collect(self.base_url + extend, year)
                year -= 1

# call our class using the appropriate url
y = attendance('https://www.espn.com/mlb/attendance')
# initiate data collection
df_attendance = y.get_data()
---
```
</div>
</details>


## Payroll Data

The next step for the data collection involves grabbing the team payroll data for each year we wish to look at. I aslso used pd.read_html for this, as Beautiful had struggles. I used information from thebaseballcube to gather this data. 

I scraped this data for each year in a very similar way to the previous data, editing the year of the url I grabbed the data from. I then cleaned the data by selecting the team, year, and payroll column from the scraped and combined information. It is important to note that for this data as well changing the name of the teams is crucial for combining the data later. 

In the dropdown below is my full code and class implementation for the payroll dataset. 

<details>
<summary style = 'color: blue;'> 
Full Code and Class Implementation 
</summary>

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

## Stadium Data

Next, I gathered data for each of the MLB stadiums and their total capacity. To do this I used python's BeautifulSoup to scrape data off of ballparksofbaseball.com. I gathered data from past and present ballparks in order to accurately combine this information with the others gathered. 

For this data, the website I scraped did not contain a dataset, and instead just had a collection of ballparks with various information. This meant that the scraping process was a little trickier to grab all of the information that I needed. Cleaning the data was also not so simple. I used several regular expressions to extract the important pieces of information to create my final and complete stadium dataset. 

Additionally, each of the ballparks on the main page of the website contain links to a new webpage with information specific to that ballpark. This means that for each of the ballparks, a new BeautifulSoup object has to be created and the new webpage scraped, as shown in the code below. 

In the dropdown below is my full code and class implementation for the stadium data:

<details>
<summary style = 'color: blue;'> 
Full Code and Class Implementation 
</summary>

<div markdown="1">

```python
---
# python packages required for scraping this data
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# dictionary with states and their abbreviations
STATES = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
        'ON': 'Canada',
        'PQ': 'Canada'
    }

# class implementation 
class stadiums():
    def __init__(self, url_1, url_2, url_3):
        # create empty dataframe with the column titles we want
        self.data = pd.DataFrame(columns = ['team', 'location', 'stadium', 'capacity', 'opened', 'closed'])
        self.url_1 = url_1
        self.url_2 = url_2
        self.url_3 = url_3
    
    def get_data(self):
        # gather the data for each of the urls
        self.stadium_data(self.url_1)
        self.stadium_data(self.url_2)
        self.past_stadium(self.url_3)
        # clean the data we have gathered
        self.clean()
        return self.data

    # scrapes the past stadium data
    def past_stadium(self, url):
        # create our BeautifulSoup object
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # find all stadium items we need to look at
        ballparks = soup.find_all('a', class_ = 'stadium-item', href = True)

        # loop each ballpark found above
        for ballpark in ballparks:
            # grab name of the ballpark
            name = ballpark.find('div', class_ = 'title').text
            # grab location of ballpark
            location = ballpark.find('div', class_ = 'city').text.strip()
            # create request and BeautifulSoup object for this ballpark using href link
            tmp_r = requests.get(ballpark['href'])
            tmp_soup = BeautifulSoup(tmp_r.text, 'html.parser')
            # grab information from html
            info = tmp_soup.find_all('div', class_ = 'facts-col')
            tmp = ''
            # create complete string with all the information found above
            for x in info:
                tmp = tmp + x.find('p').text + '\n'
            
            # use regular expression to select team name from string
            team = re.search(r'(?:Tenant|Tenants):\s*(.*?)\n', tmp).group(1)
            # use regular expression to select stadium capacity
            capacity = re.search(r'Capacity:\s*(.*?)\n', tmp).group(1)
            # use regular expression to select year opened
            opened = re.search(r'(?:Opened|Opening):\s*(.*?)\n', tmp).group(1)
            # use regular expression to select year closed 
            closed = re.search(r'Closed:\s*(.*?)\n', tmp)

            # RFK STADIUM is the Washington Nationals Stadium, and while opened before 2005, wasn't used by the team until then
            if name == 'RFK STADIUM':
                opened = ', 2005'
            
            # past stadiums must have a closed date, so if none is found we create one
            if closed == None:
                # find the stadium that replaced it 
                closed = self.data[self.data['location'] == location]['opened'].to_string()
                closed = re.search(r',\s*(.*?)(?:,|\s*\(|$)', closed).group(1)
                closed = int(closed) - 1
                closed = f'{closed}'

                
            else:
                # create the closed variable that was found
                closed = closed.group(1)
                closed = re.search(r',\s*(.*?)(?:,|\s*\(|$)', closed).group(1)
            
            # only add stadiums in our desired time interval
            if int(closed) >= 2003:
                # create a row to be appended to the data
                row = {'team' : team, 'location' : location, 'stadium' : name, 'capacity' : capacity, 'opened' : opened, 'closed' : closed}
                self.data = pd.concat([self.data, pd.DataFrame(data = row, index = [len(self.data) + 1])], ignore_index = True)
            tmp_r.close()
        r.close()


        
    def stadium_data(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        ballparks = soup.find_all('a', class_ = 'stadium-item', href = True)

        for ballpark in ballparks:
            name = ballpark.find('div', class_ = 'title').text
            location = ballpark.find('div', class_ = 'city').text.strip()
            tmp_r = requests.get(ballpark['href'])
            tmp_soup = BeautifulSoup(tmp_r.text, 'html.parser')
            info = tmp_soup.find('div', class_ = 'facts-col')
            info = info.find('p').text
            team = re.search(r'-(?:Tenant|Tenants):\s*(.*?)\n', info).group(1)
            capacity = re.search(r'-Capacity:\s*(.*?)\n', info).group(1)
            opened = re.search(r'-(?:Opened|Opening):\s*(.*?)\n', info).group(1)

            row = {'team' : team, 'location' : location, 'stadium' : name, 'capacity' : capacity, 'opened' : opened, 'closed' : '-'}
            self.data = pd.concat([self.data, pd.DataFrame(data = row, index = [len(self.data) + 1])], ignore_index = True)
            tmp_r.close()
        r.close()
    
    def clean(self):
        data = self.data
        data[['team']] = data['team'].str.extract(r'\s*(.*?)(?:,|\(|$)')
        data['team'] = data['team'].str.strip()
        data['team'] = data['team'].str.replace('Florida', 'Miami')
        data['team'] = data['team'].str.replace('Indians', 'Guardians')
        data['location'] = data['location'].str.strip()
        data['capacity'] = data['capacity'].str.replace(',', '')
        data['capacity'] = data['capacity'].str.extract(r'(\d+)').astype('int')
        data[['city']] = data['location'].str.extract(r'(.*?)(?:,)')
        data['city'] = data['city'].replace(['Bronx', 'Queens', 'Flushing'], 'New York City')
        data[['state']] = data['location'].str.extract(r',\s*(\w+)')
        data[['opened']] = data['opened'].str.extract(r',\s*(.*?)(?:,|\s*\(|$)')
        data[['city']] = data['city'].str.extract(r'(.*?)(?:\s*City|$)')
        data['state'] = data['state'].map(STATES)
        data['location'] = data['city'] + ', ' + data['state']
        self.data = data[['team', 'location', 'stadium', 'capacity', 'opened', 'closed']].dropna().reset_index(drop = True)

z = stadiums('https://www.ballparksofbaseball.com/american-league/', 'https://www.ballparksofbaseball.com/national-league/', 
            'https://www.ballparksofbaseball.com/past-ballparks/')
df_stadium = z.get_data()
df_stadium.to_csv('DATA/stadiums.csv', index = False)

       
---
```
</div>
</details>
