import fileinput

for line in fileinput.input([r'disease_list_with IDs']):
    line_list = line.split(';') 
    disease_text = str(line_list[0]).strip()