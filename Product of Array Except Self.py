# import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        # print(nums[-4])
        L=[1]
        R=[1]
        Lelem=1
        for i in range(0,len(nums)-1):
            Lelem=Lelem*nums[i]
            L.append(Lelem) 
        nums.reverse()
        Relem=1
        for j in range(0,len(nums)-1):
            Relem=Relem*nums[j]
            R.append(Relem) 
        R.reverse()    
        for k in range(0,len(nums)):
            answer.append(L[k]*R[k])
        return(answer)
        
        ##Old Code
        # answer=[]
        # nums2=[]
        # for i in range(0,(len(nums))):
        #     nums2=nums
        #     numsapp=1
        #     elem=nums[i]
        #     nums2.remove(elem)
        #     for j in range(0, len(nums2)):
        #         numsapp=numsapp*nums2[j]
        #     answer.append(numsapp)
        #     nums2.insert(i,elem)
        # return answer
