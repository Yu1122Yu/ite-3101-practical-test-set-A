def main():
    while True:
        try:
            number = int(input())
            break
        except ValueError:
            print("Please enter an integer.")

    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} is divisible by both 3 and 5.")
    else:
        print(f"{number} is not divisible by both 3 and 5.")


if __name__ == "__main__":
    # execute only if run as a script
    main()
