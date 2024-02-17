arr = []
n = int(input())
for i in range(0,n):
    ele = int(input("Enter"))
    arr.append(ele)
print(arr)

#hashing
hash = [0]*10
print(hash)
for i in range(0,n):
    hash[arr[i]] = hash[arr[i]]+1

q = int(input())
while(q != 0):
    num = int(input("Enter"))
    print(hash[num])
