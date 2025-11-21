import time
import random
import matplotlib.pyplot as plt
from select_algorithms import median_of_medians, randomized_select


# --------------------------------------------------------------
# Helper Function: Measure time
# --------------------------------------------------------------

def time_algorithm(func, arr, k):
    start = time.perf_counter()
    func(arr.copy(), k)  # use arr.copy() so original is untouched
    return time.perf_counter() - start


# --------------------------------------------------------------
# Generate test arrays
# --------------------------------------------------------------

def generate_arrays(n):
    return {
        "random": [random.randint(0, 10_000) for _ in range(n)],
        "sorted": list(range(n)),
        "reverse": list(range(n, 0, -1)),
        "duplicates": [random.choice([1,2,3,4,5]) for _ in range(n)]
    }


# --------------------------------------------------------------
# Experimental setup
# --------------------------------------------------------------

def run_experiments():
    sizes = [100, 500, 1000, 2000, 5000]
    distributions = ["random", "sorted", "reverse", "duplicates"]

    results = {d: {"det": [], "rand": []} for d in distributions}

    for n in sizes:
        print(f"\nRunning experiments for n = {n}")
        arrays = generate_arrays(n)
        k = n // 2  # median

        for dist in distributions:
            print(f"  Testing {dist} distribution...")

            arr = arrays[dist]

            # Deterministic
            t_det = time_algorithm(median_of_medians, arr, k)
            results[dist]["det"].append(t_det)

            # Randomized
            t_rand = time_algorithm(randomized_select, arr, k)
            results[dist]["rand"].append(t_rand)

            print(f"    Deterministic: {t_det:.6f} sec")
            print(f"    Randomized:    {t_rand:.6f} sec")

    return sizes, results


# --------------------------------------------------------------
# Plotting
# --------------------------------------------------------------

def plot_results(sizes, results):
    for dist in results:
        det_times = results[dist]["det"]
        rand_times = results[dist]["rand"]

        plt.figure()
        plt.plot(sizes, det_times, marker='o', label="Deterministic")
        plt.plot(sizes, rand_times, marker='o', label="Randomized")
        plt.xlabel("Input Size (n)")
        plt.ylabel("Running Time (seconds)")
        plt.title(f"Selection Algorithm Performance — {dist}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


# --------------------------------------------------------------
# Main
# --------------------------------------------------------------

if __name__ == "__main__":
    sizes, results = run_experiments()
    plot_results(sizes, results)
