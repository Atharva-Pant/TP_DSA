def selection_sort(Salaries):
    n=len(Salaries)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if Salaries[j]< Salaries[min_index]:
                min_index = j
        Salaries[i] , Salaries[min_index] = Salaries[min_index] ,Salaries[i]

    return Salaries

def bubble_sort(Salaries):
    """
    Sorts an array using the Bubble Sort algorithm.
    Time Complexity: O(n^2)
    """
    n = len(Salaries)
    for i in range(n-2,-1,-1):
        swapped = False
        
        # Last i elements are already in place, so we don't check them
        for j in range(0, i+1):
            # Swap if the element found is greater than the next element
            if Salaries[j] > Salaries[j + 1]:
                Salaries[j], Salaries[j + 1] = Salaries[j + 1], Salaries[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, then array is sorted
        if not swapped:
            break
            
    return Salaries

def main():
    # Sample list of floating-point Salaries
    Salaries = [54000.50, 78500.00, 42000.75, 120500.25, 61000.00, 
                89000.50, 95000.00, 45000.25, 110000.00, 52000.50]
                
    print(f"Original Salaries:\n{Salaries}\n")

    # We use a copy of the list so we can demonstrate both algorithms
    # running on the original unsorted data.
    selection_sorted = selection_sort(Salaries.copy())
    print(f"After Selection Sort:\n{selection_sorted}\n")

    bubble_sorted = bubble_sort(Salaries.copy())
    print(f"After Bubble Sort:\n{bubble_sorted}\n")
    # The list is now sorted in ASCENDING order (lowest to highest).
    # To get the top 5 highest, we slice the last 5 elements from the list: [-5:]
    # Then we reverse them [::-1] so the absolute highest is printed first.
    top_five = bubble_sorted[-5:][::-1]
    
    print("--- Top 5 Highest Salaries ---")
    for i, salary in enumerate(top_five, 1):
        print(f"{i}. ${salary:,.2f}")

# Run the program
main()