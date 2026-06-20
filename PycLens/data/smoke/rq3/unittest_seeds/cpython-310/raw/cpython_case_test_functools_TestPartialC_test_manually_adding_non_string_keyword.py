# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialC_test_manually_adding_non_string_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture)
    p.keywords[1234] = 'value'
    r = repr(p)
    self.assertIn('1234', r)
    self.assertIn("'value'", r)
    with self.assertRaises(TypeError):
        p()
