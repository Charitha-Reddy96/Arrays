#When the is asking you to print the element at place provided row and col
def ncr(r,c):
    result = 1
    for i in range(c):
        result *= r-i
        result //= i+1
    return result 
print(ncr(4,8))

#Print nth row of Pascal's Triangle
#Using above ncr function
def nth_row(n):
    result = []
    for i in range(n+1):
        result.append(ncr(n,i))
    return result
print(nth_row(4))  # Output: [1, 4, 6, 4, 1]
#Time Complexity: O(n*r)
#Space Complexity: O(n)

#Optimal Approach
def nth_row(n):
    result = [1]
    nums = 1
    for i in range(1, n):
        nums *= n - i 
        nums //= i
        result.append(nums)
    return result
#Time Complexity: O(n)
#Space Complexity: O(n)
print(nth_row(5))  # Output: [1, 4, 6, 4, 1]

#print the entire Pascal's Triangle
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        triangle.append(nth_row(i))
    return triangle

print(pascal_triangle(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
        
        
        
        
    