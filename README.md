# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Unit Testing - Part 1

| Title                        | Type   | Duration | Author               |
|------------------------------|--------|----------|----------------------|
| Python Unit Testing - Part 1 | Lesson | 2:00     | Suresh Melvin Sigera |

## Objectives

*After this lesson, students will be able to:*

- Write simple unit test
- Implementing a sample script using the Selenium WebDriver Python client library

### What is Unit Testing?

A unit test is a kind of test that aims to cover the application's functionality at the most *basic level possible*. It
is very **imperative** to **test every single unit of code**, usually a function or a method, in isolation. This is in
order to determine if it will perform as expected under certain circumstances. As soon as you break testing down to this
level, you can be confident that each part of the application will behave as expected.

You'll be able to include edge cases where the unexpected happens, and will be prepared to handle them accordingly.

To put it another way, a unit test is a piece of code which imports parts of the code with the business logic and
executes that logic, asserting multiple scenarios with the idea of guaranteeing certain conditions. There are some
traits that unit tests must have, such as:

- `Isolation`:In order to ensure that unit tests are completely independent of any external agents, they have to focus
  solely on the business logic that needs to be tested. In order to take advantage of this feature, they do not use a
  database, they do not execute HTTP requests, and so forth. In order to achieve isolation, the tests must also be
  independent among themselves: they must be able to run in any order and without being dependent on anything that might
  have happened previously.
- `Performance`: It is essential that unit tests run as quickly as possible. It is intended to run these programs
  multiple times, repeatedly in order to obtain the best results.
- `Repeatability`: As far as the software is concerned, unit tests must be able to objectively assess the status of the
  software in a deterministic manner. This means that the test results should be able to be repeated by the same tester
  again and again. Whenever a unit test fails, the test must keep failing until the code is fixed, as this is how unit
  tests assess the status of the code. If a test passes and no changes are made to the code, then the test should be
  expected to pass in the future. It is critical that your tests are not flaky or random in any way.
- `Self-validating`: In order for a unit test to produce a result, it must be executed. The process of completing the
  form should not require any additional steps; It is much easier to interpret the unit test (much less manual
  intervention is required).

### What Should You Test?

### Using Unittest

```python
import unittest


class TestClass01(unittest.TestCase):
    def test_case_01(self):
        my_name_str = "Suresh Sigera "
        my_int = 1000
        self.assertTrue(isinstance(my_name_str, str))
        self.assertTrue(isinstance(my_int, int))

    def test_case_02(self):
        my_pi = 3.14
        self.assertFalse(isinstance(my_pi, int))


if __name__ == '__main__':
    unittest.main()

```

In the code above, the `import unittest` statement imports the unittest module. `TestClass01` is the test class. It is
subclassed from the [TestCase](https://docs.python.org/3/library/unittest.html) class in the unittest module.

The class methods `test_case01()` and `test_case02(`) are test methods, as their names start with test_ (Later in the
lesson, you will learn about the guidelines and naming conventions that should be followed when writing tests).

The `assertTrue()` and `assertFalse()` methods are assertion methods which check if the argument
passed to them is `True` or `False`, respectively.

If the argument meets the assert condition, the test case passes; otherwise, it fails. `unittest.main()` is the test
runner. We will explore more assert methods in detail later.

Run the following command in order to run the test: `python3 test_module01.py -v`

Since verbosity is disabled by default, the `-v` option will give you more detailed information about the test.

```text
(venv) Sureshs-MBP:unit suresh$ python3 test_module01.py -v
test_case_01 (__main__.TestClass01) ... ok
test_case_02 (__main__.TestClass01) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
(venv) Sureshs-MBP:unit suresh$ 

```

### References

- [TestCase](https://docs.python.org/3/library/unittest.html)
