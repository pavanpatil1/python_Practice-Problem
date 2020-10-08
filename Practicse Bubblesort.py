
def bubble(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0,i-n-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [10,40,1]

bubble(arr)
print "Sorted elements are.."

for i in range(len(arr)):

    print "%d" %arr[i]

