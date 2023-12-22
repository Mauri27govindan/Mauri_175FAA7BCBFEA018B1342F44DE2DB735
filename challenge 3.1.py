def linear_search_product(products, target_product):
    indices = []  # List to store indices of occurrences

    # Iterate over the list of products and check for the target product
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)

    return indices  # Return list of indices of occurrences


# Test the linear_search_product function
if __name__ == "__main__":
    products_list = ["Apple", "Banana", "Orange", "Apple", "Grape", "Apple", "Mango"]

    target = "Apple"
    result_indices = linear_search_product(products_list, target)
    if result_indices:
        print(f"The product '{target}' is found at indices: {result_indices}")
    else:
        print(f"The product '{target}' is not found in the list.")

    target = "Pineapple"
    result_indices = linear_search_product(products_list, target)
    if result_indices:
        print(f"The product '{target}' is found at indices: {result_indices}")
    else:
        print(f"The product '{target}' is not found in the list.")
