def paginate(list_to_paginate, page_size):
    """
    Paginates a list into chunks of a specified size.

    Args:
        list_to_paginate (list): The list to be paginated.
        page_size (int): The size of each page.

    Returns:
        list: A list of pages, where each page is a list of items.
    """
    pages = []
    for i in range(0, len(list_to_paginate), page_size):
        page = list_to_paginate[i:i + page_size]
        pages.append(page)
    return pages