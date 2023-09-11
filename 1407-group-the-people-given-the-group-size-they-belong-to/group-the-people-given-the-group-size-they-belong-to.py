from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashm = defaultdict(list)
        for i, g in enumerate(groupSizes):
            hashm[g].append(i)
        final_ans = []
        for groupSize in hashm.keys():
            people = hashm[groupSize]
            num_people = len(people)
            for i in range(0, num_people, groupSize):
                final_ans.append(people[i:i+groupSize])
        return final_ans

        