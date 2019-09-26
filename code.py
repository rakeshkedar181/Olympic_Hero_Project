                                            # Project Name :- Olympic Hero
    
# Task 1:- Data Loading
# Task Description:- Let's start with the simple task of loading the data and do a little bit of renaming.
#Importing header files

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)

# Task 2:- Summer or Winter
# Task Description:- Some Countries love Summer, some Winter. We think it has to do something with their Olympic performance.
#                    For this task we will try to figure out which olympic event does a country perform better in.
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')

data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])

better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)

# Task 3:- Top 10
# Task Description:- 
# So we figured out which is a better event for each country. Let's move on to finding out the best performing countries across all events
# In this task we will try to find
# 1) Which are the top 10 performing teams at summer event (with respect to total medals),   winter event and overall?
# 2) How many teams are present in all of the three lists above?
#Code starts here

top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(top_countries,season):
    country_list=[]
    top_countries = top_countries.nlargest(10,season)
    country_list = top_countries['Country_Name']
    return country_list

top_10_summer = list(top_ten(top_countries,'Total_Summer'))
top_10_winter = list(top_ten(top_countries,'Total_Winter'))
top_10 = list(top_ten(top_countries,'Total_Medals'))

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print(common)

# Task 4:-Plotting Top 10
# Task Description:- From the lists that you have created from the previous task, 
#                    let's plot the medal count of the top 10 countries for better visualisation\
# Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

# print(summer_df)
# print(winter_df)
print(top_df)

plt.plot(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xlabel('Country Name')
plt.ylabel('Total of medals in summer season')
plt.xticks(rotation=45)
plt.show()

plt.plot(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.xlabel('Country Name')
plt.ylabel('Total of medals in winter season')
plt.xticks(rotation=45)
plt.show()

plt.plot(top_df['Country_Name'],top_df['Total_Medals'])
plt.xlabel('Country Name')
plt.ylabel('Total of medals in summer season')
plt.xticks(rotation=45)
plt.show()

# Task 5 :  Top performing country(Gold)
# Task Description : Winning silver or bronze medals is a big achievement but winning gold is bigger.
# Using the above created dataframe subsets, in this task let's find out which country has had the best performance with respect to the ratio between gold medals won and total medals won.
# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print(summer_country_gold)
print(winter_country_gold)
print(top_country_gold)

# Task 6 :- Best in the world
# Task Description :- Winning Gold is great but is winning most gold equivalent to being the best overall perfomer? Let's find out.
#Code starts here

# dropping last row as it contains total of all values calculated vertically
data_1 = data.drop(data.tail(1).index)

# Taking weighted value 
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1

# finding max value 
most_points = max(data_1['Total_Points'])

# finding best country with the most points
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print(most_points)

print(best_country)

# Task 7 :- Plot for the best
# Task Description :- We know which country is best when it comes to winning the most points in Olympic Games. Let's plot the medal count to visualise their success better
# Code starts here

best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Tally')
plt.xticks(rotation=45)



