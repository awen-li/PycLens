# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_additive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('x = 1 - y + 15 - 1 + 0x124 + z + a[5]', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 4) (1, 5)\n    OP         '-'           (1, 6) (1, 7)\n    NAME       'y'           (1, 8) (1, 9)\n    OP         '+'           (1, 10) (1, 11)\n    NUMBER     '15'          (1, 12) (1, 14)\n    OP         '-'           (1, 15) (1, 16)\n    NUMBER     '1'           (1, 17) (1, 18)\n    OP         '+'           (1, 19) (1, 20)\n    NUMBER     '0x124'       (1, 21) (1, 26)\n    OP         '+'           (1, 27) (1, 28)\n    NAME       'z'           (1, 29) (1, 30)\n    OP         '+'           (1, 31) (1, 32)\n    NAME       'a'           (1, 33) (1, 34)\n    OP         '['           (1, 34) (1, 35)\n    NUMBER     '5'           (1, 35) (1, 36)\n    OP         ']'           (1, 36) (1, 37)\n    ")
