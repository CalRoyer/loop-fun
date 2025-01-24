 '''
 Cal Royer
 1/24/25
 Loop Fun
 '''

 def main():
    # Part 1 - Get user input
    height = int(input("Enter a box height (between 3 and 10): "))
    while height < 3 or height > 10:
        print("That number is out of bounds: Try again.")
        height = int(input("Enter a box height (between 3 and 10): "))

    width = int(input(f"Enter a box width (greater than {height} and no more than 20): "))
    while width <= height or width > 20:
        print("That number is out of bounds: Try again.")
        width = int(input(f"Enter a box width (greater than {height} and no more than 20): "))

    # Part 2a - Print numbers
    print(f"\nThe integers from {height} to {width} are:")
    for num in range(height, width + 1):
        print(num, end=" ")
    print()

    # Part 2b - Calculate and print average of the numbers
    total = sum(range(height, width + 1))
    count = width - height + 1
    average = total / count
    print(f"\nand the average of those numbers is {average:.1f}.\n")

    # Part 3 - Print the hollow box
    print("*" * width)
    for _ in range(height - 2):
        print("*" + " " * (width - 2) + "*")
    print("*" * width)

    # Part 4 - Print the triangular shape
    print()
    for i in range(1, height + 1):
        print("*" * (2 * i))

if __name__ == '__main__':
    main()
