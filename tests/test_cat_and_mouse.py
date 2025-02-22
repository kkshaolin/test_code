from my_tests_code.cat_and_mouse import cat_and_mouse
import unittest

class CatAndMouseTest(unittest.TestCase):
    def test_give_1_2_3_should_be_Cat_B(self):
        # arrange
        x = 1
        y = 2
        z = 3
        expected_output = "Cat B"
        expected = "Cat B"

        # act
        result = cat_and_mouse.cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(result, expected, f'Should be {expected_output}')

    def test_give_1_3_2_should_be_Cat_A(self):
        # arrange
        x = 1
        y = 3
        z = 2
        expected_output = "Cat A"
        expected = "Cat A"

        # act
        result = cat_and_mouse.cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(result, expected, f'Should be {expected_output}')

    def test_give_1_1_2_should_be_Mouse_C(self):
        # arrange
        x = 1
        y = 1
        z = 2
        expected_output = "Mouse C"
        expected = "Mouse C"

        # act
        result = cat_and_mouse.cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(result, expected, f'Should be {expected_output}')

    def test_give_1_1_1_should_be_Mouse_C(self):
        # arrange
        x = 1
        y = 1
        z = 1
        expected_output = "Mouse C"
        expected = "Mouse C"

        # act
        result = cat_and_mouse.cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(result, expected, f'Should be {expected_output}')