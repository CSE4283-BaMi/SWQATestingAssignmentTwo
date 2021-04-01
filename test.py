import unittest
import xmlrunner

from assignmentTwo import *

"""
Testing the main menu functionality and input validation
"""
class TestMenu(unittest.TestCase):
    def testBMISelection(self):
        data = 1
        result = menu(data, True)
        self.assertEqual(result, 5)


    def testRetirementSelection(self):
        data = 2
        result = menu(data, True)
        self.assertEqual(result, 3)

    def testQuitSelection(self):
        data = 3
        result = menu(data, True)
        self.assertEqual(result, 2)

    def testValidInput(self):
        data = 4
        result = menu(data, True)
        self.assertEqual(result, 1)

"""
Testing BMI functionality and input validation
"""

class TestBMI(unittest.TestCase):
    def testValidInput(self):
        weight = 150
        heightFT = 6
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, 21)

    def testInvalidWeight(self):
        weight = "f"
        heightFT = 6
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, False)

    def testInvalidWeightTwo(self):
        weight = -1
        heightFT = 6
        heightIn = 0
        data = (weight, heightFT, heightIn)
        result = bmi(data, True)
        self.assertEqual(result, False)

    def testInvalidHeightFT(self):
        weight = 150
        heightFT = "six"
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, False)
    
    def testInvalidHeightFTTwo(self):
        weight = 150
        heightFT = -1
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, False)

    def testInvalidHeightFTThree(self):
        weight = 150
        heightFT = "6 feet"
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, False)

    def testInvalidHeightIN(self):
        weight = 150
        heightFT = 6
        heightIN = "zero"
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, False)

    def testInvalidHeightINTwo(self):
        weight = 150
        heightFT = 6
        heightIN = -1
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, False)
    
    def testInvalidHeightINThree(self):
        weight = 150
        heightFT = 6
        heightIN = 14
        data = (weight, heightFT, heightIN)
        result = bmi(data, True)
        self.assertEqual(result, False)

    def testInvalidHeightINFour(self):
        weight = 150
        heightFT = 6
        heightIN = "0 inches"
        data = (weight, heightFT, heightIN)
        result = bmi(data, testMode = True)
        self.assertEqual(result, False)

"""
Testing the retirement calculator
"""
class TestRetirement(unittest.TestCase):
    def testValidInput(self):
        age = 21
        salary = 50000
        percentSaved = 25
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, 81)

    def testInvalidAge(self):
        age = -1
        salary = 50000
        percentSaved = 25
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidAgeTwo(self):
        age = "Twenty One"
        salary = 50000
        percentSaved = 25
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidAgeThree(self):
        age = 100
        salary = 50000
        percentSaved = 25
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidSalary(self):
        age = 21
        salary = -1
        percentSaved = 25
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidSalaryTwo(self):
        age = 21
        salary = "Fifty Thousand Dollars"
        percentSaved = 25
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidSaved(self):
        age = 21
        salary = 50000
        percentSaved = -25
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidSavedTwo(self):
        age = 21
        salary = 50000
        percentSaved = "Twenty Five Percent"
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidSavedThree(self):
        age = 21
        salary = 50000
        percentSaved = 125
        goal = 1000000
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidGoal(self):
        age = 21
        salary = 50000
        percentSaved = 25
        goal = -24
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)

    def testInvalidGoalTwo(self):
        age = 21
        salary = 50000
        percentSaved = 25
        goal = "One Million Dollars"
        data = (age, salary, percentSaved, goal)
        result = retirement(data, True)
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="python_tests_xml"),
        failfast = False, 
        buffer = False, 
        catchbreak = False)
