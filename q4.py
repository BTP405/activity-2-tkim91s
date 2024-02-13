def stats_decorator(func):
    def wrapper(numbers):
        count = len(numbers)
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)

        print("Numbers:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)

        func(numbers)

    return wrapper

@stats_decorator
def process_numbers(numbers):
    # Your additional processing logic here, if needed
    pass

def printStats(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert each line to a list of numbers
                numbers = list(map(float, line.split()))
                process_numbers(numbers)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


printStats('sample_number.txt')
