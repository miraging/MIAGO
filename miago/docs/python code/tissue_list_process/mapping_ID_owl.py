# mapping_ID_owl.py is to generate the OWL file from the tissue_mapping_list

import fileinput

updateFile = open('tissue_terms_mapping.owl','a')

for line in fileinput.input(['tissue_mapping_list']):
    line_list = line.split(';')
    if len(line_list) > 1:
        for i in range(len(line_list)):
            mother_term_ID = str(line_list[i]).strip()
            if 'EFO' in mother_term_ID:
                mother_term_ID = 'http://www.ebi.ac.uk/efo/'+ mother_term_ID
            else:
                mother_term_ID = 'http://purl.obolibrary.org/obo/'+ mother_term_ID
            if i == 0:
                updateFile.write('    <!-- '+ mother_term_ID +' -->\n\n')
                updateFile.write('     <owl:Class rdf:about="&obo;'+str(line_list[i]).strip()+'">\n')
            if i > 0:
                if 'EFO' not in mother_term_ID: 
                    updateFile.write('        <rdfs:seeAlso rdf:resource="&obo;'+str(line_list[i]).strip()+'"/>\n')
                else:
                    updateFile.write('        <rdfs:seeAlso rdf:resource="'+mother_term_ID+'"/>\n')
        updateFile.write('    </owl:Class>\n\n\n')  
    else:
        pass
    
            
updateFile.close()