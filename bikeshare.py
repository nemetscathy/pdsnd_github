import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: need to update this to be able to offer the user another chance to input values if an invalid value is entered
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city would you like to see statistics for?  Please type in one of the following city names: chicago, new york city, washington.\n').lower()
        if city.lower() == 'chicago':
            break
        elif city.lower() == 'new york city':
            break
        elif city.lower() == 'washington':
            break
        else:
            print('\nSince you have entered an invalid value, we will default chicago.\n')
            city = 'chicago'
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to see statistics for?  Type in the following month names or type the word all for all months: all, january, february, ... , june.\n').lower()
        if month.lower() == 'all':
            break
        elif month.lower() == 'january':
            break
        elif month.lower() == 'february':
            break
        elif month.lower() == 'march':
            break
        elif month.lower() == 'april':
            break
        elif month.lower() == 'may':
            break
        elif month.lower() == 'june':
            break
        else:
            print('\nSince you have entered an invalid value, we will default january.\n')
            month = 'january'
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day of the week would you like to see statistics for?  Type in one of the following weekdays or type the word all for every weekday: all, monday, tuesday, ... sunday.\n').lower()
        if day.lower() == 'all':
            break
        elif day.lower() == 'monday':
            break
        elif day.lower() == 'tuesday':
            break
        elif day.lower() == 'wednesday':
            break
        elif day.lower() == 'thursday':
            break
        elif day.lower() == 'friday':
            break
        elif day.lower() == 'saturday':
            break
        elif day.lower() == 'sunday':
            break
        else:
            print('\nSince you have entered an invalid value, we will default monday.\n')
            day = 'monday'
            break

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] =  pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most common start month:', popular_month)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most common start day of the week:', popular_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:',  popular_hour)
    """Added the ability to display the most popular start time month, day of week, and hour in the code above."""
    print("\nThis took %s seconds." % round((time.time() - start_time),5))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used Start Station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used End Station:', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_startend_station = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('Most commonly used Start and End Station:', popular_startend_station)
    """Added the ability to display the most popular start and end stations.  Took 2 columns and brought them together into a combined value using plus symbols."""
    print("\nThis took %s seconds." % round((time.time() - start_time),5))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    """Added the ability to display the total time of all travel (every trip) and the mean of the trips."""
    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    total_travel_time = (df['End Time'] - df['Start Time']).sum()
    print('Total travel time:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = (df['End Time'] - df['Start Time']).mean()
    print('Mean of travel time:', mean_travel_time)
    print("\nThis took %s seconds." % round((time.time() - start_time),5))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of the user types: \n', user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_of_sex = df['Gender'].value_counts()
        print('\nCount of each sex of the user: \n', count_of_sex)
        """Displaying the user's statistics such as the User Type and User Sex in the code above for cities that are not washington."""
    # TO DO: Display earliest, most recent, and most common year of birth
        min_birth_year = (df['Birth Year']).min()
        print('\nEarliest birth year of users:', int(min_birth_year))
        max_birth_year = (df['Birth Year']).max()
        print('\nMost recent birth year of users:', int(max_birth_year))
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common user birth year:', int(common_birth_year))
        """Added the ability to display the oldest, youngest, and most common birth year in the code above for cities that are not washington."""
    else:
        print('\nNo statistics in washington for Sex or Birth Year.\n')

    print("\nThis took %s seconds." % round((time.time() - start_time),5))
    print('-'*40)



def display_raw_data(df):
    """Function to request if the user wants to view the raw data 5 rows at at time."""
    beginning_row = 0
    ending_row = 5
    max_rows = df.count().max()
    while ending_row < max_rows:
        ask_input_5_rows = input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n')
        if ask_input_5_rows.lower() == 'yes':
            print((df[beginning_row:ending_row]).to_string(index=False, header=False))
            beginning_row += 5
            ending_row += 5
        else:
            print("\n")
            break
    else:
        ending_row = max_rows
        print("\nNo more rows of raw data.\n")


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
    # TO DO: marking this part of the script to remember to try an elegant way to determine if users have entered an invalid entry by mistake and request another chance at an input instead of ending the script
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
