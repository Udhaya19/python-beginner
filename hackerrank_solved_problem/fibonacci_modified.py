def fibonacci_modified(t1, t2, n):
    fibbonacci_series = [t1, t2]
    for i in range(2, n):
        values = fibbonacci_series[i - 2] + (fibbonacci_series[i - 1] * fibbonacci_series[i - 1])
        fibbonacci_series.append(values)
    print(fibbonacci_series[n-1])


t1 = 0
t2 = 1
n = 5
fibonacci_modified(t1, t2, n)
