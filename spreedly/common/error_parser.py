def errors_from(xml_doc):
    errors = []

    for xml_error in xml_doc.xpath('.//errors/error'):
        #TODO Error attributes and key.
        errors.append({
            "attributes": "",
            "key": "",
            "message": xml_error.text
        })

    return errors
