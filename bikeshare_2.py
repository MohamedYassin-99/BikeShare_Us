import time
import pandas as pd
##import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("\nwhich city would you like to choose? new york city or chicago or washington\n")
        if city not in ('chicago','new york city','washington'):
            print("This city is not valid, please try again")
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("\nwhich month would you like to choose? january or february or March or April or May or June or all ?\n")
        if month not in ("january","february","March","April","May","June","all"):
            print("This month is not found in the data please try again ")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("\nWhich day would you like to choose? Sunday or Monday or Tuesday or Wednesday or Thursday or Friday or Saturday or all ?\n")
        if day not in ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","all"):
            print("Invalid Data please try again ")
            continue
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
##### extract month from the dataset and create new column
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    ####filter the month
    if month !="all":
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
        df=df[df['month']== month]
    ####filter the day_name
    if day !="all":
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print(" The most common month",common_month )

    # display the most common day of week
    common_day=df['day'].mode()[0]
    print(" The most common day",common_day )

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print(" The most common hour",common_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start staton :",Start_Station)

    # display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print("The most commonly used End staton :",End_Station)


    # display most frequent combination of start station and end station trip
    Combination_Station=df.groupby(['Start Station','End Station']).count()
    print("Most frequent combination of start station and end station trip",Combination_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time per seconds
    Total_Travel_Time=  sum(df['Trip Duration'])
    print('Total travel time :',Total_Travel_Time/86400,"Days")

    # display mean travel time
    Mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time",Mean_travel_time/60,"Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts()
    print("User Types:\n",user_types)

    # Display counts of gender
    try:
        type_gender=df['Gender'].value_counts()
        print('\ngender Types:\n',type_gender)
    except KeyError:
        print("\nGender Types: \nNo data available for this month")

    # Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
