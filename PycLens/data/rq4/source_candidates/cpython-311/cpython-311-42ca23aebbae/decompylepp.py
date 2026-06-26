# Source Generated with Decompyle++
# File: cpython-311-42ca23aebbae.pyc (Python 3.11)

__pybcsec_seed__ =     self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('x = 3.14159', "    NAME       'x'           (1, 0) (1, 1)\n    EQUAL      '='           (1, 2) (1, 3)\n    NUMBER     '3.14159'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = 314159.', "    NAME       'x'           (1, 0) (1, 1)\n    EQUAL      '='           (1, 2) (1, 3)\n    NUMBER     '314159.'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = .314159', "    NAME       'x'           (1, 0) (1, 1)\n    EQUAL      '='           (1, 2) (1, 3)\n    NUMBER     '.314159'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = 3e14159', "    NAME       'x'           (1, 0) (1, 1)\n    EQUAL      '='           (1, 2) (1, 3)\n    NUMBER     '3e14159'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = 3E123', "    NAME       'x'           (1, 0) (1, 1)\n    EQUAL      '='           (1, 2) (1, 3)\n    NUMBER     '3E123'       (1, 4) (1, 9)\n    ")
    self.check_tokenize('x+y = 3e-1230', "    NAME       'x'           (1, 0) (1, 1)\n    PLUS       '+'           (1, 1) (1, 2)\n    NAME       'y'           (1, 2) (1, 3)\n    EQUAL      '='           (1, 4) (1, 5)\n    NUMBER     '3e-1230'     (1, 6) (1, 13)\n    ")
    self.check_tokenize('x = 3.14e159', "    NAME       'x'           (1, 0) (1, 1)\n    EQUAL      '='           (1, 2) (1, 3)\n    NUMBER     '3.14e159'    (1, 4) (1, 12)\n    ")

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
