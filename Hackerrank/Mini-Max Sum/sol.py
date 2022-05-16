def miniMaxSum(arr):
    # Write your code here
    mi = min(arr)
    ma = max(arr)
    s = sum(arr)
    print(s - ma, s - mi)