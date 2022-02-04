class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=""
        iterator=0
        vor_prefix=""

        for letter in strs[0]:
            vor_prefix += letter
            for word in strs[1:]: 
                if word.startswith(vor_prefix):
                    iterator +=1
            if iterator == len(strs[1:]):
                prefix=vor_prefix
            iterator =0

        return prefix
# oder 
""" 
def longestCommonPrefix( a):
	
	size = len(a)

	# if size is 0, return empty string
	if (size == 0):
		return ""

	if (size == 1):
		return a[0]

	# sort the array of strings
	a.sort()
	
	# find the minimum length from
	# first and last string
	end = min(len(a[0]), len(a[size - 1]))

	# find the common prefix between
	# the first and last string
	i = 0
	while (i < end and a[0][i] == a[size - 1][i]):
		i += 1

	pre = a[0][0: i]
	return pre

# Driver Code
if __name__ == "__main__":

	input = ["flower","flow","flight"]
	print("The longest Common Prefix is :" , longestCommonPrefix(input))

# This code is contributed by ita_c

"""

# oder
                    