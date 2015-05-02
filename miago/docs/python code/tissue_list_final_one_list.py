# this file uses two inputs from the final folder: tissue_list_with_IDs_mother_processed and tissue_list_final_noID_processed 
# output is the list contains tissue instance name and mother term ID
# it will be imported into tissuestudymodel.py for generating owl file

import fileinput
tissue_instance_name_list = []
tissue_mother_ID_list = []
tissue_mother_both_list =[]

updateFile1 = open('tissue_mother_both','w+')

for line in fileinput.input([r'tissue_list_process\final\tissue_list_with_IDs_mother_processed']):
    line_list = line.split(';')
    if len(line_list) > 1:
        tissue_instance_name = str(line_list[0]).strip()
        tissue_instance_name_list.append(str(tissue_instance_name))
        tissue_mother_ID = str(line_list[1]).strip()
        tissue_mother_ID_list.append(str(tissue_mother_ID))
        if len(line_list) > 2 :
            tissue_mother_both = str(line_list[1]) + str(line_list[2])
            tissue_mother_both_list.append(str(tissue_mother_both))
        else :
            tissue_mother_both = tissue_mother_ID
            tissue_mother_both_list.append(str(tissue_mother_both))
    else:
        pass

for line1 in fileinput.input([r'tissue_list_process\final\tissue_list_final_noID_processed']):
    line1_list = line1.split(';')
    if len(line1_list) > 1:
        tissue_instance_name = str(line1_list[0]).strip()
        tissue_instance_name_list.append(str(tissue_instance_name))
        tissue_mother_ID = str(line1_list[1]).strip()
        tissue_mother_ID_list.append(str(tissue_mother_ID))
        if len(line1_list) > 2 :
            line2_list = line1.split(';',1)
            tissue_mother_both = str(line2_list[1])
            tissue_mother_both_list.append(str(tissue_mother_both))
            updateFile1.write(str(tissue_mother_both) + '\n')
        else :
            tissue_mother_both = tissue_mother_ID
            tissue_mother_both_list.append(str(tissue_mother_both))
            updateFile1.write(str(tissue_mother_both) + '\n')
    else:
        pass


updateFile = open('final_one_list','w+')
mothers_list = []
for i in range(len(tissue_mother_ID_list)):
    mothers = tissue_mother_ID_list[i]
    mother_list = mothers.split(';')
    if len(mother_list) >0:
        for j in range(len(mother_list)):
            mother_term = mother_list[j]
            if mother_term not in mothers_list:
                mothers_list.append(str(mother_term))
            else:
                pass
# sort the list
OBO_namespace = ['CL','CLO','BTO','UBERON','FMA','MIAGO','OBI']
mothers_list = sorted(mothers_list)
for k in range(len(mothers_list)):
    mothers_term = str(mothers_list[k])
    if any(x in mothers_term for x in OBO_namespace):
        mothers_prefix = 'http://purl.obolibrary.org/obo/'
    else:
        mothers_prefix = 'http://www.ebi.ac.uk/efo/'
    updateFile.write(mothers_prefix + str(mothers_list[k])+'\n')   
 



updateFile.close()
updateFile1.close()
#print len(tissue_mother_ID_list)  # result  436
#print len(tissue_instance_name_list)   # result  436
#print len(tissue_mother_both_list) 

