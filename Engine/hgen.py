from functions import *
from data import *

class Router:
    def __init__(self, name):
        if(name == "plainBottom"):
            self.function = plainBottom
        if(name == "gradientBottom"):
            self.function = gradientBottom
        if(name == "plainTop"):
            self.function = plainTop
        if(name == "gradientTop"):
            self.function = gradientTop


class htmlPreview:
    def __init__(self, function, ani : Animation, data : Dataset, vis : Visuals, *args):
        page = Router(function)
        a = boilerplate("None", "None")
        b = style(*args)
        c = AMPstandalone("None","None","None","None") 
        d = page(data, ani, vis)
        self.code = a + b + c + d + ending()