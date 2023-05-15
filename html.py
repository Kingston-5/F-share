

def ulify(elements, parentId = "", childId = ""):
    string = f"<ul id='{parentId}'>\n"
    for s in elements:
        string += "\n" + "<li id={childId}>" + iconify(s[-4:]) + str(s) + "</li>"
        print(iconify(s[-4:]))
    string += "\n</ul>"
    return string


def nestedUlify(elements, parentId = "", childId = ""):
    string = f"<div id='{parentId}'>\n"
    for e in elements:
        string += f'<p>{iconify()} {list(e.items())[0][0]}</p>\n'
        string += "<ul>"
        for li in list(e.items())[0][1]:
            string += '<li>' +iconify(li[-4:]) + li + '</li>'
        string += "</ul>"
    string += "\n</div>"
    return string


def iconify(icon=""):
    if icon == ".jpg":
        return ' <i class="fa-solid fa-image"></i> '
    elif icon == ".pdf":
        return ' <i class="fa-solid fa-file-pdf"></i> '
    else:
        return ' <i class="fa-solid fa-folder"></i> '


