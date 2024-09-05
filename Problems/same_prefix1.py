test_list = ['an', 'a', 'geek', 'for', 'g', 'free']
print("The original list : " + str(test_list))

res = []
visited = set()  # To keep track of items that have already been processed

compare_prefix=lambda x,y:x[0]==y[0]

for item in test_list:
    if item not in visited:
        res1 = []
        for sub_item in test_list:
            if item != sub_item and compare_prefix(item,sub_item):
                res1.append(sub_item)
        res1.append(item)
        res.append(res1)
        visited.update(res1)  # Mark all items in this group as visited

print("Grouped list : " + str(res))
