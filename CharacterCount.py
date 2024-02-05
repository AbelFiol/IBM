  from collections import defaultdict

def count_characters(input_string):
    # Use defaultdict to automatically initialize counts to 0.
    char_count = defaultdict(int)

    # Iterate through each character in the input string.
    for letter in input_string:
        # Check if the character is an alphabetic character.
        if letter.isalpha():
            # Increment the count for the current character.
            char_count[letter] += 1

    # Convert defaultdict to a regular dictionary before returning.
    return dict(char_count)

# Test the function with the provided examples.
print(count_characters("aabbccc"))
