#!/usr/bin/env python

import sys
from collections import defaultdict

def reducer():
    total_term_frequency = defaultdict(int)
    total_documents = 0

    for line in sys.stdin:
        term, frequency = line.strip().split('\t')
        total_term_frequency[term] += int(frequency)
        total_documents += 1

    for term, tf in total_term_frequency.items():
        idf = total_documents / (total_term_frequency[term] + 1)
        print(f"{term}\t{tf}\t{idf}")

# Call the reducer function
reducer()
