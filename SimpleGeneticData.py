from IGeneticData import *


class SimpleGeneticData(IGeneticData):

    supported_types = [float, int, bool]

    class Parameter:
        def __init__(self, name, variable_type, value):
            self.name = name
            self.variable_type = variable_type
            self.value = value

    def __init__(self):
        super().__init__()
        self.parameters = []
        self.parameters_by_name = {}

    def __setitem__(self, key, value):
        assert key is not None, "Expecting not None key"
        assert isinstance(key, str), "Expecting key to be a string"

        assert value is not None, "Expecting a not None value"
        assert type(value) in self.supported_types, "Parameter type is not supported"

        parameter = self.Parameter(name=key, variable_type=type(value), value=value)
        self.parameters.append(parameter)
        self.parameters_by_name[key] = parameter

    def __getitem__(self, key):
        assert key in self.parameters_by_name, "Could not retrieve parameter with given name"
        return self.parameters_by_name[key]
