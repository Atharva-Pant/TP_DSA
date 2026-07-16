def linear_search (customer_id, Targeted_customer_id):
    for index in range(len(customer_id)):
        if customer_id[index] == Targeted_customer_id:
            return index
    return -1


def Binary_search(customer_id , Targeted_customer_id):
    l = 0
    u = len(customer_id) - 1

    while l <= u :
        mid = (l+u)//2

        if customer_id[mid] == Targeted_customer_id:
            return mid
        elif Targeted_customer_id > customer_id[mid]:
            l = mid + 1 
        else:
            u = mid - 1
    return -1

#Sample output 
def main():
    customer_id = [1,34,56,78,23,32,120,34]
    customer_id.sort()
    Targeted_customer_id = 32

    print(f"""-------Customer_search-------
    Customer_id = {customer_id}
    Target_customer = {Targeted_customer_id}
    """)
    linear_search_result = linear_search(customer_id,Targeted_customer_id)
    if linear_search_result !=-1:
        print(f"[Linear Search] Found ID {Targeted_customer_id} at index {linear_search_result}")
    else:
        print(f"[Linear Search] ID {Targeted_customer_id} not found.")


    binary_result = Binary_search(customer_id, Targeted_customer_id)
    if binary_result != -1:
        print(f"[Binary Search] Found ID {Targeted_customer_id} at index {binary_result}")
    else:
        print(f"[Binary Search] ID {Targeted_customer_id} not found.")


main()


 