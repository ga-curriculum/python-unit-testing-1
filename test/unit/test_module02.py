import unittest
import inspect

debug = True


class TestClass02(unittest.TestCase):
    def test_case02(self):
        # for info in inspect.stack():
        #     print(info.frame)
        #     print(info.filename)
        #     print(info.lineno)
        #     print(info.function)
        #     print(info.code_context)
        #     print('')
        print("\nRunning Test Method : " + inspect.stack()[0][3])

    def test_case01(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
