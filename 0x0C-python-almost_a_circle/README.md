# Almost a Circle

This project was completed as part of the Full Stack Software Engineering curriculum at ALX. It serves as an educational exercise to understand various concepts in Python, such as unit testing, serialization, deserialization, JSON, and working with arguments and keyword arguments (args and kwargs).

## Technologies

- Python Scripts: Written with Python 3.4.3
- Tested on: Ubuntu 14.04 LTS

## Files

Inside the `models` folder:

| Filename       | Description                                                |
| ---------------| ---------------------------------------------------------- |
| `__init__.py`  | Script that converts the directory as a package.          |
| `base.py`      | Base class of geometrical instances.                      |
| `rectangle.py` | Class that inherits attributes and references from the Base class. |
| `square.py`    | Class that inherits attributes and references from the Square class. |

Each class contains public/private attributes, class and static methods. Also, these classes raise exceptions when required.

Inside the `tests/test_models` folder:

| Filename           | Description                                     |
| -------------------| ----------------------------------------------- |
| `__init__.py`      | Script that converts the directory as a package. |
| `test_base.py`     | Module that contains unit tests for the Base class. |
| `test_rectangle.py`| Module that contains unit tests for the Rectangle class. |
| `test_square.py`   | Module that contains unit tests for the Square class. |

## Running the Tests

To run the unit tests and check the functionality of the classes, you can execute the test files in the `tests` folder.

For example, to run the tests for the `Base` class, you can use the following command:

```bash
python -m unittest tests.test_models.test_base

