class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        len1 = len(word1)
        len2 = len(word2)
        result = ""

        if (len1 <= len2):              # word1 is shorter than or same length as word2
            for i in range(len1):
                result += word1[i] + word2[i]
            for j in range(len1, len2):
                result += word2[j]

            # result += word2[len1:]    # faster method using array slicing

        else:                           # word1 is longer than word2
            for i in range(len2):
                result += word1[i] + word2[i]
            for j in range(len2, len1):
                result += word1[j]

            # result += word1[len2:]

        return result