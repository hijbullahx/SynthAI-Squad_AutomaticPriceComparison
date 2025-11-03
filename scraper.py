import time
import pandas as pd

def get_service_data(service_type, location):
    """
    Simulates scraping data for a given service and location.

    In a real hackathon, this function would use Requests and BeautifulSoup
    to fetch and parse live web pages.

    For reliability, we are using "mock" (fake) data.
    """

    print(f"--- Simulating a web scrape for '{service_type}' in '{location}' ---")

    time.sleep(1.5) 

    # --- MOCK DATA ---
    # This is the data we are "pretending" to scrape.
    # It's a list of dictionaries, which is easy to turn into a table.
    mock_data_list = [
        {
            "service_name": "Dhaka Cleaners Pro",
            "price": "৳3,500 (Basic)",
            "rating": "4.8/5",
            "review_summary": "Amazing service! My apartment is spotless. Very professional and on time."
        },
        {
            "service_name": "Quick Home Fix",
            "price": "৳2,800 (Standard)",
            "rating": "4.2/5",
            "review_summary": "Good value for the price, but they were a bit late. The job was done well."
        },
        {
            "service_name": "Sparkle Services BD",
            "price": "৳4,000 (Premium)",
            "rating": "4.5/5",
            "review_summary": "A bit expensive, but the quality is top-notch. Recommended for deep cleaning."
        },
        {
            "service_name": "BD Home Repair",
            "price": "৳3,200 (Basic)",
            "rating": "3.9/5",
            "review_summary": "Average service. They missed a few spots and I had to call them back."
        }
    ]

    print("--- Simulation complete. Returning mock data. ---")
    return mock_data_list


"""
import requests
from bs4 import BeautifulSoup

def get_REAL_data(service_type, location):

    # 1. Define a URL (This is a FAKE example URL)
    # We would use 'service_type' and 'location' to build this URL
    url = f"https://fake-service-directory.com/search?service={service_type}&loc={location}"

    try:
        # 2. Fetch the webpage
        # We add headers to pretend we are a real browser
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=5)

        # Raise an error if the request (e.g., 404, 500)
        response.raise_for_status() 

        # 3. Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 4. Find the data
        # This is the hard part. You must "Inspect Element" in your browser
        # to find the correct HTML tags and classes (e.g., 'service-card', 'price-tag')

        results_list = []

        # Example: finding all 'div's with the class 'service-card'
        cards = soup.find_all('div', class_='service-card')

        for card in cards:
            # Find elements *inside* the card
            name = card.find('h3', class_='service-name').text.strip()
            price = card.find('span', class_='price').text.strip()
            rating = card.find('div', class_='rating').text.strip()
            review = card.find('p', class_='review').text.strip()

            results_list.append({
                "service_name": name,
                "price": price,
                "rating": rating,
                "review_summary": review
            })

        return results_list

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return [] # Return an empty list on failure
"""