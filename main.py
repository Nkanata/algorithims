# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# algorithms a set of instructions for accomplishing a task.

# Binary Search
import collections
from functools import reduce
from math import ceil, floor
from time import sleep


def binary_search(nums, n):
    nums = sorted(nums)
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = floor((low + high) / 2)
        guess = nums[mid]
        print(f'{mid=} {guess=}')
        if guess == n:
            return mid
        if guess > n:
            high = mid - 1
        else:
            low = mid + 1
    return None


# selection sort


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        # print(arr.pop(smallest))
        print(i, len(arr))
        newArr.append(arr.pop(smallest))
        print(newArr)
    return newArr


# recursion


def count(i):
    print(i)
    if i <= 0:
        return
    else:
        count(i - 1)


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def sum_(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + sum_(arr)


def count_items_in_a_list(arr):
    count = 0
    if not arr:
        return 0
    else:
        arr.pop(0)
        count += 1 + count_items_in_a_list(arr)
        return count


def max_in_a_list(arr):
    max_ = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_:
            max_ = arr[i]
            max_index = i
    return max_, max_index


# quicksort

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def print_item(list):
    for item in list:
        print(item)


def print_item2(list):
    for item in list:
        sleep(1)
        print(item)


# Breadth first Search
from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def bfs():
    graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "claire": ["thom", "jonny"],
             "anuj": [], "peggy": [], "thom": [], "jonny": []}
    search_queue = deque()
    search_queue += graph["you"]

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + "is a mango seller")
            return True
        else:
            search_queue += graph[person]
    return False


# Dijkstras algorithm

# insertion sort
def insertionSort(array):
    for j in range(len(array)):
        print(j)
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array


def openLock(self, deadends: list[str], target: str) -> int:
    queue = collections.deque()
    sdeadends = set(int(x) for x in deadends)

    if 0 in sdeadends:
        return -1

    dist = {}
    queue.append(0)
    dist[0] = 0

    while len(queue) > 0:
        current = queue.popleft()
        current_positions = [(current // (10 ** index)) % 10 for index in range(4)]

        for index in range(4):
            for delta in [-1, 1]:
                next_positions = current_positions[:]
                next_positions[index] += delta
                next_positions[index] %= 10

                nxt = reduce(lambda a, x: a * 10 + x, next_positions[::-1])

                if nxt not in sdeadends and nxt not in dist:
                    queue.append(nxt)
                    dist[nxt] = dist[current] + 1

    if int(target) not in dist:
        return -1
    return dist[int(target)]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    my_list1 = [7, 8, -1, 5, -6, 9, 4, -2, -1556, 879]
    # print(binary_search(my_list, -1556))
    # print(selection_sort(my_list))
    # count(10)
    # print(fact(9))
    print(sum_([120, 454, 600]))
    # print(count_items_in_a_list(my_list1))
    print(max_in_a_list([469, 8, 987, 1000, -78]))
    print(quicksort(my_list1))
    list = [1, 2, 3, 4]

    print(list[1:])
    print(list[:3])
    # print_item(list)
    # print_item2(list)
    book = dict()
    book["apple"] = 0.67
    book["milk"] = 1.49
    book["avocado"] = 1.49
    print(book)
    print(book["milk"])
    print("")
    print(insertionSort([5, 2, 4, 6, 1, 3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
