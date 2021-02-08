import numpy as np
import pandas as pd
import random
from collections import namedtuple

class Matcher:
    def __init__(self,resp_csv,proj,cons_csv,cons):
        self.responses = pd.read_csv(
            resp_csv,
            header=0,
            usecols=proj,
            names=["student","first","second","third","fourth","fifth"]
            )
        self.constraints = pd.read_csv(
            cons_csv,
            header=0,
            usecols=cons
            )
    
    def match():
        return self.responses,self.constraints
        