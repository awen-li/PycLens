# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestAscii_test_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ascii = curses.ascii.ascii
    self.assertEqual(ascii('Á'), 'A')
    self.assertEqual(ascii('A'), 'A')
    self.assertEqual(ascii(ord('Á')), ord('A'))
