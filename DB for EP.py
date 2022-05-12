import sqlite3

db = sqlite3.connect('Database.db') #Print database to keep track of episodes

#TABLE CREATION AND INSERTION
def Creation():
    db.execute('''
                CREATE TABLE ANIME
                (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                URL TEXT NOT NULL,
                CURRENT_EPISODE INT NOT NULL);
                ''')
    print('Table Created')

'''db.execute("INSERT INTO ANIME(ID,NAME,URL,CURRENT_EPISODE)\
            VALUES(1, 'Demon Slayer 2S', 'https://www1.gogoanime.cm/category/kimetsu-no-yaiba-yuukaku-hen', 0);")
db.commit()

db.execute("INSERT INTO ANIME(ID,NAME,URL,CURRENT_EPISODE)\
            VALUES(2, 'Demon Slayer 2S', 'https://www2.gogoanime.cm/category/shingeki-no-kyojin-the-final-season-part-2', 0);")
db.commit()'''

def Add_to_DB(ID,name,url):
    db.execute("INSERT INTO ANIME(ID,NAME,URL,CURRENT_EPISODE)\
                VALUES(?, ?, ?, 0)",
               (ID,name,url))
    db.commit()

def DataEntry():
    listdb = db.execute('SELECT ID FROM ANIME')
    for row in listdb:
        ID = row[0] #Gets the last id no will be used to increment ID in function call
    name = input('Enter Name of the Anime:')
    url = input('Enter the URL of the Anime from GogoAnime:')
    Add_to_DB(ID+1,name,url)

def ViewDB():
    names = db.execute("SELECT NAME FROM ANIME")
    for row in names:
        print(row[0])

def PrintMenu():
    print("---WELCOME TO THE MENU---")
    print("1: Add new entry to database.")
    print("2: View entries in database.")

def UserSelection():
    selection = int(input("\nSELECT WHAT DO YOU WANT TO DO:"))
    if selection < 1 or selection > 2: 
        raise Exception("Whoops enter a valid input >=1 and <=2")
    if selection == 1:
        DataEntry()
    if selection == 2:
        ViewDB()

if __name__ == "__main__":
    PrintMenu()
    UserSelection()
    
    

    

