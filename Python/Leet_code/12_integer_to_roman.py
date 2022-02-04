class Solution(object):
    def intToRoman(self, num: int):
        """
        :type num: int
        :rtype: str
        """
        roman= {1:"I", 5:"V", 10:"X" , 50:"L", 100:"C", 500:"D", 1000:"M"}
        extra_roman={4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        zahl=""
        ziffer=0
        iterator=0
        length=0
        symbol=""
        power=0
        length2=len(str(num))
        while iterator !=length2: 
            length= len(str(num))
            power=10**(length-1)
            if length ==4:
                ziffer=int(num / power)
                num -= ziffer*(power)
                symbol=power
                zahl+=(roman[symbol])*ziffer
                iterator+=1
            else:
                ziffer=int(num / power)
                num -= ziffer*(power)
                symbol=(power)*ziffer
                if symbol in extra_roman:
                    zahl += extra_roman[symbol]
                elif symbol in roman:
                    zahl +=roman[symbol]
                else: 
                    if symbol > (5*power): 
                        zahl += roman[(5*power)] + roman[(power)]*(ziffer-5) 
                    else:
                        zahl+=(roman[power])*ziffer
                iterator+=1
        return zahl



myobj= Solution()
x=1588 
print(myobj.intToRoman(x))