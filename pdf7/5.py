file = open("Test.txt")

result = {}

for line in file:
    if '\n' in line:
        line = line[:-1]  #usuwa znak konca linii
    if ":"  in line:
        key,val = line.split(":")
        if key in result:
            result[key].append(val)
        else:
            result[key] = [val]
    else:
        print("Zignorowano linijkę:", line, "z powodu braku dwukropka")

sorted_keys = sorted(result)

sorted_dict = {key : result[key] for key in sorted_keys}

save_file = open("Test1.txt", "w")

save_file.write(str(sorted_dict))

print(sorted_dict)