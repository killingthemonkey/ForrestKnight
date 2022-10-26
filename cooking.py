from lasagna import EXPECTED_BAKE_TIME
from lasagna import bake_time_remaining
# EXPECTED_BAKE_TIME, elapsed_minutes
from lasagna import preparation_time_in_minutes
# num_layers
from lasagna import elapsed_time_in_minutes
# elapsed_minutes, preparation_time

def print_menu():
    print("""
    1. See how many minutes it takes to bake a lasagna
    2. See how long it takes to prepare a lasagna
    3. See how many minutes are left to bake
    4. See the total elapsed time since you started cooking the lasagna
    5. Quit

    What would you like to do?
    """)

print_menu()

user_action = 0

while user_action != 5:
    user_action = int(input("> "))
    if user_action == 1:
        print(f"It will take {EXPECTED_BAKE_TIME} minutes to bake your lasagna.")
        print_menu()
    elif user_action == 2:
        print("How many layers?")
        layers = input("> ")
        print(f"It will take approximately {preparation_time_in_minutes(layers)} minutes to prepare your lasagna.")
        print_menu()
    elif user_action == 3:
        print("How long has your lasagna been in the oven?")
        elapsed_time = int(input("> "))
        print(f"There are {bake_time_remaining(EXPECTED_BAKE_TIME, elapsed_time)} minutes left for your lasagna to bake.")
        print_menu()
    elif user_action == 4:
        print("How many minutes did it take to prepare your lasagna?")
        prep_time = int(input("> "))
        print("How many minutes has your lasagna been in the oven?")
        elapsed_time = int(input("> "))
        print(f"You have been cooking for {elapsed_time_in_minutes(prep_time, elapsed_time)} minutes.")
        print_menu()

print("Thank you for using my lasagna guide.")