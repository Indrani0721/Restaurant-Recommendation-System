## Restaurant Recommendation System

## Overview:

This Python program is designed to provide restaurant recommendations based on user-input food preferences. It utilizes a data structure to store restaurant information and implements an algorithm that considers user preferences, ratings, and proximity to suggest relevant dining options.

## Table of contents :

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Setup instructions](#setup-instructions)
- [Project Structure](#Project-Struture)
- [Data Structure](#Data-Structure)
- [Implementation](#implementation)
- [Usage](#Usage)

## Features

- Personalized restaurant recommendations
- Search and filter restaurants based on cuisine, location, and ratings
- User reviews and ratings for restaurants

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites:
- [Python](https://www.python.org/) (version 3.12 or higher)
  
## Setup instructions 

After installation, opened cmd ->> entered python --version, to check if it is installed and up to date.
Later, using cmd, created two files :
1. restaurant_recommendation.py
2. test_recommendation.py

Created a file from cmd to VS code, using below commands:

C:\projectdirectory>type nul > restaurant_recommendation.py

C:\projectdirectory>type nul > test_recommendation.py

C:\projectdirectory>code .

## Project Structure:

->restaurant_recommendation.py - In this file
->test_recommendation.py
->README

## Data Structure:

The main data structure in this system is the `Restaurant` class. 
Here are the attributes of the `Restaurant` class:

- **Name:** The name of the restaurant.
- **Cuisine:** The type of cuisine offered.
- **Rating:** The rating of the restaurant.
- **Distance:** The distance from a reference point (in kilometers).
- **Location:** The general location or area of the restaurant.

## Implementation:

Created a variable user_input and passed as parameter to the function as recommend_restaurant(user_input)

user_input = input("Enter the type of food you're craving: ")
recommended = recommend_restaurants(user_input)

Based on the factor like cuisine : restaurant names, rating and location is given for the user.
If the user enters any invalid input, error message displays accordingly. 

For example:
Input: 1234
Output: Oops! No restaurant found for the given cuisine.


## Usage

To use the system, follow these steps:

1. Run the `main()` function in the provided Python script.
2. Input the type of food you're craving when prompted.
3. The system will generate and display a list of recommended restaurants based on your cuisine preference.

## Sample Output

```plaintext
Enter the type of food you're craving: Italian

Recommended Restaurants:
1. Name: Tre-Forni Bar & Restaurant, Rating: 4.5, Distance: 6 km, Location: Kondapur
2. Name: Olive Bistro, Rating: 4.5, Distance: 3 km, Location: Madhapur
3. Name: Ci Gusta!, Rating: 4.2, Distance: 1 km, Location: kukatpally

While writing the code, every block of code is tested and corrected accordingly.
I have written few test cases in the test_recommendation.py file.
