""" Given an integer array nums, return all the triplets [num[i],num[j],num[k]] such that i<>j and i<>k and j<>k, and
 num[i]+num[j]+num[k]==0"""

input_num=[-1,0,1,2,-1,-4]

def _get_triplets(arr):
    triplets=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                sub_sum=[]
                sub_sum.append(arr[i])
                sub_sum.append(arr[j])
                sub_sum.append(arr[k])
                if arr[i]!=arr[j] and arr[i]!=arr[k] and arr[j]!=arr[k]:
                    sub_sum.append(arr[k])
                if sum(sub_sum)==0:
                    triplets.append(tuple(sub_sum))
                sub_sum.pop()

    return triplets
                
print(_get_triplets(input_num))