# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_repr_source

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = repr(unittest)
    starts_with = "<module 'unittest' from '"
    ends_with = "__init__.py'>"
    self.assertEqual(r[:len(starts_with)], starts_with, '{!r} does not start with {!r}'.format(r, starts_with))
    self.assertEqual(r[-len(ends_with):], ends_with, '{!r} does not end with {!r}'.format(r, ends_with))
