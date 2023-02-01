Using Queue:
* First, we sort the array, then start with the smallest element. It is guaranteed that the smallest element can't be a doubled value, therefore could be part of the original array.
* Once we add it to `queue`, we look for its doubled value. Any element we go over along the way that isn't the doubled value we are looking for could be part of the original array, and we add it to `stack`.
* Once we find the doubled vlaue of the smallest elemnt in the stack and so on.
* We repeat these steps for the next smallest element in the stack and so on.
* If `queue` is not empty after looping over `changed`, then some elements in `changed` didn't have a doubled value, which means `changed` is not a doubled array, therefore `res` is not a valid answer.