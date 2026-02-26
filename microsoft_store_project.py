# -*- coding: utf-8 -*-

project_name = "Microsoft_Store_Project"

!pip install jovian --upgrade -q

import jovian

jovian.commit(project=project_name)

"""## Data Preparation and Cleaning

First of all, let's import numpy, pandas, matplotlib and seaborn libraries.
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""We also include the special command `%matplotlib inline` to ensure that plots are shown and embedded within the Jupyter notebook itself, because sometimes plots may show up in pop-up windows without this command.

So, now we can upload our data set using pandas.
"""

data = pd.read_csv("msft.csv")

"""Using the function info() we can check, how many rows and columns in our data set are and also the name of every column."""

data.info()

"""As we can see, our data set contains 5321 rows and 6 columns. Let us see the content of our data.

"""

data

"""As we saw above, we have 5321 rows which is non-null. But when we take a look on our data, there are altogether 5322 rows and the last one is filled with no values `NaN`, which means, it doesn't give us any information about any app in Windows Store, so we can deleate it using drop operation."""

data = data.drop(5321)

data

"""Now, we've got 5321 apps in our data set. So let's take a look on prices. As we can see, there is apps for free and also all prices in strings and in Indian rupee. To make it easier to work with Prices, we should concatinate those prices in integers. But first of all, let's find out, what is the last value of non cost app using modul display and tail."""

from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(data[data.Price == 'Free'].tail())

"""So we see, the last row with value of price 'Free' is 5162. Let's replace 'Free' with value 0 and all prices concatinate in integers and transer in euro for more visibility (multiply by 0.0116)."""

Price_list = []
for i in data.loc[data.Price != 'Free', 'Price']:
    Price_list.append(round(float(i[2:])*0.0116, 2))

data.loc[data.Price != 'Free', 'Price'] = np.array(Price_list)

data.loc[data.Price == 'Free', 'Price'] = 0

data

"""The last thing what we can do, we rename 'No of people Rated' with 'No_of_people_Rated', so it will easier to work with it."""

data = data.rename(columns={'No of people Rated':'No_of_people_Rated'})

"""Now, if we go up again see information about our data, we see that only 2 of columns were detected as a numeric columns. But since we concatinated Price into integer,even though there is one more column which has numeric values. To make our analysis easier, let's convert it into numeric data types and view some basic statistics about the numeric columns."""

data['Price'] = pd.to_numeric(data.Price, errors = 'coerce')

data.describe()

import jovian

jovian.commit()

"""## Exploratory Analysis and Visualization

Now data set is ready for analysing. Lets see, what is the most amount of downloaded apps gropping by category in this data set and plot it using barplot.
"""

most_popular_category = data.Category.value_counts()
most_popular_category

sns.set_style("darkgrid")

plt.figure(figsize=(12, 6))
plt.title('Which category is the most popular for download?')
plt.xticks(rotation = 75)
sns.barplot(most_popular_category.index, most_popular_category);

"""Here we can see, that the most of apps in this data set are from category 'Music'."""

Prices = data.groupby('Category')['Price'].sum()
Prices

plt.figure(figsize=(12,6))
plt.title('Which category has the most highest price?')
Prices.plot(kind = "pie", autopct = lambda p: '{:.1f}%'.format(round(p)) if p > 0 else None);

"""Since we have only 3 categories, which has a price, we have in our pie chart Books with 29%, Business with 32% and the most expensive - Developer Tools with 39%, which is also not suprised.

Now lets find out, in which year was the most highest amount of downloads.
"""

data['year'] = pd.DatetimeIndex(data.Date).year
data['month'] = pd.DatetimeIndex(data.Date).month
data['day'] = pd.DatetimeIndex(data.Date).day
data['weekday'] = pd.DatetimeIndex(data.Date).weekday

downloaded_apps_in_year = data.groupby('year')['No_of_people_Rated'].sum()

downloaded_apps_in_year

