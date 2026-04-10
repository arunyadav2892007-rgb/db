# i=[6,7,8,9,70]

# for j in range (0,len(i)):
#     if i[j]%2==0:
#         print("evren",j)
#     else:
#         print("odd",j)

# l = [1, 2, 3, 4]
# r = []

# for i in range(len(l)):
#     p = 1
#     for j in range(len(l)):
#          if i != j:
#             p *= l[j]
#     r.append(p)

# print(r)

#  l=[1,2,3,4,5,6,7,8]
#  for i in range(0,len(l)):
#      for j in range(0,len(l)):
#          if l[i]>l[j]:
#              x=i
#  print(x,"is the greatest")
# l = [3, 12, 9, 16, 18, 7, 8]

# largest = second_largest = -1

# for num in l:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Second largest element:", second_largest)
# 

# x = int (input("Enter an integer: "))
# result = []
# for i in range(1, x + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         result.append("FizzBuzz")
#     elif i % 3 == 0:
#         result.append("Fizz")
#     elif i % 5 == 0:
#         result.append("Buzz")
#     else:
#         result.append(str(i))
# print(result)

# l=[1,4,4,5,6]
# set={}
# for i in l:
#     if i in set:
#        return True
#     else:
#         set.add(i)
#         return False


# l=[2,3,4,5,6,6,3,3]
# for i in range(0,len(l)):
#      for J in range(0,len(l)):
#          if l[i]+l[J] ==6:
#              x=i
#              y=J
# print(x,y)
# l2=[]
# l=[2,3,4,5,6,6,3,3]
# mp={}
# for i in range(len(l)):
#     val= 6-l[i]
#     if val in mp:



#      l2.append(mp[l[i]])
#      l2.append(i)


#     else:
#       mp[l[i]]=i
# print(l2)


# s="anagram"
# l="nagaram"
# for i in range(0,len(s)):
#     for j in range(0,len(l)):
#         if s[i]==l[j] and s.count(i)==l.count(j):
#             print("amalgrem")
#         else:
#             print("not amalgrem")

# l="gyg"
# d="ygg"
# mp={}
# for i in l:
#     mp[i]=mp.get(i,0)+1
# for i in d:
#     if i not in mp:
#         return False
#     mp[i]-=1
# for i in mp:
#     if mp[i]!=0:
#         return False
#     return True
# l="uihygu"
# for i in range(0,len(l)):
#     x=l.count(i)
# if x<2:
#     print(i,"unique")
# else:
#     print("-1")
# l1=[]  
# l=[1,2,3]
# s=0
# for i in l:
#     s*=10
#     s+=i
# s+=1
# while s>0:
#     var=s%10
#     l1.append(var)
#     s/=10
# n = 3
# m = 3
# AIML = []
# for i in range (n):
#     row = []
    
#     for j in range (m):
#         var = (int(input("Enter your mark: ")))
#         row.append(var)
#     AIML.append(row)
# print(AIML)


    



# for i in range (n):
#     for j in range (m):
#         print(AIML[i][j], end = " ")
#     print()
# for i in range(N):
#     sum=0
#     for j in range(m):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print(aiml[i][j],end="")
#         else:
#             print(end="")
#     print()
# r=int(input("enter"))
# c=int(input("rntr"))
# L=[]
# M=len(AIML)
# N=len(AIML[0])
# if M*N!=r*c:
#     print(AIML)
# L=[]   


    
# for i in range(M):
        
#     for j in range(N):
#         L.append(AIML[i][j])
# res=[]
# k=0
# for i in range(r):
#     l1=[]
#     for j in range(c):
#         l1.append(L[k])
#         k+=1
#     res.append(l1)
# print(res)

# n=124
# temp = n
# s = 0
# while temp > 0:
#     d = temp % 10
#     p = 1
#     i = 0
#     while i <3:
#         p *= d
#         i += 1
#     s += p
#     temp//=10
# print(s)


# n = 1234
# digits = []

# while n > 0:
#     digits.append(n % 10)
#     n //= 10



# a=0
# b=1
# for i in digits:
#     a=a+i
#     b=b*i
# print(a,b)
# class Node:
#      def __init__(self,data = None, next = None):
#          self.data = data
#          self.next = next
# class LinkedList:
#      def __init__(self, head = None):
#          self.head = head
#      def insert_at_begining(self, data):
#          new_node = Node(data, self.head)
#          new_node.next = self.head
#          self.head = new_node

#      def insert_at_end(self, data):
#          new_node = Node(data)
#          temp = self.head
#          while temp.next:
#              temp = temp.next
#          temp.next = new_node
#      def display(self):
#          temp = self.head
#          while temp:
#              print(temp.data, end = " -> ")
#              temp = temp.next
#          print("None")


#      def del_at_end(self):
#        temp=self.head
#        if not temp:
#          return
#        if temp.next in None:
#         self.head=None
#         return
#        while temp.next.next:
#         temp=temp.next


