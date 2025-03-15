def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sum_of_primes(start, end):
    """Calculate sum of prime numbers in range."""
    return sum(n for n in range(max(2, start), end + 1) if is_prime(n))


def convert_length(value, direction):
    """Convert between meters and feet."""
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)  # Meters to feet
    else:
        return round(value * 0.3048, 2)   # Feet to meters


def count_consonants(text):
    """Count consonants in a string."""
    consonants = "bcdfghjklmnpqrstvwxyz"
    return sum(1 for char in text.lower() if char in consonants)


def find_min_max(numbers):
    """Find min and max numbers in a list."""
    return min(numbers), max(numbers)


def is_palindrome(text):
    """Check if a string is a palindrome."""
    text = ''.join(text.lower().split())
    return text == text[::-1]



def word_count(text_file_url):
    response = request.get(text_file_url)
    text = response.text.lower()
    wlist = ['the', 'was', 'and']
    word = {word: text. count(word) for word in wlist}
    return word_count(word)

def get_input(prompt, input_type=int, min_value=None, max_value=None):
    """Get validated user input of specified type."""
    while True:
        try:
            value = input_type(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Error: Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Error: Value must be at most {max_value}.")
                continue
            return value
        except ValueError:
            print(f"Error: Please enter a valid {input_type.__name__}.")


def prime_number_sum_calculator():
    """Calculate sum of prime numbers in a range."""
    print("\n--- Prime Number Sum Calculator ---")
    start = get_input("Enter the start of the range: ")
    end = get_input("Enter the end of the range: ", min_value=start)
    
    result = sum_of_primes(start, end)
    print(f"The sum of prime numbers between {start} and {end} is: {result}")


def length_unit_converter():
    """Convert between meters and feet."""
    print("\n--- Length Unit Converter ---")
    value = get_input("Enter the length value: ", float, min_value=0)
    
    while True:
        direction = input("Enter direction (M for meters to feet, F for feet to meters): ").upper()
        if direction in ['M', 'F']:
            break
        print("Error: Please enter 'M' or 'F'.")
    
    result = convert_length(value, direction)
    unit_from = "meters" if direction == 'M' else "feet"
    unit_to = "feet" if direction == 'M' else "meters"
    print(f"{value} {unit_from} = {result} {unit_to}")


def consonant_counter():
    """Count consonants in a string."""
    print("\n--- Consonant Counter ---")
    text = input("Enter a text string: ")
    result = count_consonants(text)
    print(f"The text contains {result} consonants.")


def min_max_number_finder():
    """Find min and max numbers in a series."""
    print("\n--- Min-Max Number Finder ---")
    count = get_input("How many numbers do you want to enter? ", min_value=1)
    
    numbers = []
    for i in range(count):
        num = get_input(f"Enter number {i+1}: ", float)
        numbers.append(num)
    
    smallest, largest = find_min_max(numbers)
    print(f"Smallest: {smallest}, Largest: {largest}")


def palindrome_checker():
    """Check if a string is a palindrome."""
    print("\n--- Palindrome Checker ---")
    text = input("Enter a text string: ")
    result = is_palindrome(text)
    print(f"Is '{text}' a palindrome? {result}")


def word_counter():
    """Count specific words in a sample text."""
    print("\n--- Word Counter ---")
    print("Using sample text to count words...")
    
    word_counts = count_words_in_sample_text()
    
    print("\nWord counts:")
    for word, count in word_counts.items():
        print(f"'{word}': {count}")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*40)
    print("MATH AND STRING PROCESSING PROGRAM")
    print("="*40)
    print("1. Prime Number Sum Calculator")
    print("2. Length Unit Converter")
    print("3. Consonant Counter")
    print("4. Min-Max Number Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter")
    print("0. Exit")
    print("="*40)


def main():
    """Main program loop."""
    functions = {
        1: prime_number_sum_calculator,
        2: length_unit_converter,
        3: consonant_counter,
        4: min_max_number_finder,
        5: palindrome_checker,
        6: word_counter
    }
    
    while True:
        display_menu()
        choice = get_input("Enter your choice (0-6): ", min_value=0, max_value=6)
        
        if choice == 0:
            print("Thank you for using the program. Goodbye!")
            break
        
        try:
            functions[choice]()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")