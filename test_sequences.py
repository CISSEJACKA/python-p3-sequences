# test_sequences.py

import io
import sys
from sequences import print_fibonacci

class TestPrintFibonacci:
    '''Tests for print_fibonacci()'''

    def test_print_fibonacci_zero(self):
        '''Prints empty list when length = 0'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(0)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[]\n'

    def test_print_fibonacci_one(self):
        '''Prints [0] when length = 1'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(1)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0]\n'

    def test_print_fibonacci_two(self):
        '''Prints [0, 1] when length = 2'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(2)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1]\n'

    def test_print_fibonacci_ten(self):
        '''Prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] when length = 10'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(10)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n'

# If running pytest from command line:
# Ensure pytest is installed (`pip install pytest`) and run `pytest` in the same directory as this script.
