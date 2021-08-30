import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }
city = '' #Creating global city variable
month = '' #Creating global month variable
day = '' #Creating global day variable

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york, washington). HINT: while loop used to handle invalid inputs
    while True:
        global city; # in order to change value of a global variable
        city = str(input('Would you like to see data for Chicago, New York, or Washington?\n').title())
        if city not in ('Chicago','New York','Washington'):
           print('This is invalid input!')
        else:
            break
        
    # Get user input for month (all, january, february, ... , june)
    while True:
        global month; # in order to change value of a global variable 
        month = str(input('Which month you want to filter by? January, February, March, April, May, June? or \'all\' to apply no month filter.\n').title())
        if month not in ('January', 'February', 'March', 'April', 'May', 'June','All'):
            print('This is invalid input!')
        else:
            break
      
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        global day; #in order to change value of a global variable
        day = str(input('Which day you want to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday? or \'all\' to apply no day filter.\n').title())
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print('This is invalid input!')
        else:
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
    df = pd.read_csv(CITY_DATA[city]) #create DataFrame for the file's data

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
         
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
          
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('What is the most popular month for travelling?\n', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('What is the most popular day for travelling?\n', common_day)

    # display the most common start hour
    common_hour = df['Start Time'].mode()[0]
    print('What is the most popular hour of the day to start your travels?\n', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    
    print('Below are the most popular start and end station respectivly.\nStart Station: {}\nEnd Station: {}\n'.format(common_start_station, common_end_station))
    
    # display most frequent combination of start station and end station trip
    comb_start_end_station = (df['Start Station']+ df['End Station']).mode()[0]
    print('What was the most popular trip from start to end?\n', comb_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('\nThe total travel time:\n', total) 
    
    # display mean travel time
    average = df['Trip Duration'].mean()
    print('\nThe average travel time:\n', average) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df['User Type'].value_counts()
    print('What is the breakdown of users?\n', count_user)
    
    # Display counts of gender
    if city == 'Washington':
        print('\nNo gender data to share\n')
    else:
        count_gender = df['Gender'].value_counts()
        print('\nWhat is the breakdown of gender?\n', count_gender)

    # Display earliest, most recent, and most common year of birth
    if city == 'Washington':
        print('\nNo birth year data to share\n')
    else:
        earliest = df['Birth Year'].min() #earlist year of birth
        print('\nWhat is the earliest year of birth?\n', earliest)
        
        recent = df['Birth Year'].max()   #most recent year of birth
        print('\nWhat is the most recent year of birth?\n', recent)
        
        common_year = df['Birth Year'].mode()[0]  #common year of birth
        print('\nWhat is the most common year of birth?\n', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    '''Display 5 row data '''
    while True:
        #take an input from the user.
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter \'yes\' or \'no\'\n').lower()
        #handling invalid input.
        if view_data not in ('yes', 'no'):  
            print('This is invalid input!')
        else:
            break
    start_loc = 0
    while (view_data != 'no'):
        #print only 5 rows of row data.
        print(df.iloc[start_loc:(start_loc + 5 )]) 
        start_loc += 5
        
        #ask again to view another 5 rows.
        while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter \'yes\' or \'no\'\n').lower()
            #handling invalid input.
            if view_data not in ('yes', 'no'):  
                print('This is invalid input!')
            else:
                break
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)          
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
