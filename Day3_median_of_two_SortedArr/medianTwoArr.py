#! /usr/bin/python3

def aveOfArr(lst):
	sum = 0
	for i in lst:
		sum += i
	return sum / len(lst)

class Solution:
	def __init__(self, lst1, lst2):
		self._lst1 = lst1
		self._lst2 = lst2
	def findMedianSortedArr(self):
		sumOfTwo = aveOfArr(self._lst1) + aveOfArr(self._lst2)
		median = sumOfTwo / 2
		return median

if __name__ == "__main__":
	lst1 = [2, 3, 4]
	lst2 = [1, 2, 3]
	test = Solution(lst1, lst2)
	result = test.findMedianSortedArr()
	print(result)