# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_tabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize('def f():\n\tif x\n        \tpass', "    NAME       'def'         (1, 0) (1, 3)\n    NAME       'f'           (1, 4) (1, 5)\n    OP         '('           (1, 5) (1, 6)\n    OP         ')'           (1, 6) (1, 7)\n    OP         ':'           (1, 7) (1, 8)\n    NEWLINE    '\\n'          (1, 8) (1, 9)\n    INDENT     '\\t'          (2, 0) (2, 1)\n    NAME       'if'          (2, 1) (2, 3)\n    NAME       'x'           (2, 4) (2, 5)\n    NEWLINE    '\\n'          (2, 5) (2, 6)\n    INDENT     '        \\t'  (3, 0) (3, 9)\n    NAME       'pass'        (3, 9) (3, 13)\n    DEDENT     ''            (4, 0) (4, 0)\n    DEDENT     ''            (4, 0) (4, 0)\n    ")
