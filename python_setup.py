print('Hello from inside a file!')

def hello():
    print('hello!')

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(list):
  if len(list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(list)):
      if i == 0:
        print(f"First I eat {list[0]}")
      else:
        print(f"Next I eat {list[i]}")

hello()
print(pack("a","b","c"))
eat_lunch(["fruit", "sandwich"])
