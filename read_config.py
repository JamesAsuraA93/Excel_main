temp_lst = []
file = open("Floppy.txt","r")
all_lines = file.readlines()
file.close()
for line in all_lines:
    temp_lst.append(line.strip())
