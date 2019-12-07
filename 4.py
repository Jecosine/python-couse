
nums = {1:1,2:1}
def fibo(n):
    global nums
    if nums.get(n):
        return nums[n]
    if n == 0:
        return 0 
    s, t = fibo(n - 1), fibo(n - 2)   
    nums[n - 1] = s
    nums[n - 2] = t
    return s + t

if __name__ == "__main__":
    nums[20] = fibo(20)
    for i in range(20):
        print(str(nums[i+1]) + " ",end="")