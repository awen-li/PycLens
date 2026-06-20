# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('@staticmethod\ndef foo(x,y): pass', "    OP         '@'           (1, 0) (1, 1)\n    NAME       'staticmethod' (1, 1) (1, 13)\n    NEWLINE    '\\n'          (1, 13) (1, 14)\n    NAME       'def'         (2, 0) (2, 3)\n    NAME       'foo'         (2, 4) (2, 7)\n    OP         '('           (2, 7) (2, 8)\n    NAME       'x'           (2, 8) (2, 9)\n    OP         ','           (2, 9) (2, 10)\n    NAME       'y'           (2, 10) (2, 11)\n    OP         ')'           (2, 11) (2, 12)\n    OP         ':'           (2, 12) (2, 13)\n    NAME       'pass'        (2, 14) (2, 18)\n    ")
