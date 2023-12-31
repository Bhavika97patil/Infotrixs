 Infotrixs
 
 Python Developer Intern
 
 Task 1

 # Weather Checking Application Documentation

 # Overview
 The Weather Checking Application is a command-line tool developed in Python to check weather information for specific cities, manage a list 
 of favorite cities, and enable auto-refresh of weather data.

 # Prerequisites
 •	Python 3.x installed.
 
 •	WeatherAPI key for authentication. You can obtain one by signing up at https://www.weatherapi.com
 
 •	My API Key is “f93b33c211e1494bb2180745230412”
 # Usage

 Command line arguments: 

 •	--apikey : Your WeatherAPI key for authentication.
 
 •	--add: Add a city to your list of favorite cities.
 
 •	--favorites: View your list of favorite cities.
 
 •	--update: Update the name of a city in your list of favorites.
 
 •	--remove: Remove a city from your list of favorite cities.
 
 •	--auto-refresh: Enable auto-refresh to get weather updates at specified intervals.
 
 •	[city]: Optional argument to check the weather for a specific city.

 # Commands

 Run the application using the following command:

 # Check Weather for a Specific City:
 
 python weather_app1.py --apikey your_actual_api_key NewYork

 # output:
 
 Weather in NewYork: Cloudy

 # Add a City to Favorites:

 python weather_app1.py --apikey your_actual_api_key --add London

# output:

London added to favorites.

# View Favorite Cities:

python weather_app1.py --apikey your_actual_api_key --favorites

# output:

Your favorite cities:
- London
- Paris
- Tokyo

# Update a Favorite City:

python weather_app1.py --apikey your_actual_api_key --update Paris Berlin

# output:

Paris updated to Berlin in your favorites.

# Remove a City from Favorites:

python weather_app1.py --apikey your_actual_api_key --remove Tokyo

# output:

Tokyo removed from favorites.

# Enable Auto-Refresh:

python weather_app1.py --apikey your_actual_api_key --auto-refresh 30

# output:

Auto-refresh enabled. Refreshing every 30 seconds.

# Note:

•	Make sure to replace your_actual_api_key with your actual WeatherAPI key.












 

 

 
