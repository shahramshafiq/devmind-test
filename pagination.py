def paginate(data, page_size):
    """
    Divide a list into pages of a specified size.

    Args:
        data (list): The list to be paginated.
        page_size (int): The size of each page.

    Returns:
        list: A list of pages, where each page is a list of elements.
    """
    total_pages = -(-len(data) // page_size)  # Calculate the total number of pages using ceiling division
    return [data[i * page_size:(i + 1) * page_size] for i in range(total_pages)]