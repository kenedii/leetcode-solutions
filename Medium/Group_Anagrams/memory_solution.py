# Beats 99.41% Memory. beats 51.94% runtime
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in anagrams.keys():
                anagrams[''.join(sorted(strs[i]))] = [strs[i]]
            else:
                anagrams[''.join(sorted(strs[i]))].append(strs[i])
        return list(anagrams.values())
