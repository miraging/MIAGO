import fileinput

disease_mother_list = []
disease_text_list = []

updateFile = open('no disease mapping','w+')
updateFile1 = open('disease_mother_for_ontofox','w+')

for line in fileinput.input([r'disease_list_with_IDs']):
    line_list = line.split(';') 
    disease_text = str(line_list[0]).strip()
    print disease_text
    if len(line_list) > 1 and line_list[1] :
        disease_mother = str(line_list[1]).strip()
        if disease_mother not in disease_mother_list:
            disease_mother_list.append(str(disease_mother))
            disease_text_list.append(str(disease_text))
        else:
            pass
    else:
        updateFile.write(disease_text+'\n')

disease_mother_list = sorted(disease_mother_list)
for disease_ID in disease_mother_list:
    updateFile1.write(disease_ID+'\n')