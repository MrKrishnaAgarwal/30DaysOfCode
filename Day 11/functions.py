def food_item(preference):
    food= input("What would you like to eat? ")
    if food == "pizza":
        print("I like pizza too and It's my favorite food if I had to choose one.")
    elif food == "salad":
        print("I like salad too and It will be ready in 5 minutes with a side of dressing.")
    elif food == "ice cream":
        print("I like ice cream too and we have 3 flavors and 2 toppings.")
    else:
        print("I don't like that food but I will make it for you anyway.")

def main():
    food_item("pizza")
    food_item("salad")
    food_item("ice cream")
if __name__ == "__main__":
    main()