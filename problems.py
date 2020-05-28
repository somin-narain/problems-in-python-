 #find the maximum in given array a
#recurrence relation = maximum(a,i) = max(a[i],maximum(a,i-1))

def maximum(a, i):
    if i == 0:
        return a[0]
    else:
        return max(a[i], maximum(a, i - 1))


a = [4, 3, 6, 7, 0, 9, 2,12]
print(maximum(a, len(a)-1))

#given string s check if s is a paliandrome or not by writing a recursive solution 
def is_palindrome(s, i, j):
    if i >= j:
        return True
    return s[i] == s[j] and is_palindrome(s, i + 1, j - 1)


s = "xyyzzpzzyyx"
print(is_palindrome(s, 0, len(s) - 1))

'''given array m write a recursive function which checks 
if there is a sequence between the numbers for eg [1,2,3,4,5]
output slould be true because common diffrence is 1 '''

def check_sequence(nums, i):
    return i == len(nums)-1 or (nums[i] == nums[i+1]-1 and check_sequence(nums,i+1))

nums=[1,2,3,4,5,6,7,8]
print(check_sequence(nums, 0))

'''Given an intiger f return the sum of its digits for eg if 
you are give 11 output should be 2'''


def digits_sum(n):
    if n == 0:
        return 0
    return n%10 + digits_sum(int(n/10))

sum = digits_sum(11)
print(sum)

'''how to reverse a number'''
f = int(input("enter a number"))
rev = 0 
while(f>0):
	dig = f%10
	rev = rev*10+dig 
	f = f //10
print(rev)

#the star patten 
x = int(input("enter a number"))
row = 0 
while row<x:
	star = row+1 
	while star>0:
		print("*",end="")
		star = star - 1 
	row = row + 1
	print()

