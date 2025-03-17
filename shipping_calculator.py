def main():
    # Display welcome message
    print("Welcome to Package Express. Please follow the instructions below.")

    # Get package weight from user
    print("Please enter the package weight:")
    weight = float(input())

    # Check if package is too heavy (over 50 pounds)
    if weight > 50:
        print("Package too heavy to be shipped via Package Express. Have a good day.")
        return  # End program if package is too heavy

    # Get package dimensions from user
    print("Please enter the package width:")
    width = float(input())

    print("Please enter the package height:")
    height = float(input())

    print("Please enter the package length:")
    length = float(input())

    # Calculate total dimensions
    total_dimensions = width + height + length

    # Check if package is too big (dimensions total over 50)
    if total_dimensions > 50:
        print("Package too big to be shipped via Package Express.")
        return  # End program if package is too big

    # Calculate shipping quote:
    # 1. Multiply dimensions (width * height * length)
    # 2. Multiply by weight
    # 3. Divide by 100 to get final quote
    quote = (width * height * length * weight) / 100

    # Display the shipping quote formatted as currency with 2 decimal places
    print(f"Your estimated total for shipping this package is: ${quote:.2f}")
    print("Thank you!")

# Run the program
if __name__ == "__main__":
    main() 