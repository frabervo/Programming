class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <2:
            return True
        if word[0].isupper() and word[1].islower():     # Erste Groß und zweite Klein
            return word ==word.title()
        elif word == word.lower() or word==word.upper():  # entweder alles klein oder alles Groß
            return True
        else: 
            return False