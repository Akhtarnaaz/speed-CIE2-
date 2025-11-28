def calculate_speed(distance, time):
    """
    Calculate speed given distance and time.

    Args:
        distance (float): Distance traveled in kilometers.
        time (float): Time taken in hours.

    Returns:
        float: Speed in kilometers per hour.
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    speed = distance / time
    return speed

def main():
    distance = float(input("Enter distance traveled (in km): "))
    time = float(input("Enter time taken (in hours): "))
    try:
        speed = calculate_speed(distance, time)
        print(f"Speed: {speed:.2f} km/h")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()