#        temp.next=None
#      def del_at_begning(self):
#       if not self.head:
#         return
#       if not self.head.next:
#         self.head=None
#         return
#       self.head=self.head.next
# l1 = LinkedList()
# l1.insert_at_begining(10)
# l1.insert_at_begining(20)
# l1.insert_at_end(30)
# l1.insert_at_end(40)
# l1.display()

# class Node:
#     def __init__(self, data = None, next = None, prev = None):
#         self.data = data
#         self.next = next
#         self.prev = prev

# class DLL:
#     def __init__(self, head = None):
#         self.head = head

#     def insert_at_Beginning(self,data):
#         new_nose = Node(data)
#         if self.head is None:
#             self.head = None
#             self.head = new_node
#             return

#     def insert_at_PQS(self,data,val):
#         if self.head is None:
#             self.head.next = new_node
#             new_node.prev = self.head


#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end = " <-> ")
#             temp = temp.next
#             print("None")
# s="()"
# if len(s)<1 and len(s)%2==0:
#     print("false")
# st=[]
# for i in range (len(s)):
#     if s[i]=="(" and s[i]=="{" and s[i]=="[":
#         st.push(s)
#     elif !st.empty() and s[i]=="}":
#         if st.top=="{":
#             st.pop()
#         else:
#             print("false")
#     elif !st.empty() and s[i]=="]":
#         if st.top=="[":
#             st.pop()
#         else:
#             print("false")
#     elif !st.empty() and s[i]==")":
#         if st.top=="(":
#             st.pop()
#         else:
#             print("false")
# current=head
# while current is not None
# l1+=1
# current=current.next
# current=head
# l1=l1//5
# class ListNode(object):
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next


# class Solution(object):
#     def middleNode(self, head):
#         fast=head
#         slow=head
#         while fast and fast.next:
#             fast=fast.next.next
#             slow=slow.next
#         return slow

# class ListNode(object):
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next


# class Solution(object):
#     def middleNode(self, head):
#         fast=head
#         slow=head
#         while fast and fast.next:
#             fast=fast.next.next
#             slow=slow.next
#             if fast==slow:
#                 return True
#         return False

# l=[1,2,2,1]
# s=len(l)
# for i in range(0,s+1):
#     for j in range(-1,-s):
#         if l[i]==l[j]:
#             print("ispallinrome")
#         else:
#             print("notpalindrome")

# class Solution(object):
#     def isPalindrome(self, head):
#         fast=head
#         slow=head
#         while fast and fast.next:
#             fast=fast.next.next
#             slow=slow.next
#         temp=None
#         prev=None
#         while slow:
#             temp=slow.next
#             slow.next=prev
#             prev=slow
#             slow=temp
#             fast=head
#             while prev:
#                 if prev.val!=fast.val:
#                     return False
#                 fast=fast.next
#                 slow=slow.next
#         return True


#         """
#         :type head: Optional[ListNode]
#         :rtype: bool
#         """
    #  dummy=ListNode(0)
    #     dummy.next=head
    #     c=0
    #     curr=head
    #     while curr:
    #         c+=1
    #         curr=curr.next
    #     curr=head
    #     temp=dummy
    #     while c>n:
    #         temp=curr
    #         curr=curr.next
    #         c-=1
    #     temp.next=curr.next
    #     return dummy.next
#  e=headA
#         j=headB
#         while e!=j:
#             if e==None:
#                 e=headB
#             else:
#                 e=e.next
#             if j==None:
#                 j=headA
#             else:
#                 j=j.next
#         return e
# target=5
# l=[1,2,3,4,5,6,7]
# c=0
# h=len(l)-1
# while c<=h:
#     mid=(1+h)//2
#     if l[mid]==target:
#         print(mid)
#     elif l[mid]<target:
#         c=mid+1
#     else:
#         h=mid-1
# print(c)

# n=len(nums):
# for i in range(n):
#     for j in range(n-i-1):
#         if nums[i]>nums[i+1]:
#             nums[i+1],nums[i]=nums[i],nums[i+1]




# def concour(nums1,nums2):
#     l1=[]
#     while i<len(nums1) and j<len(nums2):
#         if nums1[i]< nums2[j]:
#             l1.append(nums1[i])
#             i+=1
#         else:
#             l1.append(nums2[j])
#             j+=1
#     l1.append(nums1[:i])
#     l1.append(nums2[j:])

# l=[6,7,8,5,4,0,8,9]
# if len(l)<=1:
#     print(l)
# mid=len(l)//2
# n=l[:mid]
# m=l[mid:]
# x=concour(n,m)
# print(x)
# l=[8,9,7,6,5,0,4,2]
# n=len(l)
# for i in range (n):
#     min=i
#     for j in range(i+1,n):
#         if l[j]<l[min]:
#             min=j
#     l[i],l[min]=l[min],l[j]


# root=Node(1)
# root.left=Node(3)
# root.left.left=node()

def preorder(self,root):
    l=[]
self.traverse(root,l)


def traverse(self,root,l)
    if root is none:
        return
    l.append(root.val)
self.traverse(root.left,l)
self.traverse(root.right,l)



def traverse(self,root,l)
    if root is None
      return
self.traverse(root.left,l)
l.append(root.val)
self.traverse(root.right,l)
94,144,145





