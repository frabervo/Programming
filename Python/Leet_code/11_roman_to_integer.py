class Solution(object):
    def romanToInt(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        roman= {"I":1, "V": 5, "X" : 10, "L":50, "C":100, "D": 500, "M":1000}
        int_zahl=0
        vorzahl=0
        
        for index in s: 
            if  roman[index] > vorzahl and vorzahl !=0:        # Die nächste Buchstabe ist größer als vorherige Zahl
                int_zahl= int_zahl + (roman[index] - vorzahl) -vorzahl
                vorzahl=roman[index]
            else: 
                int_zahl += roman[index]
                vorzahl=roman[index]
        return int_zahl

myobj= Solution()
roman= "XI"
print(myobj.romanToInt(roman))
