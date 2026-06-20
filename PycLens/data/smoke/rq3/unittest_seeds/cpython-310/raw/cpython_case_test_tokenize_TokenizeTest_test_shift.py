# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_shift

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('x = 1 << 1 >> 5', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 4) (1, 5)\n    OP         '<<'          (1, 6) (1, 8)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '>>'          (1, 11) (1, 13)\n    NUMBER     '5'           (1, 14) (1, 15)\n    ")
