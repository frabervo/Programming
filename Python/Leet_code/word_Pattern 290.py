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
        stop =0
        counter=[]             # Anzahl der Character in s      / len(character)= len(counter)
        character=[]            # die vorhanden characters in s   /
        indexes=[] 
        i_indexes=[]           # Nur ein Intermediär
        iterator1=0
        words=[]
        i_words=[]
        counter_words=[]
        indexes_word=[]
        i_indexes_word=[]
        
        if len(pattern) >= 1 or len(pattern)<= 300 or (pattern.startswith(" ") or pattern.endswith(" ")):     # Wort-Länge überprüfen
            if s.startswith(" ") or s.endswith(" ") or len(s) <1 or len(s)> 3000:  # S überprüfen länge, anfang und ende
                stop=1
            for index in s:                         # S länge überprüfen
                if index not in string.ascii_lowercase and index !=" ":
                    stop=1
                    break
            if not stop:
                if pattern.startswith(" ") or pattern.endswith(" "):
                    return False
                for index in pattern: 
                    if index not in string.ascii_lowercase:     # Beinhaltet Großbuchstabe oder Zahlen --> Stop                    
                        break                               # Wenn Break aus wird else nicht ausgeführt 
                else:
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
                        #print("false")
                        return False
                    else: 
                        i_words=s.split(" ")
                        for index in i_words:
                            if index not in words:
                                words.append(index)
                        # Ergebnis words=["dog", "cat"]
                        if len(words) != len(character):    #Anzahl der einzelnen Wöter in s nicht gleich Anzahl der einzelnen Zeichen in s
                            #print("false")
                            return False
                        else:
                            for index in words: 
                                counter_words.append(s.count(index))
                            if counter_words !=counter:     # Wiederholungen nicht gleich
                                #print("false")
                                return False
                            #result counter_words= [2,2]
                            for index in words:
                                s=s.replace(index, index[0])
                                s=s.replace(" ","")
                            #print(s)
                            #result s="dccd"
                            i_words= []
                            iterator1=0
                            for index in s: 
                                if index not in i_words:
                                    i_words.append(index)
                            #print(i_words)
                            # resul i_words=["d","c"]
                            for index in range(0,len(i_words)):   #0 a 1
                                for index1 in s:        # s="dccd" 
                                    if index1== i_words[index]:
                                        i_indexes_word.append(iterator1)
                                    iterator1 +=1
                                indexes_word.append(i_indexes_word)
                                i_indexes_word=[]
                                iterator1=0
                            # Result [[0,3],[1,2]]
                            if indexes_word != indexes:
                                #print("False")
                                return False
                            else:
                                #print("True")
                                return True

        else: 
            #print("Nichts machen")
            return False


