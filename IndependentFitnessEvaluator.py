import types

from IFitnessEvaluator import *
from IGeneticData import *


class IndependentFitnessEvaluator(IFitnessEvaluator):

    def __init__(self, evaluation_function):
        super().__init__()

        assert evaluation_function is not None, "Expecting not None evaluation_function"
        assert isinstance(evaluation_function, types.LambdaType), "Expecting evaluation_function to be a Lambda"

        self.evaluation_function = evaluation_function

    def evaluate(self, individual, population):
        assert individual is not None, "Expecting not None individual"
        assert isinstance(individual, IGeneticData), "Expecting individual to be an IGeneticData"

        result = self.evaluation_function(individual, population)
        assert isinstance(result, float), "Expecting result of evaluation_function to be a float"
        return result
