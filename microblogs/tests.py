from django.test import TestCase

# Create your tests here.
#
# def factorial(integer):
#     if integer < 0:
#         raise ValueError(f'Factorial requires a non-negative integer, got {integer}')
#
#     result = 1
#     for i in range(2, integer+1):
#         result *= i
#     return result
#
# class UnitTstCase(TestCase):
#     def test_factorial_of_0(self):
#         self.assertEqual(1, factorial(0))
#
#     def test_factorial_of_1(self):
#         self.assertEqual(1, factorial(1))
#
#     def test_factorial_of_2(self):
#         self.assertEqual(2, factorial(2))
#
#     def test_factorial_of_3(self):
#         self.assertEqual(6, factorial(3))
#
#     def test_factorial_of_5(self):
#         self.assertEqual(120, factorial(5))
#
#     def test_factorial_of_10(self):
#         self.assertEqual(3628800, factorial(10))
#
#     def test_factorial_of_minus1(self):
#         with self.assertRaises(ValueError):
#             factorial(-1)
