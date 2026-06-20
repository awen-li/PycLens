# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_with_bound_and_unbound_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(map(str, range(10)))
    join = self.partial(str.join, '')
    self.assertEqual(join(data), '0123456789')
    join = self.partial(''.join)
    self.assertEqual(join(data), '0123456789')
