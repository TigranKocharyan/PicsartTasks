def square_of_sum():
    count = 0
    for i in range(100):
        count += i
    return count**2
def sum_of_squares():
    count = 0
    for i in range(100):
        count+= i**2
    return count
print(square_of_sum() - sum_of_squares())


Input = open("test.txt", "r").readlines()
Output = open("test1.txt", "w")
for Line in Input:
    arr = Line.split(",")
    print(arr)
    for i, el in enumerate(arr):
        arr[i] = el.replace('"', '')
    for i, el in enumerate(arr):
        arr[i] = el.capitalize()
    s = str(arr).replace("["  , "").replace("]", "")
Output.write(s)

def is_palindrom(n):
    s = str(n)
    if s == s[::-1]:
        print("True")
    else:
        print("False")






























