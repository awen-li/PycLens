# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_selector

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize("import sys, time\nx = sys.modules['time'].time()", '    NAME       \'import\'      (1, 0) (1, 6)\n    NAME       \'sys\'         (1, 7) (1, 10)\n    OP         \',\'           (1, 10) (1, 11)\n    NAME       \'time\'        (1, 12) (1, 16)\n    NEWLINE    \'\\n\'          (1, 16) (1, 17)\n    NAME       \'x\'           (2, 0) (2, 1)\n    OP         \'=\'           (2, 2) (2, 3)\n    NAME       \'sys\'         (2, 4) (2, 7)\n    OP         \'.\'           (2, 7) (2, 8)\n    NAME       \'modules\'     (2, 8) (2, 15)\n    OP         \'[\'           (2, 15) (2, 16)\n    STRING     "\'time\'"      (2, 16) (2, 22)\n    OP         \']\'           (2, 22) (2, 23)\n    OP         \'.\'           (2, 23) (2, 24)\n    NAME       \'time\'        (2, 24) (2, 28)\n    OP         \'(\'           (2, 28) (2, 29)\n    OP         \')\'           (2, 29) (2, 30)\n    ')
