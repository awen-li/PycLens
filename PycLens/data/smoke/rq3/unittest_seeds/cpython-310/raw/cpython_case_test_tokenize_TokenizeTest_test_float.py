# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('x = 3.14159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3.14159'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = 314159.', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '314159.'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = .314159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '.314159'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = 3e14159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3e14159'     (1, 4) (1, 11)\n    ")
    self.check_tokenize('x = 3E123', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3E123'       (1, 4) (1, 9)\n    ")
    self.check_tokenize('x+y = 3e-1230', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '+'           (1, 1) (1, 2)\n    NAME       'y'           (1, 2) (1, 3)\n    OP         '='           (1, 4) (1, 5)\n    NUMBER     '3e-1230'     (1, 6) (1, 13)\n    ")
    self.check_tokenize('x = 3.14e159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3.14e159'    (1, 4) (1, 12)\n    ")
