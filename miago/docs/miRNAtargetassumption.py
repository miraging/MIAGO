""" The pattern for miRNA target assumption (class) is:
    MIAGO_0000076  is about miRNA target
    MIAGO_0000078  is about miRNA
    MIAGO_0000045  miRNA target assumption based on
    
   
    <!-- http://purl.obolibrary.org/obo/MIAGO_0000080 -->

    <owl:Class rdf:about="&obo;MIAGO_0000080">
        <rdfs:label xml:lang="en">miR-29a targeting Ppm1d assumption</rdfs:label>
        <rdfs:subClassOf rdf:resource="&obo;MIAGO_0000079"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="&obo;MIAGO_0000076"/> 
                <owl:someValuesFrom rdf:resource="&obo;MIAGO_0000088"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="&obo;MIAGO_0000076"/>
                <owl:someValuesFrom rdf:resource="&obo;MGI_1858214"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="&obo;MIAGO_0000045"/>
                <owl:hasValue rdf:resource="&obo;MIAGO_0000100"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="&obo;MIAGO_0000045"/>
                <owl:hasValue rdf:resource="&obo;MIAGO_0000099"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="&obo;MIAGO_0000045"/>
                <owl:hasValue rdf:resource="&obo;MIAGO_0000103"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="&obo;MIAGO_0000078"/>
                <owl:someValuesFrom rdf:resource="&obo;MIAGO_0000204"/>
            </owl:Restriction>
        </rdfs:subClassOf>
    </owl:Class>