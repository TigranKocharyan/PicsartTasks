import re


arr = [9,4,9,8,4]
arr1 = [4, 9, 5, 9]
def target(lst, n):
    temp =[]
    for i in range(n):
        if i == len(lst) - 1:
            temp.append("pop")
        else:
            temp.append("push")
    return temp

def intercep(arr, arr1):
    temp = []
    for i in range(len(arr)):
        for j in range(len(arr1)):
            if arr[i] == arr1[j]:
                temp.append(arr[i])
    return list(set(temp))

def deg(arr):
    left, right, count = {}, {}, {}
    for i, x in enumerate(arr):
        if x not in left:
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1
    ans = len(arr)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)
    return ans

def sort_par(arr):
    new_arr = []
    for i in range(len(arr)):
        if i % 2 == 0:
            new_arr.insert(0, i)
        if i % 2 != 0:
            new_arr.append(i)
    return(new_arr)
def sum(arr):
    arr.sort()
    sum = 0
    for i in range( len(arr) - 1):
        if (arr[i] != arr[i + 1]):
            sum +=  arr[i]

    return sum

def target(arr, n):
    first = arr.index(n)
    last = len(arr) - 1 - arr[::-1].index(n)
    return [first, last]
print(target(arr1, 9))

def str_index(str, needle):
    return str.find(f"{needle}")
haystack = "hello"
needle = "vv"
print(str_index(haystack, needle))

def len_last(str):
    arr = str.split()
    print(len(arr[len(arr) - 1]))
len_last("jdj dncd jjffff")

def valid_palindrome(str):
   pattern = r'[^A-Za-z0-9]'
   new_str = re.sub( pattern, '', str).lower()
   if new_str == new_str[::-1]:
       return True
   else:
       return False

str = "A man, a plan, a canal: Panama"
print(valid_palindrome(str))


def numUniqueEmails(emails):
    ans = []
    for email in emails:
        acc, dom = email.split("@")
        acc = acc.split("+")[0].replace(".", "")
        ans.append(acc + "@" + dom)
    print(ans)
    return len(ans)
e = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(e))
