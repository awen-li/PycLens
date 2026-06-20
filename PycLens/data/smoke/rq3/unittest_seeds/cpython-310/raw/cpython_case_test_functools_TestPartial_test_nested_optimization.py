# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_nested_optimization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    partial = self.partial
    inner = partial(signature, 'asdf')
    nested = partial(inner, bar=True)
    flat = partial(signature, 'asdf', bar=True)
    self.assertEqual(signature(nested), signature(flat))
