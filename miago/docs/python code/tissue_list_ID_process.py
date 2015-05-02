# this script is to seperate the tissue that have a Mother_ID from the tissue_list_with_IDs file

import fileinput

line_list = []
mapping_list = []

updateFile = open(r'tissue_list_process\tissue_list_with_IDs_processed','a') # this file gives only the tissue list with the IDs that will need to import and build up the derives from relation between a tissue and an existing ID.
updateFile1 = open(r'tissue_list_process\tissue_list_with_IDs_mother','a') # this file gives the tissues that needs to assign to a mother term
updateFile2 = open(r'tissue_list_process\tissue_list_with_IDs_noID','a') # this file gives the tissue that has no id or needs to check the original papers.
updateFile3 = open(r'tissue_list_process\tissue_list_with_IDs_mother_transfected','a') # this file gives the tissues that needs to assign to a mother term / after deleted the 'Mother-' just assert it as an instance 
updateFile4 = open(r'tissue_list_process\tissue_list_with_IDs_mother_cell_line','a') # this file gives the tissues that needs to assign to a new cell line term. There is no data in this file. 
updateFile5 = open(r'tissue_list_process\tissue_mapping_list','a') # this file contains the distinct mapping list from the manual mapping, then it will be processed and produce a tissue_mapping owl file

for line in fileinput.input(['tissue_list_with_IDs_manual_mapping']):
    line = str(line).strip()
    line_list = line.split(';',1 )
    if len(line_list) >1:
        mapping = str(line_list[1])
        mapping = mapping.replace('Mother-','')
        if mapping not in mapping_list:
            mapping_list.append(str(mapping))
        else:
            pass
    if "#" in line:
        pass
    elif 'Mother' in line:
        if 'cell_line' in line:
            updateFile4.write(line+'\n')
        elif ('transfect' or 'treat') in line:
            updateFile3.write(line+'\n')
        else:
            updateFile1.write(line+'\n')
    elif '???' in line:
        updateFile2.write(line+'\n')
    else:
        updateFile.write(line+'\n')

for i in range(len(mapping_list)):
    updateFile5.write(str(mapping_list[i])+'\n')
    
updateFile.close()
updateFile1.close()	
updateFile2.close()	
updateFile3.close()	
updateFile4.close()	
updateFile5.close()	