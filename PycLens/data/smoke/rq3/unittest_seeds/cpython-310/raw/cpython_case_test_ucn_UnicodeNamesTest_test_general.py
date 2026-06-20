# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_general

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    chars = ['LATIN CAPITAL LETTER T', 'LATIN SMALL LETTER H', 'LATIN SMALL LETTER E', 'SPACE', 'LATIN SMALL LETTER R', 'LATIN CAPITAL LETTER E', 'LATIN SMALL LETTER D', 'SPACE', 'LATIN SMALL LETTER f', 'LATIN CAPITAL LeTtEr o', 'LATIN SMaLl LETTER x', 'SPACE', 'LATIN SMALL LETTER A', 'LATIN SMALL LETTER T', 'LATIN SMALL LETTER E', 'SPACE', 'LATIN SMALL LETTER T', 'LATIN SMALL LETTER H', 'LATIN SMALL LETTER E', 'SpAcE', 'LATIN SMALL LETTER S', 'LATIN SMALL LETTER H', 'LATIN small LETTER e', 'LATIN small LETTER e', 'LATIN SMALL LETTER P', 'FULL STOP']
    string = 'The rEd fOx ate the sheep.'
    self.assertEqual(''.join([self.checkletter(*args) for args in zip(chars, string)]), string)
