With the brute force approach, we need to run a nested for loop to find the next greatest element in the parent array.
​
With the 1st optimal solution, we can use hashmap to keep track of the element and their respective indices. So that, whenever, we find the next greatest element, we can put it in it approciate index.
​
```
nums1Idx = {n:i for i, n in enumerate(nums1)}
res = [-1] * len(nums1)
for i in range(len(nums2)):
if nums2[i] not in nums1Idx:
continue
for j in range(i+1, len(nums2)):
if nums2[j] > nums2[i]:
idx = nums1Idx[nums2[i]]
res[idx] = nums2[j]
break
return res
```
​
**The time complexity is O(n * m).**
​
**The memory complexity is O(m) because we will have a hashmap for the subset array.**
​
### Best Solution
​
#### Using monotonic descreasing stack
Time complexity is O(m+n)
Space complexity is O(m)
​
​
​
[Neetcode Solution](http://www.youtube.com/watch?v=68a1Dc_qVq4&ab_channel=NeetCode)