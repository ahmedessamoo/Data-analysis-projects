import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def input_validation(usr_name, usr_type):  # Function to check user validation for user input & tupe

    while True:
        usr_read = input(usr_name)
        try:
            if usr_read in ['chicago', 'new york city', 'washington'] and usr_type == 1:
                break
            elif usr_read in['january', 'february', 'march', 'april', 'may', 'june', 'all'] and usr_type == 2:
                break
            elif usr_read in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] and usr_type == 3:
                break
            else:
                if usr_type == 1:
                    print("unfortunately it's invaild input : chicago, new york city ,washington only")
                if usr_type == 2:
                    print("unfortunately it's invaild input : january, february, march, april, may, june or all")
                if usr_type == 3:
                    print("unfortunately  invaild input : sunday, ... friday, saturday or all")
        except ValueError:
            print("unfortunately user input is invaild")
    return usr_read


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    city = input_validation('which Data you want  please choose here  : chicago  , new york city or washington?',1)
   # TO DO: get user input for month (all, january, february, ... , june)

    month = input_validation('Which month  Do you want  please choose here (all, january, ... june)?', 2)

   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input_validation('Which day do you want  please choose here ? (all, monday, tuesday, ... sunday)', 3)  
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
    print("please wait Data is lading...")
    df = pd.read_csv(CITY_DATA[city])  # convert City Data

    # coverting satart time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month.dayofweek& in addition to hour  ,from start
    df['month'] = df['Start Time'].dt.month  # extracting month.dayofweek&hour ,from start
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


  # months filtering
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # months filtering to create New Dataframe
        df = df[df['month'] == month]

    # day of week filtering
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    frequent_month = df['month'].mode()[0]

    print('the Most frequent Month is :', frequent_month)

    # TO DO: display the most common day of week
    frequent_day = df['day_of_week'].mode()[0]

    print('the Most frequent day in week is :', frequent_day)

    # TO DO: display the most common start hour
    frequent_start_hour = df['hour'].mode()[0]

    print('the Most frequent start hour  is :', frequent_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('The Most common start Station:', common_start_station)

   # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('the Most common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    field_grouping  =df.groupby(['Start Station','End Station'])
    common_combination_station = field_grouping.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', common_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('The Total traveling Time is :', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('The mean_travel_time is', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The user Types Stats are :"')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # TO DO: Display counts of gender
        print('the counts of Gender Stats:')
        print(df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print('stat of earliest, most recent, and most common year of birth are as following:\n')
        print('the birth year stats are:\n')
        most_common_birth_year = df['Birth year'].mode()[0]
        print('The most Common birth Year is :',  most_common_birth_year)
        most_recent_birth_year = df['Birth year'].max()
        print('The most recent birth Year is :',most_recent_birth_year)
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest  birth Year is',earliest_birth_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()