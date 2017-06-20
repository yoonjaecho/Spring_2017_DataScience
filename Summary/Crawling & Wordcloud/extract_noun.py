import sys
from konlpy.tag import Twitter
from collections import Counter
import os

class Noun_extractor:
    def __init__(self):
        self.spliter = Twitter()
        
    def extract(self, text):
        nouns = self.spliter.nouns(text)
        
        # Filtering words with digit
        no_number = list()
        for element in nouns:
            no_digit = True
            for ch in element:
                if ch.isdigit():
                    no_digit = False
                    break
            if no_digit:
                no_number.append(element)
                
        # Filtering words which length is less than 2
        filtered_nouns = [noun for noun in no_number if len(noun) >= 2]
        
        return filtered_nouns
    
    def extract_from_file(self, input_file, output_file):
        input_text_file = open(input_file, 'r')
        text = input_text_file.read()
        input_text_file.close()
        
        output_text_file = open(output_file, 'w')
        nouns = self.spliter.nouns(text)
        
        # Filtering length <= 2 word.
        for n in nouns:
            if len(n) >= 2:
                output_text_file.write(' ' + n)
                
        output_text_file.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error!!")
        print('python3 extract_noun.py [input_file] [output_file]')
        sys.exit()
        
    Noun_extractor().extract_from_file(input_file=sys.argv[1],output_file=sys.argv[2])
    print('Extract nouns completed.. Saved to', sys.argv[2])
