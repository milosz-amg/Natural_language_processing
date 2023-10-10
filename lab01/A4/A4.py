
banned_word='kocham'
counter =0

with open('source.txt', 'r') as source_file:
    with open('censored.txt', 'w') as target_file:
        for line in source_file:
            counter+=1
            lowered_line = line.lower()
            if counter % 3 == 0 or banned_word in lowered_line:
                target_file.write("***\n")
            else:
                target_file.write(line)

source_file.close()
target_file.close()