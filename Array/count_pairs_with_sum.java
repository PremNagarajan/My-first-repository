/*
Count pairs with given sum

Given an array of integers, and a number ‘sum’,
find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Below is the Algorithm.

1) Create a map to store frequency of each number in the array.

2) In the next traversal, for every element check if it can be combined with
any other element (other than itself!) to give the desired sum.
Increment the counter accordingly.

3) After completion of second traversal, we’d have twice the required value
stored in counter because every pair is counted two times.
Hence divide count by 2 and return.

*/

class Solution {
    static int countPairs(int sum, int[] arr) {
		int n = arr.length;
		HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
 
		int res = 0;
 
		for(int i=0;i<n;i++) {
			if(hm.containsKey(arr[i])) {
				int c = hm.get(arr[i]); 
				hm.put(arr[i],c+1);
			}
			else
				hm.put(arr[i],1);
		}
 
		int twiceCount = 0;
		for(int i=0;i<n;i++) {
			if(hm.get(sum-arr[i]) != null) {
				twiceCount += hm.get(sum-arr[i]); 
				if(sum-arr[i] == arr[i])
					twiceCount--;
			}
		}
 
		return twiceCount/2;
	}

}