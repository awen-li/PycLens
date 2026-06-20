# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('x = 0', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '0'           (1, 4) (1, 5)\n    ")
    self.check_tokenize('x = 0xfffffffffff', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '0xfffffffffff' (1, 4) (1, 17)\n    ")
    self.check_tokenize('x = 123141242151251616110', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '123141242151251616110' (1, 4) (1, 25)\n    ")
    self.check_tokenize('x = -15921590215012591', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    OP         '-'           (1, 4) (1, 5)\n    NUMBER     '15921590215012591' (1, 5) (1, 22)\n    ")
