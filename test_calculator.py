import unittest
from calculator import Calculator
from io import StringIO
import sys

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    # Redirect stdout to capture the output of the test runner
    output = StringIO()
    runner = unittest.TextTestRunner(stream=output, verbosity=2)
    result = unittest.main(testRunner=runner, exit=False)

    # Parse the output to extract test results
    output.seek(0)
    result_text = output.read()
    
    # Generate HTML report
    html_content = f"""
    <html>
    <head>
        <title>Unit Test Report</title>
    </head>
    <body>
        <h1>Unit Test Report</h1>
        <pre>{result_text}</pre>
    </body>
    </html>
    """

    with open('test-reports/results.html', 'w') as f:
        f.write(html_content)
    
    print("HTML report generated: test-reports/results.html")
