from Process.Api.Special import Special
from Process.Api.Get import Get
from Process.Api.Do import Do
from Process.Api.Set import Set

class Api(Special,Get,Do,Set):
    def __init__(self):
        super().__init__()
        self.Get = Get()
        self.Special = Special()

