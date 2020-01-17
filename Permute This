def permuteThis(arr):
    if len(arr) == 0: 
        yield [] 
    for i in range(len(arr)):
        newArr = arr[:i] + arr[i+1:] 
        for k in permuteThis(newArr):
            yield [arr[i]] + k

ray = [0,3,9]

x = permuteThis(ray)
 
for i in x:
    print i
