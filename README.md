Restaurant Recommendation System

Overview:

This Python program is designed to provide restaurant recommendations based on user-input food preferences. It utilizes a data structure to store restaurant information and implements an algorithm that considers user preferences, ratings, and proximity to suggest relevant dining options.

## Setup instructions 
Firstly installed python latest version from the official webiste.
Used this link: (https://www.python.org/)  for installing.
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

## Data Preparation:

In the data preparation, created a class of restaurant with the calling function



## Implementation:

Created a variable user_input and passed as parameter to the function as recommend_restaurant(user_input)

user_input = input("Enter the type of food you're craving: ")
recommended = recommend_restaurants(user_input)

Based on the factor like cuisine : restaurant names, rating and location is given for the user.
if the user enters any invalid input, error message displays accordingly. 

for example:
input: 1234
output: Oops! No restaurant found for the given cuisine.

## User interaction:

Recommended restaurants are displayed according to the user craving and available restaurants.

## Testing:

While writing the code, every block of code is tested and corrected accordingly.
I have written few test cases in the test_recommendation.py file.
