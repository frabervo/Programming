# importing string library function 
import string 

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=str(s)
        pattern=str(pattern)
        counter=[]             # Anzahl der Character in s      / len(character)= len(counter)
        character=[]            # die vorhanden characters in s   /
        indexes=[] 
        i_indexes=[]           # Nur ein Intermediär
        iterator1=0
        words=[]
        counter_words=[]
        indexes_word=[]
        i_indexes_word=[]
        

        for index in pattern:
            if index not in character:
                character.append(index)          
                counter.append(pattern.count(index))
        #resultat: character=[a,b]  und counter=[2,2]
        # Find the indexes of a and b in s
        for index1 in range(0,len(character)):
            # index1= "a"
            for index in pattern:
                if index== character[index1]:
                    i_indexes.append(iterator1)
                iterator1 +=1
            indexes.append(i_indexes)
            iterator1 =0
            i_indexes=[]                 # i_indexes auf null setzen
        # resultat indexes=[[0,3],[1,2]]
        #print(character)
        #print(counter)
        #print(indexes)

        if len(s.split(" ")) != len(pattern):   # Enthählt s mehr wörter oder weniger als die Anzhal der Zeichen in pattern?
            #print("false S 46")
            return False
        else: 
            s=s.split(" ")
            for index in s:
                if index not in words:
                    words.append(index)
            # Ergebnis words=["dog", "cat"]
            #print(words)
            if len(words) != len(character):
                #print("false S 69")
                return False
            else:
                for index in words: 
                    print("Index: " + index)
                    counter_words.append(s.count(index))
                if counter_words !=counter:
                    print("false S 62")
                    #return False
                #result counter_words= [2,2]
                print("words: " +str(counter_words))
                # Result: s=["dog", "cat", "cat", "dog"]
                # Result: words=["dog","cat"]
                print(s)
                iterator1=0
                for index in range(0,len(words)):    #0 a 1     #index von s auslesen
                    for index1 in s:
                        # s[0]= "dog"
                        if words[index] == index1:
                            i_indexes_word.append(iterator1)
                        iterator1 +=1
                    indexes_word.append(i_indexes_word)
                    i_indexes_word=[]
                    iterator1=0
                    print("indexes_word: "+ str(indexes_word))
                if indexes_word != indexes:
                    #print("False S 98")
                    return False
                else:
                    #print("True")
                    return True
my_object=Solution()
print(my_object.wordPattern("syys", "a abc abc a"))
#my_object.wordPattern("abba", "dog cat cat dog")

