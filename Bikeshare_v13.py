# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:23:58 2018

@author: aguerrero
"""

import time
import pandas as pd
import numpy as np



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input ("Please, enter a city name to analyze. You can choose between: Chicago, New York City or Washington: ").lower()
    while city not in ("chicago", "new york city", "washington"):
        print("Oops! Look like you requested data for a city non available, please try again: ")
        city = input ("Please, enter a city name to analyze. You can choose between: Chicago, New York City, Washington: ").lower()
    else:
        print("You selected the city!", city)

    # get user input for month (all, january, february, ... , june)

    month = input("Now, please enter the month you want to analyze: January, February,... or all!: ").title()
    while month not in ("January", "February", "March", "April", "May", "June","All"): 
        print("Only the months from january until June are available!") 
        month = input("Now, please enter the month you want to analyze: January, February,... or all!: ").title()
    else:
        print("You selected the month!", month)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input ("please select the day of the week for your analysis!: ").title()
    while day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"):
        print("Ups, maybe you invented a new day of the week. Bikeshare hopes that this is a new rest-day.")
        day = input("please select the day o the week for your analysis!: ").title()
    else:
        print ("Now you have finished with your selection!", day)
    print('-'*40)
    
    return city, month, day
    
city_data = { "chicago": "chicago.csv",
             "new york city": "new_york_city.csv",
              "washington": "washington.csv" }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(city_data[city])
  
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    
    df['month'] = df['Start Time'].dt.strftime('%B')
    
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    
    if month != "All":
        df = df[df["month"] == month]

    if day != "All":
        df = df[df["day_of_week"] == day]
    
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    most_common_month = df["month"].mode()
    print("Most Frequent Month: ", most_common_month)

    # display the most common day of week

    most_common_day = df["day_of_week"].mode()
    print ("Most Frequent Day: ", most_common_day)
  
    # display the most common start hour

    df["hour"] = df["Start Time"].dt.hour
    most_common_hour = df["hour"].mode()
    print ("Most Frequent Hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df["Start Station"].mode()
    print("Most common Start Station: ", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df["End Station"].mode()
    print("Most common End Station: ", most_common_end_station)

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   
    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total Travel Time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean Trael Time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df["User Type"].value_counts()
    print(user_types)

    # Display counts of gender

    if city=='washington':
        print('Gender information for Washington is unavailable and can not be calculated')
    else:
        counts_of_gender = df["Gender"].value_counts()
        print(counts_of_gender)

    # Display earliest, most recent, and most common year of birth

    if city=='washington':
        print('Birthday information for Washington is unavailable and can not be calculated')
    else:
        earliest_year = df["Birth Year"].min()

        print("Earliest Year of Birth:", earliest_year)

        most_recent = df["Birth Year"].max()

        print("Most Recent Year of Birth:", most_recent)

        most_common_year = df["Birth Year"].mode()

        print("Most Common Year of Birth:", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df, city)
        
        data_request = input ("Do You want to display the first five rows of the database?").title()
        if data_request != "Yes":
            print("Thank you")
            
        else:
            print(df.head(6))
            data_request_2 = input ("Do You want to display five rows more?").title()
            
            num = 6
            count_by = 5
            rows = num
            while data_request_2 == "Yes":
            
                rows += count_by
                print(df.head(rows))
                data_request_2 = input ("Do You want to display five rows more?").title()
               
                
            else:
                print("Thank you")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":

	main()