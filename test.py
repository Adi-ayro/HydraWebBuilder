style1 = {
    "id": ["#my", "#myheading1","#myheading2"],
    "tag": "h1",
    "font": "ariel",
    "color" : "#1169FF",
    "size" : "25px"
}

style2 = {
    "id": ["#my", "#my69","#my24"],
    "tag": "p",
    "font": "ariel",
    "color" : "#1169FF",
    "size" : "25px"
}


def style(*args):
    """
    args : dictionary containing style options
    keys:
    id: list containing page ids
    tag: h1 p div
    font: font family
    size: font size
    color: font color
    """

    start = """
    <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
    <style amp-custom>
    """

    end = """
    </style>
    </head>
    <body>
    """
    
    final = """
    """
    for arg in args:
        id = arg["id"]
        tag = arg["tag"]
        font = arg["font"]
        color = arg["color"]
        size = arg["size"]

        code = ""
        for i in range(0,len(id) - 1):
            code += f"{id[i]} {tag},"
        code += f"{id[-1]} {tag}"
        code += "{"
        code += f"""
        font-family: {font};
        font-size: {size};
        color: {color};
        """
        code += """}
        """
        final += code

    return start + final + end

print(style(style1, style2))


