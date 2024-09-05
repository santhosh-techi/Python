test_list = ['an', 'a', 'geek', 'for', 'g', 'free','HEN']
print("The original list : " + str(test_list))
 
def util_func(x, y): return x[0] == y[0]
 
res = []
for sub in test_list:
    ele = next((x for x in res if util_func(sub, x[0])), [])
    if ele == []:
      res.append(ele)
    ele.append(sub)
 
# print result
print("The list after Categorization : " + str(res))
