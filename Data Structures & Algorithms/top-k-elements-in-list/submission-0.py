class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x={}
        for i in nums:
            x[i]=x.get(i,0)+1


        z=[]
        for key,val in x.items():
            z.append([val,key])
        z.sort()
        
        res=[]
        while len(res)<k:
            res.append(z.pop()[1])
        return res