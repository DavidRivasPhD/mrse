"""
Module to allow user to select a search filter
"""

def filter_selector(query):
    """
    Selects filter
    :param query:
    :return: query including selected filter
    """
    selected_filter = input("Available Filters: \n \
    1 = Clinical Trial \n \
    2 = Meta-Analysis \n \
    3 = Personal Narrative \n \
    4 = Preprint \n \
    5 = Randomized Controlled Trial \n \
    6 = Review \n \
    7 = Systematic Review \n Enter the filter number: ")

    if (selected_filter == "1"):
        query = query + " AND Clinical Trial[pt]"
    elif (selected_filter == "2"):
        query = query + " AND Meta-Analysis[pt]"
    elif (selected_filter == "3"):
        query = query + " AND Personal Narrative[pt]"
    elif (selected_filter == "4"):
        query = query + " AND Preprint[pt]"
    elif (selected_filter == "5"):
        query = query + " AND Randomized Controlled Trial[pt]"
    elif (selected_filter == "6"):
        query = query + " AND Review[pt]"
    elif (selected_filter == "7"):
        query = query + " AND Systematic Review[pt]"

    return query