plt.figure(figsize=(12, 8))

plt.xlabel('Years')
plt.ylabel('Downloaded apps in this year')
plt.title("In which year were the most downloads from Windows Store?")
plt.plot(downloaded_apps_in_year.index, downloaded_apps_in_year, 'r-o');
plt.xticks(downloaded_apps_in_year.index);

"""Here we can see the development of downloads from Windows Store. It seems from 2010 it's getting higher and reach the pick of downloads in 2016 with over 500000 downloads, and then go down and got a little more than 100000 downloads in 2020.

And finaly, lets see, on which day people are downloading apps the most.
"""

downloads_weekday = data.groupby('weekday')['No_of_people_Rated'].sum()

downloads_weekday

plt.figure(figsize = (12, 8))
plt.title("On which weekday do the most downloads take place?")
sns.barplot(downloads_weekday.index, downloads_weekday);

"""It seems the most popular day for apps downloading is Monday. And Tuesday, Wednesday, Thursday and Friday has almost the same amount of downloads. And looks like weekends are not the day for downloading apps. I guess, a lot of people are spending more time going outside and meeting friends or dooing any other activities and hobbies, which is pretty nice."""

import jovian

jovian.commit()

"""## Asking and Answering Questions

So now, lets analyze our dataset by asking some questions.

### Q1: What is the most popular/unpopular app in the Windows Store?

If we gonna sort the data only by 'Rating', it doesn't give us an exakt answer for this qestion, because they're can be a lot of apps which were reted with 5 stars. And we sort it only by 'No_of_people_Rated', it doesn't give us an exakt answer too, because there can also a lot of apps, which were downloaded a lot of times, but rated as only 3 stars for example or even less.

So the perfect way to answer this question is sort the data both by 'Rating' and 'No_of_people_Rated'. And we don't have to forget to put 'Rating' on the first place, so it's going to be sorting at first by 'Rating' and then by 'No_of_people_Rated'.

Lets see 20 the most popular and 20 the most unpopular apps in Windows Store.
"""

best_apps = data.sort_values(['Rating', 'No_of_people_Rated'], ascending = False).head(20)

best_apps

worst_apps = best_apps = data.sort_values(['Rating', 'No_of_people_Rated'], ascending = False).tail(20)

worst_apps

"""As we can see, the most popular app is some app from social category called ILN and the worst are MapWorks Essentials and Model Railroad Manager with rating 1 star and only 108 downloads.

### Q2: Which 10 apps are the most expensive?

We have two posibilities to explore it, using only `data.sort_values` by itself and also `data.groupby` and `data.sort_value`using together. I'm going to show both of them to see the difference between these 2 methods.

As first, lets do it using `data.sort_values`. Using this method, our dataset is sorted by price, but we also can see other information about apps, like what is Rating of it, which Category is this app belong and all other columns.
"""

expensive_apps = data.sort_values("Price", ascending = False).head(10)

expensive_apps

"""Now we will use the second method. Here we can group it by every column which we want. For example for a good visibility, I'll group it by name of app and price. And here we can clearly see every price of app. And as expected, it shows 10 the most expensive apps."""

data.groupby('Name')[['Price']].sum().sort_values(['Price'], ascending = False).head(10)

"""### Q3: In which year, weekday, month and day was the most downloads in Windows Store?

We can do it using `data.groupby` and `sort.values` again.
"""

data.groupby(['year', 'weekday', 'month', 'day'])[['No_of_people_Rated']].sum().sort_values(['No_of_people_Rated'],ascending = False)

"""So looks like on 30th of January 2018, which is Tuesday, was happend the most downloads from Windows Store.

But lets see the downloads single in year, weekday, month and day as well.
"""

data.groupby(['year'])[['No_of_people_Rated']].sum().sort_values(['No_of_people_Rated'], ascending = False)

data.groupby(['weekday'])[['No_of_people_Rated']].sum().sort_values(['No_of_people_Rated'], ascending = False)

