#Michael Dornisch
#Implement Dictionary ADT (4.5-4.8) with open hash tables (fig. 4.12) for problem 1
#Verify the average number of probes required to make either a deletion or an insertion is O(1+a).
#Find best numerical constants for deletion and insertion.
import warnings #used for issuing warnings on delete/insert
import random

class openHash(object):
    def __init__(self):
        #this is the bucket list, where data gets stored.
        self.bucketlist = [[],[],[],[],[],[],[],[],[],[]]
        self.inserts = 0;
        self.insertprobes = 0;
        self.deletes = 0;
        self.deleteprobes = 0;

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
        self.insertprobes = self.insertprobes + len(self.bucketlist[hashedinput])
        self.inserts = self.inserts + 1

    def delete(self, input):
        #hashes to find bucket, checks membership, deletes if exists
        if self.member(input) == False:
            warnings.warn('Delete failed: Member does not exist.')
            return
        hashedinput = self.hash(input)
        self.deletes = self.deletes + 1
        self.deleteprobes = self.deleteprobes +  1 + self.bucketlist[self.hash(input)].index(input)
        self.bucketlist[hashedinput].remove(input)


    def printTable(self):
        #prints the hash list for debug purposes
        for i in range(0,10):
            print(self.bucketlist[i])

    def makenull(self):
        #sets the bucketlist empty
        self.bucketlist = [[],[],[],[],[],[],[],[],[],[]]
        self.inserts = 0;
        self.insertprobes = 0;
        self.deletes = 0;
        self.deleteprobes = 0;

    def statistics(self):
        print("number of inserts: " + str(self.inserts))
        print("number of deletes: " + str(self.deletes))
        print("number of insert probes: " + str(self.insertprobes))
        print("number of delete probes: " + str(self.deleteprobes))
        print("average probes on insert: " + str(self.insertprobes / self.inserts))
        print("average probes on delete: " + str(self.deleteprobes / self.deletes))

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
print('Checking if 13 is a member')
print(ht.member(23))
ht.printTable()
print("Statistics on small operation:")
ht.statistics()
print('Making hash table null:')
ht.makenull()
ht.printTable()
print('populating the hashtable with 1000 items')
print

with open('randomlist') as f:
    inputtext = f.read().splitlines()

#print inputtext


for item in inputtext:
    ht.insert(int(item))
print
print('Shuffling the input list, deleting 1000 items from hashtable')
print
random.shuffle(inputtext)
for item in inputtext:
    ht.delete(int(item))
print
print("Statistics on 1000 count operation:")
ht.statistics()

#ht.printTable() #this is a big table. be careful printing
