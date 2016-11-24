import sqlite3

def Singleton(cls):
    _instances = {}
    def getInstance():
        if cls not in _instances:
            _instances[cls] = cls()
        return _instances[cls]
    return getInstance

@Singleton
class Database:
    def __init__(self):
        self._con = sqlite3.connect(':memory:')
        self._cursor = self._con.cursor()
        userTable = "create table if not exists \
                     User (userName text primary key, \
                     password text)"
        self._cursor.execute(userTable)

        topicTable = "create table if not exists \
                      Topic (topicName text primary key)"

        self._cursor.execute(topicTable)

        postTable = "create table if not exists \
                     Post ( \
                     postUser text, \
                     postTopic text, \
                     postText text, \
                     FOREIGN KEY(postUser) REFERENCES User (userName), \
                     FOREIGN KEY(postTopic) REFERENCES Topic (topicName), \
                     primary key(postUser, postTopic))"
        self._cursor.execute(postTable)

    def addUser(self, uName, pwd):
        self._cursor.execute( "insert into User values (?,?)", (uName,pwd) )

    def getUser(self, uName, pwd):
        self._cursor.execute("select password from User where userName = ?", (uName,))
        fetchedPwd = self._cursor.fetchone()
        print(fetchedPwd)
        if(fetchedPwd != None and pwd in fetchedPwd):
            return True
        else:
            return False

    def getTopic(self, tName):
        self._cursor.execute("select * from Topic where topicName = ?", (tName,))
        fetched = self._cursor.fetchone()
        if(fetched != None):
            return True
        else:
            return False

    def addTopic(self, tName):
        self._cursor.execute("select * from Topic where topicName = ?", (tName,))
        fetched = self._cursor.fetchone()
        if(fetched == None):
            self._cursor.execute("insert into Topic Values (?) " ,(tName,))
            self._con.commit()
        
    def addPost(self, user, topic, post):
        try:
            self._cursor.execute("insert into Post Values ( ?,?,? ) ", (user,topic,post) )
            print("Added Post!")
        except sqlite3.IntegrityError:
            print("Cannot Add Post!")

    def getPosts(self, uName):
        self._cursor.execute("select * from Post where postUser = ?", (uName,))
        all_rows = self._cursor.fetchall()
        print(all_rows)

    def kill(self):
        self._con.close()