data.groupby(['month'])[['No_of_people_Rated']].sum().sort_values(['No_of_people_Rated'], ascending = False)

data.groupby(['day'])[['No_of_people_Rated']].sum().sort_values(['No_of_people_Rated'], ascending = False)

"""Obvious the most popular year for downloads was 2016, most popular weekday is Monday, most popular month is October and as we see, the most popular day for downloads is 30th of month.

### Q4: What is the most popular category of apps people downloading?

Lets group it by Category und summarize all number of rated people.
"""

data.groupby(['Category'])[['No_of_people_Rated']].sum().sort_values(['No_of_people_Rated'], ascending = False)

"""It seems people downloading a lof music from Windows Store. And if we count now how many times every category appears in our dataset, we will seeth at music is really the the most popular category which appears in our dataset 753 times."""

data.Category.value_counts()

"""### Q5: How many people have downloaded the apps in total?
### How many people have downloaded the apps on average per day?

To answer this question, we can just use simple functions `mean` and `sum`.
"""

in_total = data.No_of_people_Rated.sum()

in_total

on_average_per_day = in_total/(len(data.year.unique())*365)

on_average_per_day

"""We see, from year 2010 till today, from Windows Store it was in total more than 2.9 Million downloads, which means 731 downloads per day."""

import jovian

jovian.commit()

"""## Inferences and Conclusion
In this project, we could see and analyze Windows Store from year 2010 until nowadays. So once again, let us summarize all plots together.
"""

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Use the axes for plotting
axes[0,0].set_title('Which category is the most popular for download?')
sns.barplot(most_popular_category.index, most_popular_category,ax=axes[0,0]);
plt.setp(axes[0,0].xaxis.get_majorticklabels(), rotation=75)

#axes[0,0].set_xticks(rotation = 75)


# Pass the axes into seaborn
axes[0,1].set_title('Which category has the most highest price?')
Prices.plot(kind = "pie", autopct = lambda p: '{:.1f}%'.format(round(p)) if p > 0 else None, ax=axes[0,1]);



# Use the axes for plotting
axes[1,0].set_title("In which year were the most downloads from Windows Store?")
axes[1,0].set_xlabel('Years')
axes[1,0].set_ylabel('Downloaded apps in this year')
axes[1,0].plot(downloaded_apps_in_year.index, downloaded_apps_in_year, 'r-o');
axes[1,0].set_xticks(downloaded_apps_in_year.index)



# Pass the axes into seaborn
axes[1,1].set_title("On which weekday do the most downloads take place?")
sns.barplot(downloads_weekday.index, downloads_weekday, ax=axes[1,1]);


plt.tight_layout(pad=2);

"""From this dataset, we could learn, what is the most downloaded category, which of category is the most expensive, in which year took place the most downloaded, and also on which weekday people prefer to download apps from Windows Store and we could see how many people are downloading apps per day."""

import jovian

jovian.commit()

"""## References and Future Work

While I was working on the project, following links were very helpful. Hopefully, it helps you too.
- Lectures from course 'Data Analysis with Python: Zero to Pandas': https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas
- Asking questions on the forum: https://jovian.ml/forum/c/data-analysis-with-python-zero-to-pandas/course-project/58
- Looking for answers here: https://stackoverflow.com/
- Pandas official homepage: https://pandas.pydata.org/pandas-docs/stable/reference/io.html
- Matplotlib official homepage: https://matplotlib.org/index.html

Windows Dataset were taken from [kagle](https://www.kaggle.com/).

A huge thanks to Aakash from [Jovian.ml](https://jovian.ml/) for this amazing course and giving a lot of new knowledge in data analysis, and also thanks to [FreeCodeCamp](https://www.freecodecamp.org/) for providing your online [YouTbe platform](https://www.youtube.com/freecodecamp).
"""

import jovian

jovian.commit()