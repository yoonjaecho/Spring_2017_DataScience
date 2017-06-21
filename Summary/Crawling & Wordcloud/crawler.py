from bs4 import BeautifulSoup
import urllib.request
import time
import random
import sys

class DC_Crawler:
    def __init__(self, gallery, pagenum):
        self.list_url = 'http://gall.dcinside.com/board/lists/?id=' + gallery
        self.view_url = 'http://gall.dcinside.com/board/view/?id=' + gallery
        self.pagenum = int(pagenum)
        self.text = ''
        
    def crawl(self):
        page = 1
        
        while page <= self.pagenum:
            url_open = urllib.request.urlopen(self.list_url + '&page=' + str(page))
            soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

            notice_list = soup.findAll('td', {'class':'t_notice'})
            subject_list = soup.findAll('td', {'class':'t_subject'})

            # Exclude notice post
            for _ in notice_list:
                if notice_list[0].text == '공지':
                    notice_list.pop(0)
                    subject_list.pop(0)
                else:
                    break

            print('Start crawling %d page subject..\n\n' %(page))

            for subject in subject_list:
                print(subject.text)
                self.text += subject.text + '\n'

            rand_num = random.randrange(1,5)
            print('\nCrawling %d page subject complete. %d sec sleep...\n' %(page, rand_num))
            time.sleep(rand_num)

            print('Start crawling %d page content..\n\n' %(page))
            
            for notice in notice_list:
                url_open = urllib.request.urlopen(self.view_url + '&no=' + str(notice.text) + '&page=' + str(page))
                soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')
                content = soup.find('div', {'class':'s_write'})
                text_content = content.table.tr.td.text

                print(text_content)
                self.text += text_content + '\n'

                rand_number = random.randrange(1,4)
                print('Sleep intentionally %d sec..' %(rand_number))
                time.sleep(rand_num)

            print('\nCrawling %d page content complete.\n' %(page))

            page += 1
        
        return self.text
    
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('python3 crawler.py [gallery_name] [page_numer] [output_file_name]')
        sys.exit()

    text = DC_Crawler(gallery=sys.argv[1], pagenum=sys.argv[2]).crawl()
    f = open(sys.argv[3], "w")
    f.write(text)
    f.close()
