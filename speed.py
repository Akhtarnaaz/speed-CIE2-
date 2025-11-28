import sys

def calculate_speed(distance, time):
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    return distance / time

def main():
    # Case 1: User passed arguments → use them
    if len(sys.argv) == 3:
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
    else:
        # Case 2: No arguments → ask for input
        distance = float(input("Enter distance traveled (in km): "))
        time = float(input("Enter time taken (in hours): "))

    try:
        speed = calculate_speed(distance, time)
        print(f"Speed: {speed} km/h")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
