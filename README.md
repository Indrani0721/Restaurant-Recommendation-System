## Restaurant Recommendation System

## Overview:

This Python program is designed to provide restaurant recommendations based on user-input food preferences. It utilizes a data structure to store restaurant information and implements an algorithm that considers user preferences, ratings, and proximity to suggest relevant dining options.

## Table of contents :

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Setup instructions](#setup-instructions)
- [Project Structure](#Project-Struture)

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

restaurants = [
    Restaurant("Olive Bistro", "Italian", 4.5, 3, "Madhapur"),
    Restaurant("Dine Inn China", "Chinese", 4.0, 2, "Hitech city"),
    Restaurant("Alchemy", "Mexican", 3.5, 5, "Hitechcity"),
    Restaurant("Ci Gusta!", "Italian", 4.2, 1, "kukatpally"),
    Restaurant("Chung Hua", "Chinese", 4.1 , 4, "Madhapur"),
    Restaurant("Santhosh Daba", "North Indian", 4.3, 2, "Hafeezpet"),
    Restaurant(" AB's", "Caribbean", 3.2, 5, "Miyapur"),
    Restaurant("Udipi Upahar","South Indian", 4.6, 3, "Madeenaguda"),
    Restaurant("Barbeque Nation", "American", 4.8, 6, "Dilshuknagar"),
    Restaurant("Pamrampara", "Indian", 5, 8, "Bnajara Hills"),
    Restaurant("Barbeque Nation", "Asian", 4, 4, "Bnajara Hills"),
    Restaurant("Chutneys", "Indian", 4.2, 4, "JNTU"),
    Restaurant("Bikanervala", "Indian", 4.1, 4, "Kondapur"),
    Restaurant("Haiku", "Thai", 4.3, 8, "Hitech City"),
    Restaurant("Mamagoto", "Thai", 4.5, 6, "Kondapur"),
    Restaurant("Spice 6 Global Cuisine", "Mughlai",4.1, 6, "Secundrabad"),
    Restaurant("Tre-Forni Bar & Restaurant","Italian", 4.5, 6, "Kondapur"),
    Restaurant("ZOUQ","Turkish", 4.1, 7, "Madhapur"),
    Restaurant("MoXa Kitchen","Buffet",3.8, 7, "Nanakramguda"),
    Restaurant("Goguryeo Restaurant", "Korean", 3.8, 5, "Madhapur"),
    Restaurant("Hashi", "Japanese", 4.4, 5, "Kondapur")
]


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

Recommended restaurants are displayed according to the user craving, and cuisine chosen by the user. Name, ranting, distance and location is given accordingly.

## Testing:

While writing the code, every block of code is tested and corrected accordingly.
I have written few test cases in the test_recommendation.py file.
