import time
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  
        left = [x for x in arr[:-1] if x <= pivot]  
        right = [x for x in arr[:-1] if x > pivot]  
        return quicksort(left) + [pivot] + quicksort(right)

def benchmark_quicksort(input_generator, sizes):
    times = []
    for size in sizes:
        arr = input_generator(size)  
        start_time = time.time()  
        quicksort(arr)  
        end_time = time.time()  
        times.append(end_time - start_time) 
    return times

def best_case_input(size):
    return list(range(size))  

def worst_case_input(size):
    return list(range(size, 0, -1))  

def average_case_input(size):
    return [random.randint(0, 1000) for _ in range(size)]  

def plot_benchmarks(sizes, best_times, worst_times, avg_times):
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes, best_times, label='Best Case (Sorted Array)', marker='o', color='green')
    plt.plot(sizes, worst_times, label='Worst Case (Reverse Sorted Array)', marker='o', color='red')
    plt.plot(sizes, avg_times, label='Average Case (Random Array)', marker='o', color='blue')
    
    plt.title('Quicksort Benchmark Performance')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    
    plt.legend()
    plt.grid(True)
    
    plt.show()

sizes = [50, 100, 300, 500, 700, 1000, 1500, 2000]

best_times = benchmark_quicksort(best_case_input, sizes)
worst_times = benchmark_quicksort(worst_case_input, sizes)
avg_times = benchmark_quicksort(average_case_input, sizes)

plot_benchmarks(sizes, best_times, worst_times, avg_times)
