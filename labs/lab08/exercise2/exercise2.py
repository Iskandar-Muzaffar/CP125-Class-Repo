# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function
    files1 = open(file1, 'r')
    files2 = open(file2, 'r')
    output = open(output_file, 'w')

    name1 = files1.readlines()
    name2 = files2.readlines()

    old_file = (name1 + name2)
    new_file = []

    for names in old_file:
        if names not in new_file:
            new_file.append(names)
            
    new_file.sort()
    
    for names in new_file:
        output.write(names)

    files1.close()
    files2.close()
    output.close()
    
    return len(new_file)


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
