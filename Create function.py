def most_frequent(string):
    letter_freq = {}
    string = string.replace(" ", "").lower()
    for letter in string:
        if letter.isalpha():
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    for letter, frequency in sorted_freq:
        print(f"{letter} = {frequency}", end=" ")
# Example
input_string = input("Please enter a string: ")
most_frequent(input_string)