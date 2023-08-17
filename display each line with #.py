file_path = "textFile.txt"

with open(file_path, 'r') as file:
    for line in file:
        words = line.strip().split()
        formatted_line = ' #'.join(words)
        print(formatted_line)
