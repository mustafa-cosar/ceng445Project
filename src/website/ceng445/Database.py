import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

import sqlite3
from toPickApp.models import *
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def Singleton(cls):
    _instances = {}
    def getInstance():
        if cls not in _instances:
            _instances[cls] = cls()
        return _instances[cls]
    return getInstance

@Singleton
class Database:
    def __init__(self, *args, **kwargs):
        pass

    def addUser(self, username, password, email, first_name, last_name):
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        try:
            user.save()
            return True
        except IntegrityError:
            return False



@Singleton
class DatabaseOld:
    def __init__(self):
        self._con = sqlite3.connect('ceng445.db')
        self._cursor = self._con.cursor()
        userTable = "create table if not exists \
                     User ( ID INTEGER PRIMARY KEY autoincrement,\
                     userName text not null, \
                     password text not null )"
        self._cursor.execute(userTable)

        topicTable = "create table if not exists \
                      Topic (ID integer primary key autoincrement, \
                      topicName text not null )"
        self._cursor.execute(topicTable)

        postTable = "create table if not exists \
                     Post ( ID integer primary key autoincrement, \
                     userID integer, \
                     topicID integer, \
                     postText text not null, \
                     postUser text not null, \
                     postTopic text not null, \
                     FOREIGN KEY(postUser) REFERENCES User (userName), \
                     FOREIGN KEY(postTopic) REFERENCES Topic (topicName),\
                     FOREIGN KEY(userID) REFERENCES User (ID), \
                     FOREIGN KEY(topicID) REFERENCES Topic (ID) )"
        self._cursor.execute(postTable)

        likeTable = "create table if not exists \
                    Like ( likingUserID integer not null, \
                    postID integer not null, \
                    FOREIGN KEY(likingUserID) REFERENCES User (ID),\
                    FOREIGN KEY(postID) REFERENCES Post (ID), \
                    primary key(likingUserID, postID) )"
        self._cursor.execute(likeTable)

        dislikeTable = "create table if not exists \
                    Dislike ( dislikingUserID integer not null, \
                    postID integer not null, \
                    FOREIGN KEY(dislikingUserID) REFERENCES User (ID), \
                    FOREIGN KEY(postID) REFERENCES Post (ID), \
                    primary key(dislikingUserID, postID) )"
        self._cursor.execute(dislikeTable)

        self._commitDB()

    def _commitDB(self):
        self._con.commit()

    def __str__(self):
        return "Database"

    def getUser(self, uName, pwd):
        self._cursor.execute("select ID, password from User where userName = ?", (uName,))
        if(self._cursor == None):
            return None

        ID, password = self._cursor.fetchall()[0]

        if(password == pwd):
            return ID
        else:
            return None

    def _getUser(self, uName):

        self._cursor.execute("select ID from User where userName = ?", (uName,))
        return self._cursor.fetchall()[0][0]

    def addUser(self, uName, pwd):

        self._cursor.execute( "insert or ignore into User (userName, password) values (?,?) ", (uName,pwd) )
        self._commitDB()
        if(self.getUser(uName, pwd)):
            return True
        else:
            return False

    def _getTopic(self, tID):
        self._cursor.execute("select topicName from Topic where ID = ?", (tID,))
        result = self._cursor.fetchone()
        if(result != None):
            return result[0]
        else:
            return None

    def getTopic(self, tName):
        self._cursor.execute("select ID from Topic where topicName = ?", (tName,))
        result = self._cursor.fetchall()[0]
        if(result != None):
            return result[0]
        else:
            return None

    def addTopic(self, tName):
        self._cursor.execute("select ID from Topic where topicName = ?", (tName,))
        fetched = self._cursor.fetchall()
        if(fetched == []):
            self._cursor.execute("insert into Topic (topicName) Values (?) " ,(tName,))
            self._commitDB()
            return self._cursor.lastrowid
        else:
            return None

    def addPost(self, user, topic, post):
        uID = self._getUser(user)
        tID = self.getTopic(topic)
        if(uID == None or tID == None):
            return None
        uID = uID
        tID = tID
        self._cursor.execute("insert into Post (userID, topicID, postText, postUser, postTopic) values (?,?,?,?,?)", (uID, tID, post, user,topic))
        self._commitDB()
        return self._cursor.lastrowid

    def addLike(self, userName, postID):
        self._cursor.execute("select ID from User where userName = ?", (userName,))
        print('username: ')
        print(userName)
        if(self._cursor == None):
            return False
        userID = self._cursor.fetchall()[0][0]
        self._cursor.execute("select * from Post where ID = ?", (postID,))
        if(self._cursor == None):
            return False
        self._cursor.execute("select * from Dislike where dislikingUserID = ? and postID = ? ", (userID, postID))
        if(self._cursor.lastrowid != None):
            self.deleteDislike(userID, postID)
        self._cursor.execute("insert into Like values (?,?)", (userID,postID))
        self._commitDB()
        return True

    def deleteLike(self,userID, postID):
        self._cursor.execute("delete from Like where likingUserID = ? and postID = ? ", (userID, postID))
        self._commitDB()

    def deleteDislike(self,userID, postID):
        self._cursor.execute("delete from Dislike where dislikingUserID = ? and postID = ? ", (userID, postID))
        self._commitDB()


    def addDislike(self, userName, postID):
        self._cursor.execute("select ID from User where userName = ?", (userName,))
        if(self._cursor == None):
            return False
        userID = self._cursor.fetchall()[0][0]
        self._cursor.execute("select * from Post where ID = ?", (userID,))
        if(self._cursor == None):
            return False
        self._cursor.execute("select * from Dislike where dislikingUserID = ? and postID = ? ", (userID, postID))
        if(self._cursor.lastrowid != None):
            self.deleteLike(userID, postID)
        self._cursor.execute("insert into Dislike values (?,?)", (userID,postID))
        self._commitDB()
        return True

    def getPosts(self, topicName):
        topicID = self.getTopic(topicName)
        if(topicID == None):
            return False
        self._cursor.execute("select postText from Post where topicID = ?", (topicID,))
        if(self._cursor == None):
            return False
        rows = self._cursor.fetchall()
        ret = []
        for row in rows:
            ret.append(row)
            print(row)
        return ret

    def kill(self):
        self._con.close()
