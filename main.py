from typing import Union, Dict


class Model:
    repr: str
    fields: Union[Dict, None]

    def __init__(self):
        self.repr = 'Model'
        self.fields = None

    def query(self, **kwargs):
        self.fields = kwargs
        self.repr += f': {", ".join([f"{k}={v}" for k, v in self.fields.items()])}'

    def __str__(self):
        return self.repr


# model = Model()
# model.query(id=1, name='Bob', age=56)
#
# print(model)