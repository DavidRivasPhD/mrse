"""
Module to print out the output
"""

def printout(records):
    """
    Prints out abstracted info, specifically, certain NIH database fields of the top search results
    :param records:
    :return:
    """
    print("")
    for record in records:
        print("\033[1m" + "Title:", record.get("TI", "?"), "\033[0m")
        print("Authors:", record.get("AU", "?"))
        print("Source:", record.get("SO", "?"))
        print("Abstract:", record.get("AB", "?"))
        print("Publication Type:", record.get("PT", "?"))
        if (record.get("PMC", "?") != "?"):
            print("URL:", "https://www.ncbi.nlm.nih.gov/pmc/articles/" + record.get("PMC", "?") + "/")
        print("")

    return