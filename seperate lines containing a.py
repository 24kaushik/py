input_file_path = "textFile.txt"
output_file_path = "outputFile.txt"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        if 'a' not in line:
            output_file.write(line)
        print(line)

