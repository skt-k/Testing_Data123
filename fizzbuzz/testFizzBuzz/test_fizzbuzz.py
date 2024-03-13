import unittest

def fizzbuzz(x):
    result = []
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        expected_result = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
            "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz"
        ]

        result = fizzbuzz(30)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
