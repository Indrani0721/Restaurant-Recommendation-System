import random

class Restaurant:
    def __init__(self, name, cuisine, rating, distance, location):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.distance = distance
        self.location = location


# Sample data
restaurants = [
    Restaurant("Olive Bistro", "Italian", 4.5, 3, "Madhapur"),
    Restaurant("Dine Inn China", "Chinese", 4.0, 2, "Hitech city"),
    Restaurant("Alchemy", "Mexican", 3.5, 5, "Hitechcity"),
    Restaurant("Ci Gusta!", "Italian", 4.2, 1, "kukatpally"),
    Restaurant("Chung Hua", "Chinese", 4.1 , 4, "Madhapur"),
    Restaurant("Santhosh Daba", "North Indian", 4.3, 2, "Hafeezpet"),
    Restaurant(" AB's", "Carribbean", 3.2, 5, "Miyapur"),
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

def recommend_restaurants(user_preference):
    recommended_restaurants = []
    for restaurant in restaurants:
        if restaurant.cuisine.lower() == user_preference.lower():
            recommended_restaurants.append(restaurant)

    if not recommended_restaurants:
        raise ValueError("Oops! No restaurant found for the given cuisine.")

    recommended_restaurants.sort(key=lambda x: x.rating, reverse=True)
    return recommended_restaurants

def main():
    try:
        user_input = input("Enter the type of food you're craving: ")
        recommended = recommend_restaurants(user_input)

        print("\nRecommended Restaurants:")
        for index, restaurant in enumerate(recommended, start=1):
            print(f"{index}.Name: {restaurant.name}, Rating: {restaurant.rating}, Distance: {restaurant.distance} km, Location: {restaurant.location}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
