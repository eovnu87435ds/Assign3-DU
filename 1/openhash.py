#Michael Dornisch
#Implement Dictionary ADT (4.5-4.8) with open hash tables (fig. 4.12) for problem 1
#Verify the average number of probes required to make either a deletion or an insertion is O(1+a).
#Find best numerical constants for deletion and insertion.
import warnings #used for issuing warnings on delete/insert

class openHash(object):
    def __init__(self):
        #this is the bucket list, where data gets stored.
        self.bucketlist = [[],[],[],[],[],[],[],[],[],[]]

    def hash(self, input):
        #simple k mod m hash function. in this case k mod 10
        return(input % 10)

    def member(self, input):
        #finds hash of input, searches that bucket for input
        #returns true if found
        hashedinput = self.hash(input)
        if input in self.bucketlist[hashedinput]:
            return True
        else:
            return False

    def insert(self, input):
        #hashes the input to find bucket, appends to that specific list
        #check for membership first
        if self.member(input) == True:
            warnings.warn('Insert failed: Member already exists.')
            return
        hashedinput = self.hash(input)
        #adds the input to the correct bucket
        self.bucketlist[hashedinput].append(input)

    def delete(self, input):
        #hashes to find bucket, checks membership, deletes if exists
        if self.member(input) == False:
            warnings.warn('Delete failed: Member does not exist.')
            return
        hashedinput = self.hash(input)
        self.bucketlist[hashedinput].remove(input)

    def printTable(self):
        #prints the hash list for debug purposes
        for i in range(0,10):
            print(self.bucketlist[i])

    def makenull(self):
        #sets the bucketlist empty
        self.bucketlist = [[],[],[],[],[],[],[],[],[],[]]

"""Implementation Testing Below"""
#this inports a 1000 item long list of ints from 0-10000


ht=openHash()
print('Testing openHash ADT')
print('Inserting numbers 10-15, 20-25')
ht.insert(10)
ht.insert(11)
ht.insert(12)
ht.insert(13)
ht.insert(14)
ht.insert(15)
ht.insert(20)
ht.insert(21)
ht.insert(22)
ht.insert(23)
ht.insert(24)
ht.insert(25)
print('Checking if 13 is a member')
print(ht.member(13))
print('Deleting 13 twice in succession')
ht.delete(13)
ht.delete(13)
print('Checking if 13 is a member')
print(ht.member(13))
ht.printTable()
print('Making hash table null:')
ht.makenull()
ht.printTable()
print('populating the hashtable with 1000 items')

with open('randomlist') as f:
    inputtext = f.read().splitlines()

#print inputtext


for item in inputtext:
    ht.insert(int(item))
#ht.printTable() #this is a big table. be careful printing
