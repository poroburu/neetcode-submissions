class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        result = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in result[:k]]