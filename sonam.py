#!/usr/bin/env python3
"""Math and String Processing Program with 6 functions"""

import re
import urllib.request

def is_prime(n):
    """Check if a number is prime"""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def prime_sum(start, end):
    """Sum all primes in range (inclusive)"""
    if start > end: start, end = end, start
    return sum(n for n in range(start, end + 1) if is_prime(n))

def convert_length(value, direction):
    """Convert between meters and feet"""
    if direction.upper() == 'M': # Meters to feet
        return round(value * 3.28084, 2)
    elif direction.upper() == 'F': # Feet to meters
        return round(value * 0.3048, 2)
    raise ValueError("Direction must be 'M' or 'F'")

def count_consonants(text):
    """Count consonants in a string"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return sum(1 for c in text.lower() if c.isalpha() and c not in "aeiou")

def find_min_max(numbers):
    """Find min and max values in a list"""
    if not numbers:
        raise ValueError("List cannot be empty")
    return min(numbers), max(numbers)

def is_palindrome(text):
    """Check if string is palindrome (ignores spaces and case)"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    clean = ''.join(text.lower().split())
    return clean == clean[::-1]

def count_words(url):
    """Count specific words in a text file"""
    target_words = ["the", "was", "and"]
    counts = {word: 0 for word in target_words}
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
        
        words = re.findall(r'\b\w+\b', content.lower())
        for word in words:
            if word in counts:
                counts[word] += 1
        return counts
    except Exception as e:
        raise RuntimeError(f"Error: {str(e)}")

def get_int(prompt):
    """Get valid integer input"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_float(prompt):
    """Get valid float input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    """Main program loop"""
    functions = {
        1: ("Prime Number Sum", lambda: (
            print("\n=== Prime Number Sum Calculator ==="),
            (start := get_int("Start range: ")),
            (end := get_int("End range: ")),
            print(f"Sum of primes from {start} to {end}: {prime_sum(start, end)}")
        )),
        2: ("Length Converter", lambda: (
            print("\n=== Length Unit Converter ==="),
            (value := get_float("Value to convert: ")),
            (direction := input("Direction (M for meters to feet, F for feet to meters): ")),
            (result := convert_length(value, direction)),
            print(f"{value} {'meters' if direction.upper() == 'M' else 'feet'} = {result} {'feet' if direction.upper() == 'M' else 'meters'}")
        )),
        3: ("Consonant Counter", lambda: (
            print("\n=== Consonant Counter ==="),
            (text := input("Enter text: ")),
            print(f"Consonants in \"{text}\": {count_consonants(text)}")
        )),
        4: ("Min-Max Finder", lambda: (
            print("\n=== Min-Max Number Finder ==="),
            (count := get_int("How many numbers? ")),
            (nums := [get_float(f"Number {i+1}: ") for i in range(count)]),
            (min_val, max_val) := find_min_max(nums),
            print(f"Smallest: {min_val}, Largest: {max_val}")
        )),
        5: ("Palindrome Checker", lambda: (
            print("\n=== Palindrome Checker ==="),
            (text := input("Enter text: ")),
            print(f"Is \"{text}\" a palindrome? {is_palindrome(text)}")
        )),
        6: ("Word Counter", lambda: (
            print("\n=== Word Counter ==="),
            (url := "https://gist.githubusercontent.com/konrados/a1289ade329ac6f4598ebf5ee3bcb3c/raw/61667e95e3e5d5ad0f49549c2bce3c5cf92219ce/SampleText.txt"),
            (counts := count_words(url)),
            print("Word counts:"),
            [print(f"'{word}': {count}") for word, count in counts.items()]
        ))
    }
    
    print("Math and String Processing Program")
    
    while True:
        print("\n===== MENU =====")
        for num, (name, _) in functions.items():
            print(f"{num}. {name}")
        print("0. Exit")
        
        choice = get_int("Enter choice (0-6): ")
        
        if choice == 0:
            print("Goodbye!")
            break
        elif choice in functions:
            try:
                functions[choice][1]()
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print("Invalid choice. Please enter 0-6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
