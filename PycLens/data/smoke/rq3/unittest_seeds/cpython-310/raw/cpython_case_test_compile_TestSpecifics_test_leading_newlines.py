# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_leading_newlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s256 = ''.join(['\n'] * 256 + ['spam'])
    co = compile(s256, 'fn', 'exec')
    self.assertEqual(co.co_firstlineno, 1)
    self.assertEqual(list(co.co_lines()), [(0, 8, 257)])
