import sqlite3


#Tehtävä 4

conn = sqlite3.connect("musicalbums.db")
cursor = conn.cursor()

cursor.execute("""  CREATE TABLE Albums (
    albumName TEXT NOT NULL,
    companyName TEXT NOT NULL,
    year INTEGER,
    length INTEGER,
    genre TEXT CHECK(genre IN ('pop', 'rock', 'jazz', 'blues', 'heavy metal', 'country', 'classical',
    'folk')),
    PRIMARY KEY (albumName, companyName)
    FOREIGN KEY (companyName) REFERENCES Companies(companyName)
    );""")


cursor.execute("""  CREATE TABLE Companies (
    companyName TEXT NOT NULL PRIMARY KEY,
    country TEXT DEFAULT 'Finland',
    webpage TEXT
    );""")

cursor.execute("""  CREATE TABLE Artists (
    artistName TEXT NOT NULL PRIMARY KEY,
    country TEXT NOT NULL,
    born INTEGER CHECK(born BETWEEN 1850 AND 2030)
    );""")

cursor.execute("""  CREATE TABLE Tracks (
    trackNo INTEGER NOT NULL CHECK(trackNo > 0 AND trackNo < 45),
    albumName TEXT NOT NULL,
    companyName TEXT NOT NULL,
    trackName TEXT,
    artistName TEXT NOT NULL,
    composer TEXT,
    lyricist TEXT,
    length INTEGER,
    PRIMARY KEY (albumName, companyName, trackNo),
    FOREIGN KEY (albumName, companyName) REFERENCES Albums(albumName, companyName),
    FOREIGN KEY (artistName) REFERENCES ArWsts(artistName)
    );""")

cursor.execute("""  INSERT INTO Artists
                    VALUES('Räkä', 'Kebabia', 1999);
                    """)


cursor.execute("SELECT country FROM Artists WHERE artistName = 'Räkä';")

conn.commit()

rows = cursor.fetchall()

for row in rows:
    print(row)

#Tehtävä 5

#Ensin muodostetaan apufunktioita

   
def tracks():

    help = "INSERT INTO Tracks Values (?, ?, ?, ?, ?, ?, ?, ?);"
    q = float(input("Insert a track:\ntrackNo: "))
    w = input("Name of the album: ")
    t = input("Name of the company: ")
    r = input("trackName: ")
    t = input("artistName: ")
    y = input("composer: ")
    u = input("lyricist: ")
    i = float(input("length: "))
    cursor.execute(help, (q, w, t, r, t, y, u, i))

    print("Next")
    
    conn.commit()

def albums():

    helperf = "INSERT INTO Albums Values (?, ?, ?, ?, ?);"
    q = input("Creating a new album \nName of the album: ")
    w = input("Name of the company: ")
    t = float(input("year: "))
    r = float(input("length: "))
    t = input("genre: ")
    cursor.execute(helperf, (q, w, t, r, t))

    print("Next")

    conn.commit()
    


def companys():

    helps = "INSERT INTO Companies Values (?, ?, ?);"
    q = input("Creating a new company \nName of the company: ")
    w = input("country: ")
    e = input("webpage: ")
    cursor.execute(helps, (q, w, e))

    print("Next")

    conn.commit()
    
def artists():

    qelper = "INSERT INTO Artists Values (?, ?, ?);"
    q = input("Creating a new artist\nartistName: ")
    w = input("country: ")
    e = input("born: ")
    cursor.execute(qelper, (q, w, e))

    print("Next")

    conn.commit()



#Kutsutaan apufunktioita
artists()
artists()

companys()

albums()
albums()

tracks()
tracks()
tracks()

#Haetaan tietoja tietokannasta
newName = input("Enter a name of an artist that should be in the database")

cursor.execute("""  SELECT DISTINCT albumName 
                    FROM Tracks
                    WHERE artistName = :artist_name;""",
               {"artist_name": newName})
conn.commit()

print("Albums: ")

helper = cursor.fetchall()

for album in helper:
    print(album)

cursor.execute("""  SELECT trackName 
                    FROM Tracks 
                    WHERE artistName = :artist_name;""",
               {"artist_name": newName})

conn.commit()

print("Tracks:")

helper = cursor.fetchall()

for a in helper:
    print(a)

print("\nProgram finished")

conn.close()