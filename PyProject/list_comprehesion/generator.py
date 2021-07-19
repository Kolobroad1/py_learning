def fourer():
    words = ["sasuke", "uchiha", "mama","papa", "naruto"]
    filtered = [num for num in range(20, 0, -4)]
    filtered_new = [num * 2 for num in range(10, 0, -2)]
    word_filter = [word for word in words if len(word) < 5]
    print("new filtered below")
    print(filtered_new)
    print(filtered)
    print(word_filter)
fourer()