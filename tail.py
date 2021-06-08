from collections import deque
def tail_fn(filename,n):
    with open(filename) as f:
        return list(deque(f,n))

with open("file1.txt","w") as f:
    for i in range(100):
        f.write(f"This is line number {i}\n")
print(tail_fn("file1.txt",20))
