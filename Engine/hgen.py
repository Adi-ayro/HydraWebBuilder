from functions import *
from data import *

class Router:
    def __init__(self, name):
        if(name == "Plain Bottom"):
            self.function = plainBottom
        if(name == "Gradient Bottom"):
            self.function = gradientBottom
        if(name == "Plain Top"):
            self.function = plainTop
        if(name == "Gradient Top"):
            self.function = gradientTop

    def __call__(self, data, ani, vis):
        return self.function(data, ani, vis)


class htmlPreview:
    def __init__(self, function, ani : Animation, data : Dataset, vis : Visuals, *args):
        page = Router(function)
        a = boilerplate("None", "None")
        b = style(*args)
        c = AMPstandalone("None","None","None","None") 
        d = page(data, ani, vis)
        self.code = a + b + c + d + ending()

class htmlExport:
    def __init__(self, start: Start, styles, pages, filename, location):
        self.start = start
        self.styles = styles
        self.pages = pages
        self.filename = filename
        self.location = location

        a = boilerplate(self.start.title,self.start.canonical)
        b = style(s.getarg() for s in self.styles)
        c = AMPstandalone(self.start.title, self.start.publisher, self.start.logo, self.start.poster)

        self.code = a + b + c

        for page in pages:
            self.code += Router(page.function)(page.dataset,page.animation,page.visual)

        self.code += ending()

    def maker(self):
        addr = f"{self.location}/{self.filename}.html"
        with open(addr, "w") as f:
            f.write(self.code)
            f.close()

    