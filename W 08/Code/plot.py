import matplotlib.pyplot as plt
import cutrod
import time

# function to calculate execution time
def calculate_execution_time(function, p, n):
    start_time = time.time()
    function(p, n)
    end_time = time.time()
    return end_time - start_time

price_list = [24, 10, 9, 3, 17, 1, 8, 5, 2, 9, 10, 1, 17, 5, 17, 9, 3, 7, 11, 18, 4, 20, 5, 8, 1, 2, 9, 30, 17]
rod_length = 25
rod_lengths = list(range(1, rod_length + 1))
recursive_times = []
memoized_times = []
bottom_up_times = []

# calculating execution times for the 3 approaches
for length in rod_lengths:
    recursive_time = calculate_execution_time(cutrod.cut_rod, price_list, length)
    memoized_time = calculate_execution_time(cutrod.cut_rod_memoize, price_list, length)
    bottom_up_time = calculate_execution_time(cutrod.cut_rod_bottom_up, price_list, length)

    recursive_times.append(recursive_time)
    memoized_times.append(memoized_time)
    bottom_up_times.append(bottom_up_time)

# plotting the results
plt.plot(rod_lengths, recursive_times,  linestyle='-', label='Top-down Recursive')
plt.plot(rod_lengths, memoized_times,  linestyle='-', label='Top-down Memoized')
plt.plot(rod_lengths, bottom_up_times, linestyle='-', label='Bottom-up')

# labelling the figure with relevant labels
plt.xlabel('Rod Length (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Running Time of Rod-Cutting Algorithms')
plt.legend()
plt.grid(True)
plt.show()

