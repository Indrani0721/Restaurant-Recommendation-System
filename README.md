## Restaurant Recommendation System

## Overview:

This Python program is designed to provide restaurant recommendations based on user-input food preferences. It utilizes a data structure to store restaurant information and implements an algorithm that considers user preferences, ratings, and proximity to suggest relevant dining options.

## Table of contents :

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Setup instructions](#setup-instructions)
- [Project Structure](#Project-Struture)
- [Data Preparation](#Data-preparation)
- [Implementation](#implementation)
- [User interaction](#user-interaction)
- [Testing](#Testing)

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

## Data Preparation:

Created a list of restaurants based on the users input with the data structure list.

recommended_restaurants = []



## Implementation:

Created a variable user_input and passed as parameter to the function as recommend_restaurant(user_input)

user_input = input("Enter the type of food you're craving: ")
recommended = recommend_restaurants(user_input)

Based on the factor like cuisine : restaurant names, rating and location is given for the user.
if the user enters any invalid input, error message displays accordingly. 

For example:
Input: 1234
Output: Oops! No restaurant found for the given cuisine.

## User Interaction:

Recommended restaurants are displayed according to the user craving, and cuisine chosen by the user. 
Name, ranting, distance and location is given accordingly.

## Testing:

While writing the code, every block of code is tested and corrected accordingly.
I have written few test cases in the test_recommendation.py file.
