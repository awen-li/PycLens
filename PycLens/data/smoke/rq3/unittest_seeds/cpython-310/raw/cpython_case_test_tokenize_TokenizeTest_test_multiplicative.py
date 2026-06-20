# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_multiplicative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('x = 1//1*1/5*12%0x12@42', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 4) (1, 5)\n    OP         '//'          (1, 5) (1, 7)\n    NUMBER     '1'           (1, 7) (1, 8)\n    OP         '*'           (1, 8) (1, 9)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '/'           (1, 10) (1, 11)\n    NUMBER     '5'           (1, 11) (1, 12)\n    OP         '*'           (1, 12) (1, 13)\n    NUMBER     '12'          (1, 13) (1, 15)\n    OP         '%'           (1, 15) (1, 16)\n    NUMBER     '0x12'        (1, 16) (1, 20)\n    OP         '@'           (1, 20) (1, 21)\n    NUMBER     '42'          (1, 21) (1, 23)\n    ")
