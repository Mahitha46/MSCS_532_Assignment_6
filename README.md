Overview

This assignment is divided into two major parts:

Part 1 – Selection Algorithms:
Implementation and empirical analysis of Deterministic Linear-Time Selection (Median of Medians) and Randomized Quickselect.

Part 2 – Elementary Data Structures:
Manual implementation of arrays, stacks, queues, and linked lists, along with performance discussion.


Part 1 – Selection Algorithms

Implemented Algorithms

1. Deterministic Selection Algorithm (Median of Medians)

Worst-case linear time: O(n)

Uses the “median of 5” grouping strategy to guarantee good pivots.

Suitable for real-time and worst-case-critical applications.

2. Randomized Quickselect

Expected time: O(n)

Worst case: O(n²) (rare)

Easy to implement and efficient in practice.

Good for general-purpose selection tasks.

Datasets Used

Random arrays

Sorted arrays

Reverse-sorted arrays



How to Run Part 1 Code
python select_algorithms.py

python empirical_analysis.py

The script:

Runs both algorithms automatically

Generates timing results

Outputs empirical comparison plots using matplotlib

Part 2 – Elementary Data Structures

Implemented Data Structures
1. Arrays

Manual array with:

insert(index, value)

delete(index)

access(index)

2. Matrices

2D array implemented via lists of lists

Supports:

get(r, c)

set(r, c, value)

3. Stack (Array-based)

push(x)

pop()

peek()

is_empty()

4. Queue (Array-based Circular Buffer)

enqueue(x)

dequeue()

is_empty()

5. Singly Linked List

insert_at_head(value)

insert_at_tail(value)

delete(value)

traverse()

Discussion Summary

Arrays are ideal when constant-time access is required.

Stacks and Queues are efficiently implemented using arrays but may require resizing.

Linked Lists are better for frequent insertions and deletions.

Queues as circular buffers eliminate shifting costs and maintain O(1) performance.

Data structure choice depends on:

Memory constraints

Access pattern

Update frequency

How to Run Part 2 Code

python data_structures.py

This script:

Demonstrates operations on all implemented structures

Prints output examples to the console


Built With

Python 3.10+

Matplotlib

Random

Time
