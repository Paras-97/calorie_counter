'''
    This script will help you track calories 
    and generate data based on the foods you consume
'''

import csv


global save_data
global cals


def meal_cal_counter(meal_type, meals) -> None:
    '''Calculates meal calories

    Args:
        meal_type (string): user selection
        meals (dict): meals presented to the user
    '''


    global cals
    global save_data
    print("What would you like to have for {}?".format(meal_type))
    print("The options are: ")
    for _,meal in enumerate(meals,1):
        print(str(_)+"."+meal+" ---------- "+str(meals[meal])+"cals")
    
    select_meal = input("\n Please choose the number infront of the meal: ")
    meal_selected = ""
    j = 0
    for _,meal in enumerate(meals,1):
        if str(_) == select_meal:
            meal_selected = meal
            cals = cals - meals[meal]
    print("Your selected meal is: ", meal_selected)
    print("Your remaining calories for the day are: ", cals)
    save_data.append([meal_type, meal_selected, meals[meal_selected]])


def main():
    '''Start of the program
    '''

    global save_data
    global cals
    
    name = input("Enter you name: ")
    cals = int(input("Enter your total calories: "))
    save_data = []

    

    breakfast = {"Oats":200, "Bread and eggs":300, "Smashed avocado with two breads":400} #To be updated by api
    lunch = {"Rice and curry":600, "Chicken breast and roasted veggies":500, "Chicken curry with rice":600} #To be updated by api
    dinner = {"Salmon and asparagus":600, "Chicken breast and veggies":500, "Salad":300} #To be updated by api

    meal_inp = input("Press: \n 1 for Breakfast \n 2 for Lunch \n 3 for Dinner \n")

    if(meal_inp == "1"):
        meal_cal_counter("Breakfast",breakfast)
    if(meal_inp == "2"):
        meal_cal_counter("Lunch",lunch)
    if(meal_inp == "3"):
        meal_cal_counter("Dinner",dinner)

        
    columns = ["Meal_Type","Meal_Selected","Calories"]
    with open(name+".csv", 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
        write.writerows(save_data)


if __name__ == "__main__":
    main()