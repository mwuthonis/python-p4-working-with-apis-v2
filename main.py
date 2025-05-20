if __name__ == "__main__":
    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("\nSearch Result:\n")
    print(result)
