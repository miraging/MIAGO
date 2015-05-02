# this file is used to generate new tissue(evaluant) class IDs from the file tissue_list_with_IDs_mother
# input tissue_list_with_IDs_mother
# output tissue_list_with_IDs_mother_processed, tissue new class ID owl file

import fileinput
import math
tissue_new_class_name_list = []
tissue_mother_class_list = []

for line in fileinput.input(['tissue_list_with_IDs_mother']):
    line = str(line).strip()
    line = line.replace('Mother-','') # delete Mother-from the line  
    line_list = line.split(';')
    tissue_new_class_name = line_list[0]
    tissue_new_class_name = str(tissue_new_class_name).strip()
    tissue_new_class_name_list.append(str(tissue_new_class_name))
    tissue_mother_class = line_list[1]
    tissue_mother_class = str(tissue_mother_class).strip()
    tissue_mother_class_list.append(str(tissue_mother_class))


varID = 3000 # new MIAGO ID start point of tissue(evaluant) class
updateFile = open('new_tissue_class_ID.owl', 'a') # the owl file for assign new MIAGO IDs for evaluant terms
updateFile1 = open(r'final\tissue_list_with_IDs_mother_processed','a') # the evaluant name,ID and mother term pair
 
for i in range(len(tissue_new_class_name_list)):
    varID = varID + 1
    len1 = int(math.log10(varID))+1
    string_val = "0" * (7-len1)
    ntissue_class_ID = string_val+str(varID)
    ntissue_class_name = tissue_new_class_name_list[i]
    ntissue_mother_ID = tissue_mother_class_list[i]
    if 'EFO' in ntissue_mother_ID:
        ntissue_mother_ID = 'http://www.ebi.ac.uk/efo/'+ ntissue_mother_ID
    else:
        ntissue_mother_ID = '&obo;'+ ntissue_mother_ID # if make it imported file, &obo;has to change to http://purl.obolirbary.org/obo/

    updateFile.write('    <!-- http://purl.obolibrary.org/obo/MIAGO_'+ ntissue_class_ID +' -->\n\n')
    updateFile.write('    <owl:Class rdf:about="&obo;MIAGO_'+ ntissue_class_ID +'">\n')
    updateFile.write('        <rdfs:label xml:lang="en">' + ntissue_class_name + '</rdfs:label>\n')
    updateFile.write('        <rdfs:subClassOf rdf:resource="' + ntissue_mother_ID + '"/>\n')
    updateFile.write('    </owl:Class>\n\n\n')
    

    updateFile1.write(ntissue_class_name+';MIAGO_'+ntissue_class_ID+'\n')


updateFile.close()
updateFile1.close()

    
    





