import itertools
anagrams = [("angel","glean"),("brag","grab"),("bored","robed"),("cat","act"),("cider","cried"),
    ("dusty","study"),("elbow","below"),("inch","chin"),("night","thing"),("peach","cheap"),
    ("players","parsley"),("sadder","dreads"),("save","vase"),("state","taste"),("listen","silent"),
    ("atom","bomb"),("meals","males"),("saint","satin"),("avenge","Geneva"),("meals","Salem"),
    ("sales","seals"),("balm","lamb"),("mean","mane"),("salts","lasts"),("blot","bolt"),
    ("sharp","harps"),("brag","grab"),("more","Rome"),("shrub","brush"), ("limped","dimple")]

anagrams2 = [("angel","glean"),("brag","grab"),("bored","robed"),("cat","act"),("cider","cried"),
("dusty","study"),("elbow","below"),("inch","chin"),("night","thing"),("peach","cheap"),
("players","parsley"),("sadder","dreads"),("save","vase"),("state","taste"),("listen","silent"),
("atom","bomb"),("meals","males"),("saint","satin"),("avenge","Geneva"),("meals","Salem"),
("sales","seals"),("balm","lamb"),("mean","mane"),("salts","lasts"),("blot","bolt"),
("sharp","harps"),("brag","grab"),("more","Rome"),("shrub","brush"), ("limped","dimple"),
("courtmartial","matriculator"),("triangulated","adulterating"),("reoccupation","cornucopiate"),
("preeducation","deuteranopic"),("declinations","nondeistical"),("tropicalised","prediastolic"),
("tracheophyte","hypothecater"),("sectionalise","nesosilicate"),("stereoptican","inspectorate"),
("replications","inspectorial"),("semiromantic","cremationism"),("miscreations","romanticises"),
("incorporates","procreations"),("disagreement","demagnetiser"),("mountaineers","enumerations"),
("remonstrates","reassortment"),("germinations","anti-Negroism"),("strontianite","interstation"),
("technetronic","ethnocentric"),("mediocrities","iridectomise"),("computerised","pseudometric"),
("cryptotermes","spectrometry"),("limnocryptes","polycentrism"),("identifiably","definability"),
("nondialectic","coincidental"),("subtractions","obscurantist"),("nonuniversalist","involuntariness"),
("stationarily","antiroyalist"),("basiparachromatin","marsipobranchiata"),("thermonastically","hematocrystallin"),
("refragmentation","antiferromagnet"),("megachiropteran","cinematographer"),("centauromachias","marchantiaceous"),
("protuberantial","perturbational"),("proletarianize","prerealization"),("undefinability","unidentifiably"),
("interrogatives","reinvestigator"),("nitromagnesite","regimentations"),("rotundifoliate","titanofluoride"),
("undemocratise","documentaries"),("thysanopteran","parasyntheton"),("suprarational","pro-Australian"),
("unmaledictory","documentarily"),("recreationist","contrarieties"),("pictorialness","personalistic"),
("superintended","unpredestined"),("cameralistic","acclimatiser"),("declamations","anecdotalism"),
("pharmacolite","metaphorical"),("manometrical","commentarial"),("spectatorial","poetastrical")]

def isAnagram_exhaustive(word1, word2):
    '''
       Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.
    '''
    count=0
    i=0
    word1=word1.lower()
    word2=word2.lower()
    if word1==word2 or len(word1)!=len(word2) or len(word1)==0 or len(word2)==0:
        return False
    permutations = list(itertools.permutations(word1))
    while(i<len(permutations)):
        if permutations[i]==tuple(word2):
            count+=1
        i+=1
    if count>0:
        return True
    else:
        return False

def isAnagram_checkoff(word1, word2):
    '''
      Create a parallel array-based version of the second word (strings are immutable).
      Check off letters in the array as they are found by setting the value to None.
    '''
    word1=word1.lower()
    word2=word2.lower()
    if word1==word2 or len(word1)!=len(word2) or len(word1)==0 or len(word2)==0:
        return False
    word1=list(word1)
    word2=list(word2)
    for i, letter1 in enumerate(word1):
        if letter1 in word2:
            word1[i]=None
    print(word1)
    print(word2)
    if word1==[None]*len(word1):
        return True
    else:
        return False

def isAnagram_lettercount(word1, word2):
    '''
      Create two arrays of 26 spots to keep track of letter counts in each word.
      [0] represents the letter a, [1] represents the letter b, and so on…
      Compare final versions of each array to determine if the words are anagrams.
    '''
    count1=[0]*26
    count2=[0]*26
    word1=word1.lower()
    word2=word2.lower()
    if word1==word2 or len(word1)!=len(word2) or len(word1)==0 or len(word2)==0:
        return False
    for i in word1:
        count1[ord(i) - 97]+=1  #3
    for i in word2:
        count2[ord(i) - 97]+=1
    if count1==count2:
        return True
    else:
        return False

def isAnagram_sort(word1, word2):
    '''
      Sort both words, then compare to see if they are exactly the same.
    '''
    word1=word1.lower()
    word2=word2.lower()
    x=sorted(word1)
    y=sorted(word2)
    i=0
    if word1==word2 or len(x)!=len(y) or len(x)==0 or len(y)==0:
        return False
    while(i<len(x)):
        if x[i]!=y[i]:
            return False
        i+=1
    return True

def isAnagram_prime(word1, word2):
    '''
      Create an array of prime numbers. Use the ascii value of each letter in both
      words to construct a unique hash (). Words with the same hash value are anagrams
      of each other.
    '''
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    prime1=1
    prime2=1
    word1=word1.lower()
    word2=word2.lower()
    if word1==word2 or len(word1)!=len(word2) or len(word1)==0 or len(word2)==0:
        return False
    for i in word1:
        x=primes[ord(i) - 97]
        prime1*=x
    for i in word2:
        y=primes[ord(i) - 97]
        prime2*=y
    if prime1==prime2 and prime1!=1 and prime2!=1:
        return True
    else:
        return False

if __name__ == "__main__":
    labels=[ "Exhaustive", "Checkoff", "Lettercount", "Sort", "Prime"]
    algorithms=[ isAnagram_exhaustive, isAnagram_checkoff, isAnagram_lettercount, isAnagram_sort, isAnagram_prime]
    word1 = "All"
    word2 = "Lal"
    for i, anagramAlgorithm in enumerate(algorithms):
        print("Strategy:"+labels[i]+"- "+word1+", "+word2+": "+str(anagramAlgorithm(word1, word2)))
