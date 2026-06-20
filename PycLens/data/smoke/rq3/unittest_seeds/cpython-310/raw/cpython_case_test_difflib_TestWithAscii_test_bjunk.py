# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestWithAscii_test_bjunk

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sm = difflib.SequenceMatcher(isjunk=lambda x: x == ' ', a='a' * 40 + 'b' * 40, b='a' * 44 + 'b' * 40)
    self.assertEqual(sm.bjunk, set())
    sm = difflib.SequenceMatcher(isjunk=lambda x: x == ' ', a='a' * 40 + 'b' * 40, b='a' * 44 + 'b' * 40 + ' ' * 20)
    self.assertEqual(sm.bjunk, {' '})
    sm = difflib.SequenceMatcher(isjunk=lambda x: x in [' ', 'b'], a='a' * 40 + 'b' * 40, b='a' * 44 + 'b' * 40 + ' ' * 20)
    self.assertEqual(sm.bjunk, {' ', 'b'})
