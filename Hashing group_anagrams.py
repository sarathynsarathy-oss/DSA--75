# LeetCode 49: Group Anagrams
# Difficulty: Medium
# Topic: Hashing, Sorting

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
