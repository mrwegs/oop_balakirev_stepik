class RenderList:
    type_list: str

    def __init__(self, type_list):
        self.type_list = type_list

    def __setattr__(self, key, value):
        if key == 'type_list' and value not in ('ul', 'ol'):
            self.__dict__[key] = 'ul'
        else:
            super().__setattr__(key, value)

    def __call__(self, *args, **kwargs):
        string_list = args[0]
        string = '</li>\n<li>'.join(string_list)
        return f'<{self.type_list}>\n<li>{string}</li>\n</{self.type_list}>'


