# Weather Checking Application

import argparse
import requests
import time
import json

# WeatherAPI URL
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"

# Path to the favorites file
FAVORITES_FILE_PATH = "favorites.json"

# Sample favorite cities data 
favorite_cities = []


def load_favorites():
    # Load favorite cities from the favorites file.
    try:
        with open(FAVORITES_FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_favorites():
    # Save favorite cities to the favorites file.
    with open(FAVORITES_FILE_PATH, "w") as file:
        json.dump(favorite_cities, file)


def get_weather(city, api_key):
    # Fetch weather data for a given city.
    params = {"key": api_key, "q": city}
    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data for {city}. Status code: {response.status_code}")
        print("Response content:")
        print(response.text)
        return None



def add_favorite(city):
    # Add a city to the list of favorites.
    if city not in favorite_cities:
        favorite_cities.append(city)
        save_favorites()
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in your favorites.")


def view_favorites():
    # View the list of favorite cities.
    print("Your favorite cities:")
    if favorite_cities:
        for city in favorite_cities:
            print(f"- {city}")
    else:
        print("No favorite cities yet.")


def update_favorite(old_city, new_city):
    # Update a favorite city.
    if old_city in favorite_cities:
        favorite_cities.remove(old_city)
        favorite_cities.append(new_city)
        save_favorites()
        print(f"{old_city} updated to {new_city} in your favorites.")
    else:
        print(f"{old_city} not found in your favorites.")


def delete_favorite(city):
    # Delete a city from the list of favorites.
    if city in favorite_cities:
        favorite_cities.remove(city)
        save_favorites()
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} not found in your favorites.")


def update_favorites_file():
    """Update the favorites file with the latest data."""


def auto_refresh(api_key, interval):
    # Enable auto-refresh of weather data.
    print(f"Auto-refresh enabled. Refreshing every {interval} seconds.")
    while True:
        for city in favorite_cities:
            weather_data = get_weather(city, api_key)
            if weather_data:
                print(f"Weather in {city}: {weather_data['current']['condition']['text']}")
        time.sleep(interval)


def main():
    global favorite_cities
    favorite_cities = load_favorites()

    parser = argparse.ArgumentParser(description="Weather Checking Application")

    parser.add_argument("city", nargs="?", default=None, help="Check weather for a specific city")
    parser.add_argument("--apikey", required=True, help="WeatherAPI key")
    parser.add_argument("--add", help="Add a city to your favorite list")
    parser.add_argument("--favorites", action="store_true", help="View your favorite cities")
    parser.add_argument("--update", nargs=2, help="Update a city in your favorites (old_city new_city)")
    parser.add_argument("--remove", help="Delete a city from your favorites")
    parser.add_argument("--auto-refresh", type=int, help="Enable auto-refresh with the specified interval in seconds")

    args = parser.parse_args()

    if args.city:
        weather_data = get_weather(args.city, args.apikey)
        if weather_data:
            print(f"Weather in {args.city}: {weather_data['current']['condition']['text']}")

    elif args.add:
        add_favorite(args.add)

    elif args.favorites:
        view_favorites()

    elif args.update:
        update_favorite(args.update[0], args.update[1])

    elif args.remove:
        delete_favorite(args.remove)

    elif args.auto_refresh:
        auto_refresh(args.apikey, args.auto_refresh)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
