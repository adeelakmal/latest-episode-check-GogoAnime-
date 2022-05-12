from bs4 import BeautifulSoup
import requests  # didnt use becuase they were being blocked by cloudflare
import cloudscraper  # because cloudflare blocks normal requests on gogoanime
from plyer import notification  # to get notification on desktop
import time
import sqlite3

db = sqlite3.connect('Database.db') #Connecting to Database
print('CONNECTION TO DATABASE ESTABLISHED!')

def main(awaiting_ep, urlDB):

    url = urlDB
   
    # Getting the raw html doc
    scraper = cloudscraper.create_scraper()  # intializes scraper
    doc = scraper.get(url)  # fethces request
    html = doc.text  # returns the html document

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('title')
    
    # main container for the episode links
    links_container = soup.find_all(class_='anime_video_body')
    links = links_container[0].find_all('a')  # returns a list of anchor tag

    # print(title)
    # print(soup.prettify())
    # print(links)

    inner_text = links[0].text  # retruns first and last ep as a whole string
    episodes_array = inner_text.split('-')  # turns them into an array
    first_ep = episodes_array[0]  # First episode
    current_ep = episodes_array[-1]  # recent updated episode on the website

    print('First Episode is:', first_ep)
    print('Recent Episode is:', current_ep)

    # incase new episode are uploaded this part will execute
    if int(current_ep) >= int(awaiting_ep):
        print('yay! new episodes have been uploaded :D\n')
        
        # Script for notifying
        notification.notify(title='Gogo Notifications',
                            message='Yay! Episode '+str(awaiting_ep)+' for ' +
                            title[0].text[:-13]+' has been uploaded :D')
        awaiting_ep += 1

        #Updating DB with latest episode
        db.execute('UPDATE ANIME set CURRENT_EPISODE = ? WHERE URL = ?',
                   (awaiting_ep,url))
        db.commit()
        
        main(awaiting_ep, url)  # so it is updated to the latest ep
        
    #elif int(awaiting_ep) > int(current_ep):
        # print('THIS PART IS WORKING', current_ep)
        #awaiting_file = open('awaiting episode.txt', 'r+')
        #awaiting_file.truncate(0)
        #awaiting_file.write(str(current_ep))
        #awaiting_file.close()
        #main(current_ep)  # so it is updated to the latest ep

    else:
        print('No new episodes :(\n')
        # main(awaiting_ep)  so the program keeps running



listdb = db.execute('SELECT * FROM ANIME')
for row in listdb:
    print(f'SENDING THIS DATA TO BE LOOKED UP...\nAnime: {row[1]} & Episode: {row[3]}')
    main(row[3],row[2])
db.close()

