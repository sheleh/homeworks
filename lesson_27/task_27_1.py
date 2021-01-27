# A bubble sort can be modified to “bubble” in both directions.
# The first pass moves “up” the list and the second pass moves “down.”
# This alternating pattern continues until no more passes are necessary.
# Implement this variation and describe under what circumstances it might be appropriate.
import random
def shaker_sort(array):
    done = False
    while not done:
        done = True
        for i in range(0, len(array) - 2):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                done = False
        if done:
            break
        done = True
        for i in range(len(array) - 2, 0, -1):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                done = False

if __name__ == "__main__":
    test_list = [random.randint(1, 100) for _ in range(23)]
    print(test_list)
    shaker_sort(test_list)
    print(test_list)