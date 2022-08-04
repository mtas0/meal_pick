""" First personal python project """

import pandas as pd
import time

mealdir = r"C:\Users\Merve Tas\Documents\Merve\Personal\Projects\meal_pick\meals_df.csv"
df_meals = pd.read_csv(mealdir, sep="\t")


def meal_choice(time, health_l, difficulty_l):
    """randomly choose an item from df depending on use input"""
    mealdir = (
        r"C:\Users\Merve Tas\Documents\Merve\Personal\Projects\meal_pick\meals_df.csv"
    )
    df_meals = pd.read_csv(mealdir, sep="\t")
    filtered = df_meals.query(
        "meal_time == @time and health == @health_l and difficulty == @difficulty_l"
    )["meal"]
    filtered = filtered.sample()
    return filtered.to_string(index=False)


while True:
    meal_time = input("Hello! Enter meal type (breakfast, lunch or dinner): ").lower()
    health = input("How healthy? (healthy, kinda or nah): ").lower()
    level = input("Enter difficulty level (easy, medium or hard): ").lower()
    if (
        meal_time in df_meals.values
        and health in df_meals.values
        and level in df_meals.values
    ):
        print(f"your meal is: {meal_choice(meal_time, health, level)}")
        time.sleep(0.8)
        yesno = input("are you happy with this meal? (y/n) ")
        if yesno == "y":
            time.sleep(0.5)
            print("Enjoy your meal!!")
            break
        else:
            time.sleep(0.8)
            print("Please try again")
    else:
        time.sleep(0.8)
        print("Please enter one of the options in the brackets")
