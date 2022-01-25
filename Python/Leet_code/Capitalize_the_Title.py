import re
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        litle= title.split(" ")  # --> ['Ewn', 'R', 'C', 'Ho', 'O', 'Omi', 'Cgl']
        for index in range(0,len(litle)): 
            if len(litle[index])< 3:
                litle[index]=litle[index].lower()
            else:
                litle[index]=litle[index].capitalize()
                
        return ' '.join(litle)



my_obj= Solution()
title="Ewn r c ho o omi cgl"
print(my_obj.capitalizeTitle(title))