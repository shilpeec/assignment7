from search_recipes import search_recipes

if __name__ == "__main__":
    query = "egg curry"
    result = search_recipes(query=query)
    print("Search result:", result)
