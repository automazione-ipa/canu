def fibonacci(n):
    a, b = 0, 1
    for index in range(n):
        print(a, end=" ")
        a, b = a + b, a

fibonacci(10)