#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
Description:
Add Two Numbers

给你两个表示两个非负数字的链表。数字以相反的顺序存储，其节点包含单个数字。将这两个数字相加并将其作
为一个链表返回。

输入: (2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 0 -> 8
"""

def addTwo(arr1,arr2):
	elm1, elm2 = 0, 0
	for i in range(len(arr1)):
		elm1 += 10 ** (i) * arr1[i]
	for j in range(len(arr2)):
		elm2 += 10 ** (j) * arr2[j]
	sum = elm1 + elm2
	result = str(sum)
	rlt = []
	for i in result[::-1]:
		rlt.append(i)
	print(elm1, elm2, sum, rlt)

if __name__ == "__main__":
	arr1 = [9, 8, 7]
	arr2 = [5, 6, 4]
	addTwo(arr1, arr2)