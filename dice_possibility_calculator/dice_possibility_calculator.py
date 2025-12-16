import random

def diece_simulation(diece_numbers):
    listofresult = [random.randint(1, 6) for _ in range(diece_numbers)]
    return [f"{i}: %{(listofresult.count(i) / diece_numbers) * 100:.2f}" for i in range(1, 7)]

if __name__ == "__main__":
    try:
        diece_numbers = int(input("Enter the number of times to roll the dice: "))
        if diece_numbers > 0:
            print(diece_simulation(diece_numbers))
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a number.")

""" 
Variable Meanings:
- listofresult: Stores the outcomes of all dice rolls in a list.
- diece_numbers: Number of times the dice is rolled.

Created By: Aytuğ Yürük.
"""