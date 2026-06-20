# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_boolean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('[BOOLTEST]\nT1{equals}1\nT2{equals}TRUE\nT3{equals}True\nT4{equals}oN\nT5{equals}yes\nF1{equals}0\nF2{equals}FALSE\nF3{equals}False\nF4{equals}oFF\nF5{equals}nO\nE1{equals}2\nE2{equals}foo\nE3{equals}-1\nE4{equals}0.1\nE5{equals}FALSE AND MORE'.format(equals=self.delimiters[0]))
    for x in range(1, 5):
        self.assertTrue(cf.getboolean('BOOLTEST', 't%d' % x))
        self.assertFalse(cf.getboolean('BOOLTEST', 'f%d' % x))
        self.assertRaises(ValueError, cf.getboolean, 'BOOLTEST', 'e%d' % x)
