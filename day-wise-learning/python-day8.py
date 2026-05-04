"""
Day 8 - Python Functions + Caesar Cipher

This file covers:
- Functions with parameters
- Positional vs keyword arguments
- Return values
- Caesar Cipher project (encode/decode)

This is IMPORTANT for:
- Logic building
- Data transformation
- Future AI pipelines (input → process → output)
"""

# -------------------------------
# BASIC FUNCTION EXAMPLES
# -------------------------------

def greet(name):
    """Simple function with one parameter"""
    print(f"Hello {name}")


def greet_with(name, location):
    """Function with multiple parameters"""
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


def add(a, b):
    """Function with return value"""
    return a + b


def format_name(f_name, l_name):
    """Formats name properly"""
    return f_name.title() + " " + l_name.title()


# -------------------------------
# CAESAR CIPHER PROJECT
# -------------------------------

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]


def caesar(text, shift, direction):
    """
    Caesar Cipher function
    
    Parameters:
    - text: message string
    - shift: number of shifts
    - direction: 'encode' or 'decode'
    
    Returns:
    - transformed string
    """

    # Handle large shift values
    shift = shift % 26

    # Reverse shift for decoding
    if direction == "decode":
        shift *= -1

    result = ""

    for char in text:
        if char in alphabet:
            new_position = (alphabet.index(char) + shift) % 26
            result += alphabet[new_position]
        else:
            # Keep numbers, spaces, symbols unchanged
            result += char

    return result


# -------------------------------
# MAIN PROGRAM LOOP
# -------------------------------

def run_cipher():
    """Runs the Caesar Cipher program in loop"""

    while True:
        direction = input("Type 'encode' or 'decode': ").lower()
        text = input("Enter your message: ").lower()
        shift = int(input("Enter shift number: "))

        output = caesar(text, shift, direction)
        print(f"Result: {output}")

        restart = input("Type 'yes' to continue or 'no' to exit: ").lower()
        if restart == "no":
            print("Goodbye 👋")
            break


# -------------------------------
# ENTRY POINT
# -------------------------------

if __name__ == "__main__":
    # Example usages (uncomment to test basics)
    
    # greet("Siddharth")
    # greet_with(name="Siddharth", location="Delhi")
    # print(add(2, 3))
    # print(format_name("siddharth", "verma"))

    # Run main project
    run_cipher()