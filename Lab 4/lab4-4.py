def build_xml_element(tag, content, **kwargs):
    attributes =  "".join(f' {key} = \\"{value}\\"' for key, value in kwargs.items())
    element = f"<{tag} {attributes}>{content}</{tag}>"
    return element

print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
