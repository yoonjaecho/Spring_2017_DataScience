import crawler
import sys
import random
import pytagcloud
import webbrowser

from collections import Counter 
from konlpy.tag import Hannanum

class Wordcloud:
    def __init__(self, gallery, pagenum, topN):
        self.crawler = crawler.DC_Crawler(gallery, pagenum)
        self.hannanum = Hannanum()
        self.topN = topN 
        
    def get_text(self):
        text = self.crawler.crawl()
        '''
        f = open("dc_data.txt", "w")
        f.write(text)
        f.close()
        '''
        return text
    
    def get_tags(self, text, multiplier=10):
        nouns = self.hannanum.nouns(text)

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

        count = Counter(filtered_nouns)
        r = lambda: random.randint(0, 255)
        color = lambda: (r(), r(), r())
        
        return [{'color': color(), 'tag': n, 'size': c*multiplier} for n, c in count.most_common(self.topN)]
    
    def draw(self, filename, size=(800, 600)):
        text = self.get_text()
#print(text)
        tags = self.get_tags(text)
        pytagcloud.create_tag_image(tags, filename, fontname='Korean', size=size)
        print("Draw completed !")

if __name__ == '__main__':
    # Draw top 10 frequency word
    Wordcloud(gallery='tree', pagenum=1, topN=10).draw('image_wordcloud.png')
