#Next greater element
def next_greater_element(arr):
    n=len(arr)
    stack=[]
    result=[-1]*n
    for i in range(n*2):
        print(i)
        while stack and arr[i%n] > arr[stack[-1]]:
            result[stack.pop()] = arr[i%n]
            print('Result')
            print(result)
        if (i<n):
            stack.append(i%n)
        print('Stack')
        print(stack)
    print (result)
