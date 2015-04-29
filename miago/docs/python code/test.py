organism = ['human','mouse','rat','pig','Drosophila']
organism_ID = ['NCBITaxon_9606','NCBITaxon_10090','NCBITaxon_10116','NCBITaxon_9823','NCBITaxon_7227']
study_model =['miR-17-92 cKO mouse','mouse immunization with MOG35-55 andtransfected with miR-155', 'humans','b1-adrenergic receptor transgenic mice']

for j in range(len(study_model)):
    study_model_term = study_model[j]
    print study_model_term
    mother_study_model = 'OBI_0000'
    for k in range(len(organism)) :
        if organism[k] in study_model_term :
            print organism[k]
            mother_study_model = organism_ID[k]
        else:
            pass
    #if not mother_study_model: #true when mother_study_model is empty, but blank space is not included.http://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python
    #    mother_study_model = 'OBI_0000'
    print mother_study_model