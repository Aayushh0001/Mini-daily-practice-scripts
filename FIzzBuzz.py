for i in range(1,100):
    if i % 3 ==0:
        print("Fizz")
    elif i % 5 == 0 :
        print("BUzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
        