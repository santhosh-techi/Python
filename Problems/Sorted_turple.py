def highest_count(num):
    unique = []
    for i in num:
        if i not in unique:
            unique.append(i)

    sorted_unique = sorted(unique)  # Sort the list of unique numbers

    return tuple(sorted_unique)  # Return the sorted tuple

# Example usage:
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 0, 1, 12, 3, 4, 2, 2, 4)
print(highest_count(my_tuple))


