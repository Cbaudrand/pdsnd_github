import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
			  'new york city': 'new_york_city.csv',
			  'washington': 'washington.csv' }

def get_filters():
	"""
	Asks user to specify a city, month, and day to analyze. User can enter the number or string name
	of the selected item, and it's not case sensitive.

	Returns:
		(str) city - name of the city to analyze
		(str) month - name of the month to filter by, or "all" to apply no month filter
		(str) day - name of the day of week to filter by, or "all" to apply no day filter
	"""
	
	#get user input for city
	#refactoring update 1
	print('Hello! Let\'s explore some US bikeshare data!')
	city = 'tet'
	while True: 
		city = input('Which city you wish to inspect?\n[1] Chicago\n[2] New Your City\n[3] Washington\n')
		city = city.lower()	
		#convert the possible numerical input to the city name string and break the loop
		if city == 'chicago' or city == '1':
			city = 'chicago'
			break
		elif city == 'new york city' or city == '2':
			city= 'new york city'
			break
		elif city == 'washington' or city == '3':
			city = 'washington'
			break
		else:
			print('Invalid choice! Type either the name or number of the city you wish to inspect!')

	# get user input for month
	while True: 
		month = input('Which month?\n[1] January\t\t[5] May\n[2] February\t\t[6] June\n[3] March\t\t[7] All\n[4] April\n')
		month = month.lower()	
		#convert the possible numerical input to the month name string and break the loop
		if month == 'january' or month == '1':
			month = 'january'
			break
		elif month == 'february' or month == '2':
			month= 'february'
			break
		elif month == 'march' or month == '3':
			month = 'march'
			break
		elif month == 'april' or month == '4':
			month = 'april'
			break
		elif month == 'may' or month == '5':
			month = 'may'
			break
		elif month == 'june' or month == '6':
			month = 'june'
			break
		elif month == 'all' or month == '7':
			month = 'all'
			break
		else:
			print('\nInvalid choice! Type either the name or number of the month you wish to inspect!\n')

	# get user input day of the week
	while True: 
		day = input('Which day?\n[1] Monday\n[2] Tuesday\n[3] Wednesday\n[4] Thursday\n[5] Friday\n[6] Saturday\n[7] Sunday\n[8] All\n')
		day = day.lower()	
		#convert the possible numerical input to the day name string and break the loop
		if day == 'monday' or day == '1':
			day = 'monday'
			break
		elif day == 'tuesday' or day == '2':
			day= 'tuesday'
			break
		elif day == 'wednesday' or day == '3':
			day = 'wednesday'
			break
		elif day == 'thursday' or day == '4':
			day = 'thursday'
			break
		elif day == 'friday' or day == '5':
			day = 'friday'
			break
		elif day == 'saturday' or day == '6':
			day = 'saturday'
			break
		elif day == 'sunday' or day == '7':
			day = 'sunday'
			break
		elif day == 'all' or day == '8':
			day = 'all'
			break
		else:
			print('\nInvalid choice! Type either the name or number of the day you wish to inspect!\n')

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
	
	#load city data into pandas dataframe and convert the Start Time column
	df = pd.read_csv(CITY_DATA[city])
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	
	#split day of the week and month from the Start Time column into their own columns
	df['month'] = df['Start Time'].dt.month
	df['day_of_week'] = df['Start Time'].dt.weekday_name	
	
	#If month filtering not "all"
	if month is not 'all':
			#use the index of the months list to get the corresponding int
		temp_months = ['january', 'february', 'march', 'april', 'may', 'june']
		month_num = temp_months.index(month) + 1
		df = df[df['month'] == month_num]
		
	#If weekday filtering not "all"
	if day is not 'all':
		#filter by day
		df = df[df['day_of_week'] == day.title()]
		
	return df


