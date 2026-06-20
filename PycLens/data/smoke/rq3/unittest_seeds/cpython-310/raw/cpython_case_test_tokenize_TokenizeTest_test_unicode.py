# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_tokenize("Örter = u'places'\ngrün = U'green'", '    NAME       \'Örter\'       (1, 0) (1, 5)\n    OP         \'=\'           (1, 6) (1, 7)\n    STRING     "u\'places\'"   (1, 8) (1, 17)\n    NEWLINE    \'\\n\'          (1, 17) (1, 18)\n    NAME       \'grün\'        (2, 0) (2, 4)\n    OP         \'=\'           (2, 5) (2, 6)\n    STRING     "U\'green\'"    (2, 7) (2, 15)\n    ')
