"""
BikeShare - Python project to explore US BikeShare data.
The program allows the user to view statistics on bike share usage between three cities:
Chicago, New York City, and Washington, DC.

This script requires the following packages to be installed: pandas and numpy.

Using Python version 3.6.3
Submitted by: Mustafa YOULDASH, Ph.D.

Version:
    v1.0.2.

Last Updated:
    March 28, 2023 at 03:21:00 Arabic EST.

Usage:
    python bikeshare.py
"""

# Imports
import time
import pandas as pd
import numpy as np


# Set the file names and location for the data files
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Args:
        None.

    Returns:
        (str) city - name of the city to analyze.
        (str) month - name of the month to filter by, or "all" to apply no month filter.
        (str) day - name of the day of week to filter by, or "all" to apply no day filter.
    """
    print('Hello! Let\'s explore some US BikeShare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        
        # Convert the input to lowercase
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        
        # Is city in the CITY_DATA dictionary?
        if city in CITY_DATA:
            break     
            
        else: # We have an invalid input
            print("Invalid input. Please enter either Chicago, New York City, or Washington.")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        
        # Convert the input to lowercase
        month = input("Which month? January, February, March, April, May, June, or 'all' if you don't want to filter by month?\n").lower()
        
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
            
        else: # We have an invalid input
            print("Invalid input. Please enter a valid month name or 'all'.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        
        # Convert the input to lowercase
        day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or 'all' if you don't want to filter by day?\n").lower()
        
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
            
        else: # We have an invalid input
            print("Invalid input. Please enter a valid day name or 'all'.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze.
        (str) month - name of the month to filter by, or "all" to apply no month filter.
        (str) day - name of the day of week to filter by, or "all" to apply no day filter.
    
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day.
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # Read the start time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Read month, day of week, and hour data from the data frame
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # While month isn't 'all', specify the month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    # Last check: day must not be 'all'
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    # Return the data frame
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        df (DataFrame): The BikeShare data as a pandas DataFrame.
        
    Returns:
        None.
    
    This function takes in a BikeShare data DataFrame and uses it to calculate and print out the most frequent times
    of travel for the user. It displays the most common month, day of the week, and start hour of travel, based on
    the data provided. If any of the parameters are not found in the data, the function will simply print out that
    the data is not available.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", common_start_station)

    # TO DO: display the most common day of week
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", common_end_station)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        df (DataFrame): The BikeShare data as a pandas DataFrame.
        
    Returns:
        None.
    
    This function takes in a BikeShare data DataFrame and uses it to calculate and print out statistics on the most
    popular start and end stations, as well as the most frequent combination of start and end stations. It displays
    the total number of trips that started and ended at each station, as well as the total number of trips that
    included each station as a part of their journey. If any of the data is not available, the function will print
    out that the data is not available.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Concatenate the Start and End Station str values
    df['Start and End Station'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['Start and End Station'].mode()[0]
    print('The most common trip:', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        df (DataFrame): The BikeShare data as a pandas DataFrame.
        
    Returns:
        None.
    
    This function takes in a BikeShare data DataFrame and uses it to calculate and print out statistics on the total
    and average trip duration. It displays the total travel time, the average travel time, and the longest and
    shortest trips taken, based on the data provided. If any of the data is not available, the function will simply
    print out that the data is not available.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time: float
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time: float
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean (i.e., average) travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on BikeShare users.
    
    Args:
        df (DataFrame): The BikeShare data as a pandas DataFrame.
        
    Returns:
        None.
    
    This function takes in a BikeShare data DataFrame and uses it to calculate and print out statistics on BikeShare
    users. It displays the counts of each user type (e.g., subscriber, customer), as well as the counts of each
    gender, if applicable. It also displays the earliest, most recent, and most common birth year of users, if that
    information is available in the DataFrame. If any of the data is not available, the function will print out that
    the data is not available.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    
    # Use enumerate to log the user types data
    for i, user_type in enumerate(user_types):
        print(f"{user_types.index[i]}: {user_type}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:\n{}\n'.format(gender_counts.to_string()))
        
    else: # Data not available.
        print('Gender data is not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_years = df['Birth Year']
        earliest_year = int(birth_years.min())
        most_recent_year = int(birth_years.max())
        most_common_year = int(birth_years.mode()[0])
        
        # Log the earliest, most recent, and most common year of birth from the data frame
        print('Birth year stats:')
        print('The earliest year: {}'.format(earliest_year))
        print('The most recent year: {}'.format(most_recent_year))
        print('The most common year: {}'.format(most_common_year))
        
    else:
        print('Birth year data not available for this city!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """
    Displays raw data from a Pandas DataFrame in an interactive manner, prompting the user for input.
        
    Args:
        df (DataFrame): The BikeShare data as a pandas DataFrame.

    Returns:
        None.

    This function prompts the user to specify whether they want to see raw BikeShare data or not. If the user enters
    "yes", the function displays the first five rows of the DataFrame, then prompts the user again to ask if they
    want to see five more rows. This process continues until the user enters "no". If the user enters "no" at the
    first prompt, the function simply returns and does not display any data.
    """
    idx = 0 # Increment counter
    pd.set_option('display.max_columns', 200)

    while True:
        raw = input("\nWould you like to view the raw data? Enter 'yes' or 'no'.\n").lower()
            
        if raw == 'no':
            break
            
        elif raw == 'yes':
            print(df[idx: idx+5])
            idx += 5
            
            if idx >= len(df):
                print("End of data reached.")
                break
                
        else:')
            print("Invalid input. Please enter either a 'yes', or a 'no'.")


def run_analysis():
    """
    Function added for refactoring purposes.
    
    This way, the code inside the while loop is grouped together in a single function,
    making it easier to understand and modify.
    The loop now simply calls the run_analysis() function repeatedly until the user decides to quit.
    
    Added:
        March 28, 2023.
    """
    city, month, day = get_filters()
    df = load_data(city, month, day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

    # Added function to display raw data
    display_raw_data(df)


def main():
    """
    Runs the BikeShare analysis program.

    Args:
        None.

    Returns:
        None.

    This function is the entry point for the BikeShare analysis program. It first loads the BikeShare data from CSV files
    for a specific city selected by the user. It then prompts the user to specify what type of statistics they would
    like to see (e.g., time statistics, station statistics, user statistics). Once the user has made their selection, the
    corresponding analysis function is called and the relevant statistics are displayed to the user. The user can then
    choose to see more data or exit the program.
    """
    
    # Loop until the user decides not to restart the program for additional interactivity
    while True:
        
        # Function added for refactoring purposes
        run_analysis()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    """
    In a nutshell, the if __name__ == "__main__": statement in bikeshare.py is used to define the main entry point for the script,
    which in turn calls the main() function to coordinate the execution of the other functions and generate output for the user.
    """
	main()