def time_stats(df):
	"""Displays statistics on the most frequent times of travel."""

	print('\nCalculating The Most Frequent Times of Travel...\n')
	start_time = time.time()

	# display the most common month
	top_month = df['month'].mode()[0]
	print('Most common month for travelling was: ', top_month)

	# display the most common day of week
	top_day = df['day_of_week'].mode()[0]
	print('Most common day of the week for travelling was: ', top_day)

	# display the most common start hour
	df['hour'] = df['Start Time'].dt.hour
	popular_hour = df['hour'].mode()[0]
	print('Most common travelling hour was: ', popular_hour)

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)


def station_stats(df):
	"""Displays statistics on the most popular stations and trip."""

	print('\nCalculating The Most Popular Stations and Trip...\n')
	start_time = time.time()

	# display most commonly used start station
	s_station = df['Start Station'].value_counts().idxmax()
	print('Travel most often started the: ', s_station, ' station.')

	# display most commonly used end station
	e_station = df['End Station'].value_counts().idxmax()
	print('\nTravel most often ended at the ', e_station, ' station.')

	# display most frequent combination of start station and end station trip
	trip = df.groupby(['Start Station', 'End Station']).count()
	print('\nThe most often travelled trip was between the ', s_station, ' and ', e_station, 'stations')

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)


def trip_duration_stats(df):
	"""Displays statistics on the total and average trip duration."""

	print('\nCalculating Trip Duration...\n')
	start_time = time.time()

	# display total travel time
	travel_time_sum = sum(df['Trip Duration'])
	print('Total travel time: ', int(travel_time_sum/86400), ' days, ', int((travel_time_sum % 86400)/3600), ' hours and ', int(((travel_time_sum % 86400) % 3600)/60), ' minutes.')

	# display mean travel time
	travel_mean = df['Trip Duration'].mean()
	print('The mean of selected travel times is: ', travel_mean/60, ' minutes.')

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)


def user_stats(df):
	"""Displays statistics on bikeshare users."""

	print('\nCalculating User Stats...\n')
	start_time = time.time()

	# Display counts of user types
	types = df['User Type'].value_counts()
	print('User Types and amounts:\n', types)

	# Display counts of gender
	try:
		genders = df['Gender'].value_counts()
		print('\nGender amounts:\n', genders)
	except KeyError:
		print("\nNo gender data found for this selection.")

	# Display earliest, most recent, and most common year of birth
	
	#earliest, converting to full years
	try:
		e_year = int(df['Birth Year'].min())
		print('\nEarliest year of birth among bike users: ', e_year)
	except KeyError:
		print("\nNo data available for this selection.")
	
	#recent, converting to full years
	try:
		r_year = int(df['Birth Year'].max())
		print('\nMost recent year of birth among bike users: ', r_year)
	except KeyError:
	  print("\nNo data available for this selection.")

	#most common, converting to full years
	try:
		c_year = int(df['Birth Year'].value_counts().idxmax())
		print('\nMost common year of birth among bike users: ', c_year)
	except KeyError:
		print("\nNo data available for this selection.")


	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)

def display_raw_data(df):
	"""Asks the user y/yes/n/no input and displays 5 rows of raw data from the filtered
	selection at a time until user inputs n/no."""
	i = 0
	
	while True:
		raw_data_prompt = input('Would you like to see 5 rows of raw data? (yes / no)')
		raw_data_prompt.lower()
		
		if raw_data_prompt == 'yes' or raw_data_prompt == 'y':
			loop_counter = 0
			while loop_counter < 5:
				print(df.iloc[i])
				print('\n')
				i += 1
				loop_counter += 1
		elif raw_data_prompt == 'no' or raw_data_prompt == 'n':
			break
		else:
			print('Invalid input!')

def main():
	while True:
		city, month, day = get_filters()
		df = load_data(city, month, day)
		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df)
		display_raw_data(df)
	 

		restart = input('\nWould you like to restart? Enter yes or no.\n')
		if restart.lower() != 'yes':
			break


if __name__ == "__main__":
	main()
