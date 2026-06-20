# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_shadowed_global

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a_global = 'really a local'
    self.assertEqual(f'g:{a_global}', 'g:really a local')
    self.assertEqual(f'g:{a_global!r}', "g:'really a local'")
    a_local = 'local variable'
    self.assertEqual(f'g:{a_global} l:{a_local}', 'g:really a local l:local variable')
    self.assertEqual(f'g:{a_global!r}', "g:'really a local'")
    self.assertEqual(f'g:{a_global} l:{a_local!r}', "g:really a local l:'local variable'")
