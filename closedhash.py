import warnings
import random

class closedHash(object):
    def __init__(self):
        #this is the bucket list, where data gets stored.
        #using list of lists because python doesn't do fixed length arrays
        self.buckets = [[],[],[],[],[],[],[],[],[],[]]
        self.inserts = 0;
        self.insertprobes = 0;
        self.deletes = 0;
        self.deleteprobes = 0;

    def hash(self, input):
        #simple k mod m hash function. in this case k mod 10
        return(input % 10)

    def printTable(self):
        #prints the hash list for debug purposes
        for i in range(0,10):
            print(self.buckets[i])

    def makenull(self):
        #sets the bucketlist empty
        self.buckets = [[],[],[],[],[],[],[],[],[],[]]
        self.inserts = 0;
        self.insertprobes = 0;
        self.deletes = 0;
        self.deleteprobes = 0;

    def member(self, input):
        #this 'could' just check the buckets in order, but hashing
        #can optimize this
        hashedinput = self.hash(input)
        currentBucket = hashedinput #just a copy that we can modify
        for i in range(0,10):
            #try used here to handle IndexError exceptions.
            #an empty list obviously doesn't have the input in it
            try:
                if self.buckets[currentBucket][0] == input:
                    return True
            except IndexError:
                #print "error" + str(input) + " " + str(hashedinput)
                pass
            continue
            currentBucket = currentBucket + 1
            currentBucket = currentBucket % 10
        return False

    def insert(self, input):
        hashedinput = self.hash(input)
        if self.member(input) == True:
            warnings.warn('Insert failed: Member already exists.')
            return
        #this is the actual insert function. It checks to see if
        #the necessary bucket is empty. if it is, it adds the input.
        #if it is not empty, it checks the next bucket, with list
        #wrapping (see the mod 10 line). If after trying all buckets it
        #does not find an empty one, it returns an error.
        currentBucket = hashedinput
        probecount = 0
        for i in range(0,10):
            probecount = probecount +1
            if len(self.buckets[currentBucket]) == 0:
                self.buckets[currentBucket].append(input)
                self.insertprobes = self.insertprobes + probecount
                self.inserts = self.inserts + 1
                return
            currentBucket = currentBucket + 1
            currentBucket = currentBucket % 10

        warnings.warn('Insert Failed: Closed hash table full.')
        return

    def delete(self, input):
        if self.member(input) == False:
            warnings.warn('Delete failed: Member does not exist.')
            #print("fail")
            return
        hashedinput = self.hash(input)
        currentBucket = hashedinput
        probecount = 0
        for i in range(0,11):
            #print currentBucket
            probecount = probecount + 1
            if self.buckets[currentBucket][0] == input:
                self.deletes = self.deletes + 1
                self.deleteprobes = self.deleteprobes + probecount
                self.buckets[currentBucket].remove(input)
                return
            currentBucket = currentBucket + 1
            currentBucket = currentBucket % 10



ch = closedHash()
inputlist = []
for i in range(0,10):
    inputlist.append(random.randint(1,255))
    #inputlist.append(6*i)
print("Randomized List for testing: ")
print inputlist
print("Inserting items...")
for item in inputlist:
    ch.insert(item)
ch.printTable()
print("Shuffling list for deletions:")
random.shuffle(inputlist)
print inputlist
print("Deleting items...")
for item in inputlist:
    ch.delete(item)
ch.printTable()
print
ch.delete(30)
#ch.printTable()
