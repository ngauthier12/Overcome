from IGeneticData import *


class SimpleGeneticData(IGeneticData):

    class Parameter:
        def __init__(self, name, variable_type, value):
            self.name = name
            self.variable_type = variable_type
            self.value = value

    def __init__(self):
        super().__init__()
        self.parameters = []
        self.paramters_by_name = {}

    def register_float(self, name, default = 0.0):
        assert name is not None, "Expecting not None name"
        assert isinstance(name, str), "Expecting name to be a string"

        assert default is not None, "Expecting a not None default"
        assert isinstance(default, float), "Expecting name to be a float"

        parameter = self.Parameter(name, type(float), default)
        self.parameters.append(parameter)
        self.paramters_by_name[name] = parameter

    def register_int(self, name, default=0):
        assert name is not None, "Expecting not None name"
        assert isinstance(name, str), "Expecting name to be a string"

        assert default is not None, "Expecting a not None default"
        assert isinstance(default, int), "Expecting name to be an int"

        parameter = self.Parameter(name, type(int), default)
        self.parameters.append(parameter)
        self.paramters_by_name[name] = parameter

    def register_bool(self, name, default=False):
        assert name is not None, "Expecting not None name"
        assert isinstance(name, str), "Expecting name to be a string"

        assert default is not None, "Expecting a not None default"
        assert isinstance(default, bool), "Expecting name to be a bool"

        parameter = self.Parameter(name, type(bool), default)
        self.parameters.append(parameter)
        self.paramters_by_name[name] = parameter
