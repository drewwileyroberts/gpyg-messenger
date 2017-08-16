import string
import random
import math
import sys
import os.path
import pickle

#pseudocode

def generateRSAKeys(size = 2048):
	#using OpenSSL?
	e = 0
	n = 1
	d = 2
	#write these to some log
	return (e, n, d)
	
def registerWithServer(e, n):
	#send server e, n, and the associated userID
	#get the serber e and n values too
	userID = generateRandomString(10)
	serverE = 0
	serverN = 1
	#write these to some log
	return (serverE, serverN)

def generateRandomString(length):
	characterList = string.letters + string.digits + string.punctuation
	validationMessage = ""
	for i in range(0, length):
		validationMessage = validationMessage + random.choice(characterList)
	return validationMessage

def authenticateWithServer(serverE, serverN, d, n):
	messageLength = math.ceil(random.random()*100) + 100
	message = generateRandomString(messageLength)
	mSent = message #this should be message**serverE mod serverN when actually doing it
	#send m to the server, it presumably knows serverN
	#server decrypts with (serverD, serverN) and reads the message
	#server uses our public (e, n) which it knows from registering to encrypt same message
	#server sends back to us
	mReceived = "" #this is the m sent back from the server
	#decrypt message using (d, n)
	decryptedMessage = ""
	if decryptedMessage != message:
		print "Server failed to authenticate itself. Do not trust addresses provided by this server. Exiting."
		sys.exit()
	#this process needs to be done in reverse too
	
def getAddress(userID):
	#send server of known friend, receive IP address back
	recipientIP = "0.0.0.0"
	return recipientIP

def loadFriendsList(fileName = 'friendsList.pkl'):
	friendsList = {}
	if os.path.isfile(fileName) == False:
		with open(fileName, 'wb') as f:
			pickle.dump(friendsList, f, pickle.HIGHEST_PROTOCOL)
	with open(fileName, 'rb') as f:
		friendsList = pickle.load(f)
	return friendsList
	
def saveFriendsList(friendsList, fileName = 'friendsList.pkl'):
	with open(fileName, 'wb') as f:
			pickle.dump(friendsList, f, pickle.HIGHEST_PROTOCOL)
	
	
if __name__ == '__main__':
	friendsList = loadFriendsList()
	onlineFriends = {}
	while True:
		print "\nWecome to Kevin and Drew's dope messenger. What do you want to do?"
		print "1. View online friends"
		print "2. View all friends"
		print "3. Add a friend"
		print "4. Remove a friend\n"
		optionChoice = raw_input("Type an option and press enter: ")
		if optionChoice == '2':
			for n in friendsList:
				print n
		if optionChoice == '3':
			user = raw_input("Name the user to add: ")
			e = raw_input("RSA e: ")
			n = raw_input("RSA n: ")
			friendsList[user] = (e, n)
			saveFriendsList(friendsList)
		if optionChoice == '4':
			user = raw_input("Name of the user to delete: ")
			del friendsList[user]
			saveFriendsList(friendsList)
	

	
	
	
		
	
	