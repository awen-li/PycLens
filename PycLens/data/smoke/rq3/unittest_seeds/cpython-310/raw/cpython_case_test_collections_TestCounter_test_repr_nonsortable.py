# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_repr_nonsortable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = Counter(a=2, b=None)
    r = repr(c)
    self.assertIn("'a': 2", r)
    self.assertIn("'b': None", r)
