from Process.Api.Special import Special
from Process.Api.Get import Get
from Process.Api.Do import Do
from Process.Api.Set import Set
from Process.Api.Func import Func
import time

class Api(Special,Get,Do,Set,Func):
    def __init__(self):
        super().__init__()
        self.Get = Get()
        self.Special = Special()

