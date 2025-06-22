from typing import List


class Solution:
    def findClosestNumber(self, word1: str, word2: str) -> str:

        char = ""
        curr_word = 1
        a, b = 0, 0

        while a < len(word1) and b < len(word2):
            if curr_word == 1:
                char = char + word1[a]
                a = a+1
                curr_word = 2
            else:
                char = char + word2[b]
                b = b + 1
                curr_word = 1

        while a < len(word1):
            char += word1[a]
            a += 1

        while b < len(word2):
            char += word2[b]
            b += 1

        print(char)




Solution.findClosestNumber(None, "xyz", "abc")