# Micropsi Coding Challenge

### Setup
To test the code, you require a minimum python version of `3.5.0`
The module can be installed into a virtual environment or directly into your local pc or a project. The cobe base lives on [github](https://github.com/Basillica/micropsi).

To install from the github reposition, use the command
```bash
pip3 install git+ssh://git@github.com/Basillica/micropsi.git
```
This works either from a virtual environment, locally or inside a regular project.
Also from inside project, the module can be installed using the command
```bash
python3 setup.py install
```
To test this fully, it is best inside a virtual environment.

### Test
Create a file `main.py`, inside the package thus `pip3 install git+ssh://git@github.com/Basillica/micropsi.git`.
Inside `main.py`
```python
from micropsi import find_minimum
print(find_minimum([1,2,3,4]))
```
The output should be `1`.
