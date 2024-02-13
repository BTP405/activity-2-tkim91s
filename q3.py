def wordCount(t):
    word_occurrences = {}  # Initialize an empty dictionary to store word occurrences
    with open(t, 'r') as file:  # Open the file in read mode
        for line_number, line in enumerate(file, start=1):  # Iterate through each line in the file
            words = line.split()  # Split the line into a list of words
            for word in words:  # Iterate through each word in the line
                word = word.strip()  # Remove leading/trailing whitespaces
                if word not in word_occurrences:  # If the word is not in the dictionary
                    word_occurrences[word] = [line_number]  # Add a new entry with the word and line number
                else:
                    word_occurrences[word].append(line_number)  # If the word is already in the dictionary, append the line number

    return word_occurrences  # Return the dictionary of word occurrences

result = wordCount("sample.txt")
print(result)
