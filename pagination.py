def paginate(list, page_size):
    """
    Paginates a list into chunks of a specified size.

    Args:
        list (list): The list to be paginated.
        page_size (int): The size of each page.

    Returns:
        list: A list of pages, where each page is a list of items.
    """
    # Input validation
    if not isinstance(list, list):
        raise ValueError("Input must be a list")
    if not list:
        return []
    if not isinstance(page_size, int) or page_size <= 0:
        raise ValueError("Page size must be a positive integer")

    # Calculate the total number of pages
    total_pages = -(-len(list) // page_size)  # Ceiling division

    # Initialize the list of pages
    pages = []

    # Iterate over the range of pages
    for i in range(total_pages):
        # Calculate the start and end indices for the current page
        start = i * page_size
        end = (i + 1) * page_size

        # Append the current page to the list of pages
        if end > len(list):
            # If the list length is exactly divisible by page_size, return an empty list for the last page
            if end == len(list) + page_size:
                pages.append([])
            else:
                pages.append(list[start:])
        else:
            pages.append(list[start:end])

    return pages