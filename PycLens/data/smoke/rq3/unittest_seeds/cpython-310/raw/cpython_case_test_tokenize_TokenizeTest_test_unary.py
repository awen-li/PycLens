# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_unary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('~1 ^ 1 & 1 |1 ^ -1', "    OP         '~'           (1, 0) (1, 1)\n    NUMBER     '1'           (1, 1) (1, 2)\n    OP         '^'           (1, 3) (1, 4)\n    NUMBER     '1'           (1, 5) (1, 6)\n    OP         '&'           (1, 7) (1, 8)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '|'           (1, 11) (1, 12)\n    NUMBER     '1'           (1, 12) (1, 13)\n    OP         '^'           (1, 14) (1, 15)\n    OP         '-'           (1, 16) (1, 17)\n    NUMBER     '1'           (1, 17) (1, 18)\n    ")
    self.check_tokenize('-1*1/1+1*1//1 - ---1**1', "    OP         '-'           (1, 0) (1, 1)\n    NUMBER     '1'           (1, 1) (1, 2)\n    OP         '*'           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 3) (1, 4)\n    OP         '/'           (1, 4) (1, 5)\n    NUMBER     '1'           (1, 5) (1, 6)\n    OP         '+'           (1, 6) (1, 7)\n    NUMBER     '1'           (1, 7) (1, 8)\n    OP         '*'           (1, 8) (1, 9)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '//'          (1, 10) (1, 12)\n    NUMBER     '1'           (1, 12) (1, 13)\n    OP         '-'           (1, 14) (1, 15)\n    OP         '-'           (1, 16) (1, 17)\n    OP         '-'           (1, 17) (1, 18)\n    OP         '-'           (1, 18) (1, 19)\n    NUMBER     '1'           (1, 19) (1, 20)\n    OP         '**'          (1, 20) (1, 22)\n    NUMBER     '1'           (1, 22) (1, 23)\n    ")
