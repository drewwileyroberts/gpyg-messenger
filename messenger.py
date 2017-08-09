import string
import random
import math
import sys

#pseudocode

def generateRSAKeys(size = 2048):
	#using OpenSSL?
	e = 0
	n = 1
	d = 2
	#write these to some log
	return (e, n, d)
	
def registerWithServer(e, n):
	#send server e and n, since they are storing this, that can just be considered a username?
	#get their e and n values too
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
	#
	
	
	
		
	
	