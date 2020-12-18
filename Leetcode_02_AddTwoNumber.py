#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:31:06 2020

@author: yangsong
"""

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total=ListNode(0)
        s=total
        y=0
        
        while l1 != None or l2 != None or y:
            s.val=y
            if l1:
                s.val+=l1.val
                l1=l1.next
            if l2:
                s.val+=l2.val
                l2=l2.next
              
            y=s.val//10
            s.val=s.val%10


            if l1 or l2 or y:
                s.next = ListNode(0)
                s = s.next

        return(total)