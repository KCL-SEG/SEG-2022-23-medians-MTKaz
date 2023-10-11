"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

def findMedian(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 1:
        return numbers[len(numbers)//2]#It returns the middle value in the sorted list: median
    else:
        return (numbers[len(numbers)//2] + numbers[(len(numbers)//2)+1])/2#It returns the average of the two median values