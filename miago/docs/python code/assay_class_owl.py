# this code used to generate the assay instance and its class in OWL

import fileinput
import conclusion_assay_list


assay_list = []
assay_class_list = []



for line in fileinput.input([r'assay_class_list_mapping_OBI']):
    line_list = line.split(';') 
    assay = str(line_list[0]).strip()
    assay_list.append(str(assay))
    if len(line_list) >= 2:
        assay_class = str(line_list[1]).strip()
        if assay_class :
            assay_class_list.append(str(assay_class))
        else :
            assay_class = 'OBI_0000070'
            assay_class_list.append(str(assay_class))
    else :
        assay_class = 'OBI_0000070'
        assay_class_list.append(str(assay_class))
    
#print len(assay_class_list)
#print len(assay_list)

updateFile = open('assay_class.owl','w+')
updateFile1 = open('assay not in conclusion_assay_list','w+')
updateFile1.write('# Some assays that is not included in the ontology yet, since ontology contains only target-miRNA paired information\n') 
updateFile2 = open('assay_class_for_ontofox','w+')

assay_class_clean = []

for i in range(len(assay_list)):
    assay_1 = str(assay_list[i])
    if any(assay_1 in s for s in conclusion_assay_list.assay_list):
        for j in range(len(conclusion_assay_list.assay_list)):
            assay_text = conclusion_assay_list.assay_list[j]
            if assay_1 in assay_text:
                p = assay_list.index(assay_1)
                assay_1_class = assay_class_list[p]
                q = conclusion_assay_list.assay_list.index(assay_text)
                assay_ID = conclusion_assay_list.assay_ID_list[q]
                updateFile.write('    <!-- http://purl.obolibrary.org/obo/'+str(assay_ID)+' -->\n')
                updateFile.write('    <owl:NamedIndividual rdf:about="&obo;'+str(assay_ID)+'">\n        <rdf:type rdf:resource="&obo;'+assay_1_class+'"/>\n')
                updateFile.write('    </owl:NamedIndividual>\n\n\n')
            else:
                pass
    else: 
        updateFile1.write(assay_1+'\n') 
    assay_class_1 = str(assay_class_list[i])
    if assay_class_1 not in assay_class_clean:
        assay_class_clean.append(str(assay_class_1))
    else:
        pass

assay_class_clean = sorted(assay_class_clean)
for s in assay_class_clean:
    updateFile2.write('http://purl.obolibrary.org/obo/'+s+'\n')

updateFile.close()
updateFile1.close()
updateFile2.close()
	