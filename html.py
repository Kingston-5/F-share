

def ulify(elements, parentId = "", childId = ""):
    string = f"<ul id={parentId}>\n"
    string += "\n".join([f"<li id={childId}>" + str(s) + "</li>" for s in elements])
    string += "\n</ul>"
    return string
    

