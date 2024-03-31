#!/usr/bin/env python

import sys
import re
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Load NLTK resources
nltk.download('punkt')

def clean_text(text):
    if isinstance(text, str):
        # Convert text to lowercase
        text = text.lower()
       
        # Remove special characters and punctuation
        text = re.sub(r'[^\w\s]', '', text)

        # Replace multiple whitespaces with a single whitespace
        text = re.sub(r'\s+', ' ', text)
       
        # Remove leading and trailing whitespaces
        text = text.strip()
       
        return text
    else:
        return ''  # Return empty string for non-string values

def tokenize_text(text):
    if isinstance(text, str):
        tokens = word_tokenize(text)
        return tokens
    else:
        return []

def calculate_tf(tokens):
    # Count the frequency of each token in the document
    tf = Counter(tokens)
    # Convert the counts to the format (term_index, frequency)
    return [(word, freq) for word, freq in tf.items()]

def mapper():
    try:
        # Data loading and preprocessing
        for line in sys.stdin:
            # Assuming each line represents a document
            line = clean_text(line)
            tokens = tokenize_text(line)
            term_frequencies = calculate_tf(tokens)
            for term, frequency in term_frequencies:
                print(f"{term}\t{frequency}")

    except Exception as e:
        sys.stderr.write(f"Error processing data: {e}\n")
        sys.exit(1)

# Call the mapper function
mapper()

