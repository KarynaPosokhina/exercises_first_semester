with open("books.txt", "r") as file:
    lines = file.readlines()
for i in range(0, len(lines), 2):
    title = lines[i].strip()
    author = lines[i + 1].strip()

    print(f"{title} -> {author}")
