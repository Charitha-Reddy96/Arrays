arr = [2,-1,-2,3]
n = len(arr)
maxlen = 0
k = 3
sum =0
i = j =0
while((i>=j) and i<n):
    sum += arr[i]
    if sum > k:
        sum -= arr[j]
        j+=1
    if sum == k:
        maxlen = max(maxlen,i-j+1)

    i+=1
print(maxlen)
    
    