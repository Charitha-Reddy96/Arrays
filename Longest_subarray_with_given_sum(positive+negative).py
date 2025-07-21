arr = [2,-1,-2,3]
n = len(arr)
maxlen = 0
k = 3
map = {}
sum =0
for i in range(n):
    sum += arr[i]
    if sum == k:
        maxlen = max(maxlen,i+1)
    rem = sum - k
    if rem in map:
        len = i - map[rem]
        maxlen = max(maxlen,len)
    if sum not in map:
        map[sum] = i     
        
print(maxlen)   

