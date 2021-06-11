from typing import Union
import unittest


# write your function here
def population_density(population: Union[float, int], density: Union[float, int]) -> Union[float, int]:
    return population / density


# test cases for your function
# test1 = population_density(10, 1)
# expected_result1 = 10
# print("expected result: {}, actual result: {}".format(expected_result1, test1))
#
# test2 = population_density(864816, 121.4)
# expected_result2 = 7123.6902801
# print("expected result: {}, actual result: {}".format(expected_result2, test2))


class TestPopulationDensity(unittest.TestCase):

    def testPopulationDensity(self):
        self.assertEqual(population_density(10, 1), 10.0)

    def testPopulationDensity2(self):
        self.assertEqual(population_density(864816, 121.4), 7123.690280065897)