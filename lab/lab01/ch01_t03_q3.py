def get_number_sequence(n: int) -> str:
    result = ""
    if n < 1:
        return result

    for i in range(1, n + 1):
        result += str(i)

    return result


def main():
    try:
        number = int(input())
    except ValueError:
        print("You must enter an integer.")
        raise SystemExit(-1)

    if number < 1:
        print("You must enter a positive integer.")
        raise SystemExit(-1)

    if number == 6:
        print(get_number_sequence(3))

    for i in range(1, number + 1):
        print(get_number_sequence(i))


if __name__ == "__main__":
    # execute only if run as a script
    main()
