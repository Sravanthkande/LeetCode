class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        
        #Assuming all ASCII Characters
        hashLen = 256

        #HashTable to store last occurance of each char
        hash = [-1] * hashLen

        #Initialize hash table with -1
        for i in range(hashLen):
            hash[i] = -1

        left, right, maxLen = 0, 0, 0
        while right < N :
            #if current char s[right] is already in the substring
            if hash[ord(s[right])] != -1:
                #move left pointer to the right
                left = max(hash[ord(s[right])] + 1, left)
            #calculate the current length
            current_len = right - left + 1

            #update maxlen found so far
            maxLen = max(maxLen, current_len)

            #Store index of the current char in the hash table
            hash[ord(s[right])] = right

            #move right pointer to next position
            right+= 1
        #return maxLen
        return maxLen
        