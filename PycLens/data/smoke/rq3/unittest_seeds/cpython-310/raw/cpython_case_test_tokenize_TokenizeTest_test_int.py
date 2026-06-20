# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('0xff <= 255', "    NUMBER     '0xff'        (1, 0) (1, 4)\n    OP         '<='          (1, 5) (1, 7)\n    NUMBER     '255'         (1, 8) (1, 11)\n    ")
    self.check_tokenize('0b10 <= 255', "    NUMBER     '0b10'        (1, 0) (1, 4)\n    OP         '<='          (1, 5) (1, 7)\n    NUMBER     '255'         (1, 8) (1, 11)\n    ")
    self.check_tokenize('0o123 <= 0O123', "    NUMBER     '0o123'       (1, 0) (1, 5)\n    OP         '<='          (1, 6) (1, 8)\n    NUMBER     '0O123'       (1, 9) (1, 14)\n    ")
    self.check_tokenize('1234567 > ~0x15', "    NUMBER     '1234567'     (1, 0) (1, 7)\n    OP         '>'           (1, 8) (1, 9)\n    OP         '~'           (1, 10) (1, 11)\n    NUMBER     '0x15'        (1, 11) (1, 15)\n    ")
    self.check_tokenize('2134568 != 1231515', "    NUMBER     '2134568'     (1, 0) (1, 7)\n    OP         '!='          (1, 8) (1, 10)\n    NUMBER     '1231515'     (1, 11) (1, 18)\n    ")
    self.check_tokenize('(-124561-1) & 200000000', "    OP         '('           (1, 0) (1, 1)\n    OP         '-'           (1, 1) (1, 2)\n    NUMBER     '124561'      (1, 2) (1, 8)\n    OP         '-'           (1, 8) (1, 9)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         ')'           (1, 10) (1, 11)\n    OP         '&'           (1, 12) (1, 13)\n    NUMBER     '200000000'   (1, 14) (1, 23)\n    ")
    self.check_tokenize('0xdeadbeef != -1', "    NUMBER     '0xdeadbeef'  (1, 0) (1, 10)\n    OP         '!='          (1, 11) (1, 13)\n    OP         '-'           (1, 14) (1, 15)\n    NUMBER     '1'           (1, 15) (1, 16)\n    ")
    self.check_tokenize('0xdeadc0de & 12345', "    NUMBER     '0xdeadc0de'  (1, 0) (1, 10)\n    OP         '&'           (1, 11) (1, 12)\n    NUMBER     '12345'       (1, 13) (1, 18)\n    ")
    self.check_tokenize('0xFF & 0x15 | 1234', "    NUMBER     '0xFF'        (1, 0) (1, 4)\n    OP         '&'           (1, 5) (1, 6)\n    NUMBER     '0x15'        (1, 7) (1, 11)\n    OP         '|'           (1, 12) (1, 13)\n    NUMBER     '1234'        (1, 14) (1, 18)\n    ")
