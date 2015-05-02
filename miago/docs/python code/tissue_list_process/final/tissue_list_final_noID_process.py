# this python code process the tissue_list_final_noID file and gives the output including instance name and the mother term. This file will combine with the tissue_list_with_IDs_mother_processed file and use as input for finally generating owl file.

import fileinput

updateFile = open('tissue_list_final_noID_processed','a')
var = 0

for line in fileinput.input(['tissue_list_final_noID']):
    var = var + 1
    if 'Mother' in line :
        line = line.replace('Mother-','')
    line_list = line.split(';')
    if len(line_list) >1:
        tissue_instance_name = str(line_list[0]).strip()
    #print tissue_instance_name
        tissue_mother_name = str(line_list[1]).strip()
        updateFile.write(tissue_instance_name+';'+tissue_mother_name+'\n')
    else:
        print 'No mother term: '+ tissue_instance_name +' line:'+str(var) 

updateFile.close()
