#!/usr/bin/python3

# Author: Jay Balangue
# Date: 2026-07-07
# Module: 1
# Lab: Python Programming

'''
PIZZA ORDER COST CALCULATOR
---------------------------

PSEUDOCODE
----------

FUNCTION create_order
    SET ordering to True
    SET total_cost to 0
    WHILE ordering is True
        CALL create_pizza
        PROMPT user to confirm the base_price (yes/no)
        IF user confirms the base_price
            ADD base_price to total_cost
        PROMPT user if they want to order another pizza (yes/no)
        IF user wants to order another pizza
            CONTINUE ordering
        ELSE
            SET ordering to False
            PROMPT user for delivery distance in miles
            ADD $2 to total_cost for the first 5 miles
            IF distance is greater than 5
                ADD (distance - 5) to total_cost for each additional mile
            RETURN total_cost
END FUNCTION

FUNCTION create_pizza
        PROMPT user for pizza size (small or large)
        IF size is small
            SET base_price to 8
        ELSE IF size is large
            SET base_price to 12
        ELSE
            DISPLAY "Invalid size. Please choose small or large."
            CONTINUE create_pizza
        PROMPT user for number of additional toppings
        IF number of toppings is greater than 0
            ADD number of toppings to base_price
        RETURN base_price
END FUNCTION

START
    CALL create_order
    DISPLAY total_cost
END
'''

def create_order():
    total_cost = 0

    while True:
        base_price = create_pizza()
        confirm = input(f"The base price for your pizza is ${base_price}. Do you want to confirm this order? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            total_cost += base_price
            print(f"Order confirmed. Current total cost: ${total_cost}")

        another_order = input("Do you want to order another pizza? (yes/no): ").strip().lower()
        if another_order != 'yes':
            break

    while True:
        try:
            distance = float(input("Enter delivery distance in miles: "))
            if distance < 0:
                print("Distance cannot be negative. Please enter a valid distance.")
                continue
            total_cost += 2  # $2 for the first 5 miles
            if distance > 5:
                total_cost += (distance - 5)  # $1 for each additional mile
            break
        except ValueError:
            print("Invalid input. Please enter a valid distance.")

    return total_cost

def create_pizza():
    while True:
        size = input("Enter pizza size (small/large): ").strip().lower()
        if size == 'small':
            base_price = 8
            break
        elif size == 'large':
            base_price = 12
            break
        else:
            print("Invalid size. Please choose small or large.")

    while True:
        try:
            toppings = int(input("Enter number of additional toppings: "))
            if toppings < 0:
                print("Number of toppings cannot be negative. Please enter a valid number.")
                continue
            base_price += toppings  # Each topping costs $1
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return base_price

if __name__ == "__main__":
    print("\n-------------------------------------------")
    print("Welcome to the Pizza Order Cost Calculator!")
    print("-------------------------------------------\n")
    total_cost = create_order()
    print(f"Total cost of your order: ${total_cost}")

