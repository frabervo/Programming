class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x2=0
        x3=0
        length=0
        zehner=10
        index=0
        if x< 0 or (x%10 ==0 and x!=0):
            return False
        if x <10: 
            return True
        if x<100:
            if int(x/10) == x%10:
                return True
            else:
                return False
        while x2!=x:
            x2= x%zehner
            zehner*=10
            length+=1
        zehner=int("1" +("0"*int(length/2)))  # zehner=1000

        while index != int(length/2):
            x2=int(x2%(zehner/10**index))
            x3=x3+ (int((x2-(x2%(zehner/(10**(index+1)))))/(zehner/(10**(index+1)))))*10**index
            index +=1
        #print(int(length/2))
        if length%2==0:
            if index==0:
                index=1 
            x2= int(x/(10**index))
            return x2==x3
        else:
            x2= int(x/(10**(index+1)))
            return x2==x3