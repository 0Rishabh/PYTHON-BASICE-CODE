
# Write a Python Program for array rotation.


def rotate_arr(arr, d):
    n = len(arr) # find length of array

    if d < 0 or d >= n :
        return " Invalid Rotation value: "
    
    ro_arr = [0]*n # Create a new array to store the rotated elements.


    for i in range(n):
        ro_arr[i] = arr[(i+d)%n]

    return ro_arr

arr = [2,3,4,5,6,7,8]
d = int(input("Enter the Number of positions to rotate array: "))

result = rotate_arr(arr,d)

print("Original Array:", arr)
print("Rotated Array:", result)

