#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:08:07 2022

@author: craigrupp
"""
# Extract the Data
# =============================================================================
# Extract the data of the page using BeautifulSoup and CSS Selectors.
# 
# [Line #14] Extract the first title using the built-in function of the BeautifulSoup. Convert the result to a string and assign it to the variable soup_data.
# [Line #15] Extract the all div tags of the class which name is box using CSS Selectors. Assign the result to the variable css_data.
# [Lines #18-19] Print variables soup_data and css_data
# =============================================================================


# Import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/final.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Extract the data
soup_data = soup.title.get_text()
css_data = soup.select("div.box")

# Print variables
print(soup_data)
print(css_data)



# =============================================================================
# Your goal here is to go through all div blocks class of box in the HTML file and write them to the DataFrame:
# 
#  Assign the empty dictionary to the variable building_dict.
#  In the loop, extract the h4 tag of the div tag and convert it to the string. Assign the result to the variable building_title.
#  In the loop, extract the ul tags of the div tag and convert them to the string. Assign the result to the variable building_info.
#  Save building_info to the dictionary building_dict using as the key the variable building_title.
#  Convert the dictionary to the DataFrame with the parameter orient equal to 'index'. Assign the result to the variable df.
# =============================================================================

# This is my modified take in making each column (which held all details) into their own dataframe and concating them together while setting their index

import pandas as pd

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/final.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Select all div tags class of box
div_tags = soup.select("div.box")
print(div_tags)

# Define the dictionary
building_dict= {}

# Go thought all divs
for div in div_tags:
    # Get the h4 and other data on the page
    title = div.h4.get_text()
    items = div.ul.get_text()

    # Save the data in the dictionary
    building_dict[title] = items

# Convert dictionary to the DataFrame
df_1 = pd.DataFrame.from_dict(building_dict, orient='index')
print(df_1)
df_2 = df_1.copy()
print(type(df_1.loc['Sydney Opera House', :]))

test_1 = df_1.loc['Sydney Opera House', :]
print(test_1)



def findKeys(x):
    print(type(x))
    single_df = {}
    for name, val in x.iteritems():
        data = val.split("\n")
        for item in data:
            if item != '':
                sep = item.find(':')
                key = item[:sep]
                value = item[sep + 2:]
                single_df[key] = [value]
    return pd.DataFrame(single_df)




# Test individual row of scraped dataframe
print(findKeys(df_1.loc['Sydney Opera House', :]))
dfmut_1, dfmut_2, dfmut_3, dfmut_4, dfmut_5 = findKeys(df_1.loc['Sydney Opera House', :]), findKeys(df_1.loc['Empire State Building', :]), findKeys(df_1.loc['Taj Mahal', :]),findKeys(df_1.loc['Hagia Sophia', :]), findKeys(df_1.loc['Eiffel Tower', :])

print(dfmut_1)
print(dfmut_2)
print(dfmut_3)
print(dfmut_4)
print(dfmut_5)

combined_mut = pd.concat([dfmut_1, dfmut_2, dfmut_3, dfmut_4, dfmut_5])
combined_mut.reset_index(inplace=True)
print(combined_mut)
combined_mut.set_index('Name', inplace=True)
combined_mut.drop(['index'], inplace=True, axis=1)
combined_mut



# Another stab at this from scratch
# Import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/final.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Select all div tags class of box
div_tags = soup.select("div.box")

# Define the dictionary
building_dict = {}

# Go thought all divs
for div in div_tags:
    # Get the h4 and other data on the page
    building_title = div.h4.get_text()
    building_info = div.ul.get_text()

    # Save the data in the dictionary
    building_dict[building_title] = building_info

# Convert dictionary to the DataFrame
df = pd.DataFrame.from_dict(building_dict, orient='index')
print(df)

# Display the max amount of columns
pd.set_option('display.max_columns', None)

# Separate the text on page by columns
print(df[0].str.split(r"\n", expand=True)) 


# Use Similar logic above but need singular call to assign rows and not individual calls
df_cf_test = df.copy()
print(df_cf_test)

def updateRow(x):
    # Create default dataframe used later for stacking
    new_df = pd.DataFrame({'Name':['1'], 'Country':['1'], 'City':['1'], 'Architectural style':['1']})
    # Iterate over (column name, Series) pairs.
    for name, val in x.iteritems():
        # Empty object to fill with Key/Value pairs above in same mold as template dataframe above
        stack_obj = {}
        # Existing data (all in one column) is separated by a new line, split on this to iterate over
        data = val.split("\n")
        # Loop over new list containing each key/value pair now in one string (A few empty lines so conditionally catch those)
        for item in data:
            if item != '':
                sep = item.find(':')
                key = item[:sep]
                value = item[sep + 2:]
                # Must add singular value in a list to create DataFrame below (Declaring new Columns for Row)
                stack_obj[key] = [value]
        # Created Dictionary with each series values (multi line string in {df} var rows singular column initially into individual keys which will transform into a dataframe next)
        rows_df = pd.DataFrame(stack_obj)
        # Stack new dataframe from looped over data that created columns on each iteration on top of default dataframe
        new_df = pd.concat([new_df, rows_df])
    # Modfiy dataframe to remove default row (w/iloc after initially resetting), 
    # then set index to name column and drop the index column (along the column and not default row axis)
    new_df = new_df.reset_index().iloc[1:, :].set_index('Name').drop('index', axis=1)
    return new_df


# Test single row with function
print(updateRow(df_cf_test.loc['Sydney Opera House', :]))

# Pass web Scraped DF to updateRow function to clean up dataframe initially created Soup UL scraping
for label, content in df_cf_test.items():
    print(updateRow(content))












