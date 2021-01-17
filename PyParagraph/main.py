import os
import csv
import re


input_path1 = os.path.join('Resources', 'paragraph_1.txt')
input_path2 = os.path.join('Resources', 'paragraph_2.txt')


# Create a "get-file-name" function.
# Not really part of the problem, just for fun...
def file_name(file_path):
    a = file_path.split('/')
    for b in a:
        if b.endswith('.txt'):
            file = b
    return b


def passage_analysis(input_path):

    with open(input_path, 'r') as text:
        lines = text.read()

        # Word count
        words = re.split("[, \n\-.!?:]+", lines)
        word_count = len(words)

        # Sentence count
        sentences = lines.split(". ")
        sentence_count = len(sentences)

        # Letter count
        letters = ''
        for letter in words:
            letters += letter
        letter_count = round(len(letters)/word_count,2)

        # Sentence length (equals to word count divided by sentence count)
        average_sentence_length = word_count / sentence_count

    # Print the results to the terminal
    print(f'Paragraph Analysis: "{file_name(input_path)}"')
    print('-----------------')
    print(f'Approximate Word Count: {word_count}')
    print(f'Approximate Sentence Count: {sentence_count}')
    print(f'Average Letter Count: {letter_count}')
    print(f'Average Sentence Length: {average_sentence_length}')


# Show results by calling function "passage_analysis"
passage_analysis(input_path1)
passage_analysis(input_path2)
