#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1) this is O(1) because it is one loop that the duration of that loop
is determined by multiplying n, x number of times and if n was array it the loop would end once it has gone through all of the n elements which would then make the loop O(n).
If n = 5 this would loop would run until a is no longer less than 125


b)  for loop = O(n) n can be any value
    while loop then is O(n) n can be any value
    time complex =  O(n^2) worst case scenario

c) o(n) because of the use of recurision we don't know how many times it will recurse, it would have to depend on how many bunnies it was fed into the function it could be 1 or it could be 500

## Exercise II

The best way to find out which floor would best to drop the eggs I would use
a binary search to determine the floor. Let's say the 10 story building
I would then start at the middle of the building it would then be 5
if the threshold of broken eggs was witin limits then there's the answer otherwise it would get halved again and to 3 and check the result.
This binary search would improve the run time over doing a linear search
because of the halving. If we were to do this with a linear search it would
have to check every floor and check the result. However if I wanted to refine my binary search results to get even closer to the threshold or if it had to be spot in you could then switch to a linear search.

To answer the question of what would be the runtime complexity of the binary search it would be O(log n) since each time the floors are being halved. If we go with the linear search it would be O(n) since it goes through each floor which could be 10 stories or 500.