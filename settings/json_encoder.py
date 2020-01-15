from json import JSONEncoder


class JSONEncoderWithoutModificator(JSONEncoder):
    def default(self, o):
        return {k.lstrip('_'): v for k, v in vars(o).items()}
