
def reverse_int(n:list):
    return [int(str(i)[::-1]) for i in n]

print(reverse_int([35, 46, 57, 91, 29]))