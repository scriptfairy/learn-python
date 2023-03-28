import random

## Exercise 6: Create a random list of strings
def get_random_cities(sample_size):
    capital_cities = ['Washington', 'London', 'Paris', 'Tokyo', 'Beijing', 'Moscow', 'Cairo', 'New Delhi', 'Brasilia', 'Ottawa', 'Canberra', 'Rome', 'Berlin', 'Madrid', 'Stockholm', 'Helsinki', 'Athens', 'Ankara', 'Dublin', 'Oslo']
    if sample_size > 20:
        sample_size = 20
    if sample_size < 1:
        sample_size = 1

    return random.sample(capital_cities, sample_size)

## Exercise 7: Create a function to sort the list above alphabetically

def quicksort(l):
    if len(l) <= 0:
        return l
    else:
        left = []
        right = []
        pivot = l[0]
        for i in range(1,len(l)):
            if l[i] > pivot:
                right.append(l[i])
            else: 
                left.append(l[i])

        return quicksort(left) + [pivot] + quicksort(right)

# ## Exercise 8: Create a function to count the vowels in each word in your list
def count_vowels(l):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = []
    for item in l:
        print("\n item = ", item)
        count = 0
        for ch in item:
            print("\n ch = ", ch)
            if ch.lower() in vowels:
                print("it is in \n")
                count += 1
                print(" count is \n",count)
        counts.append(count)
    return counts


# l = get_random_cities(3)
# list_sorted = count_vowels(l)
# print("before sort \n",l)
# print("after sort \n", list_sorted)