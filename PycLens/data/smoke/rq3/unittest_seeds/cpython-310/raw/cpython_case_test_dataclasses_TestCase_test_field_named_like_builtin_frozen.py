# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_named_like_builtin_frozen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exclusions = {'None', 'True', 'False'}
    builtins_names = sorted((b for b in builtins.__dict__.keys() if not b.startswith('__') and b not in exclusions))
    attributes = [(name, str) for name in builtins_names]
    C = make_dataclass('C', attributes, frozen=True)
    c = C(*[name for name in builtins_names])
    for name in builtins_names:
        self.assertEqual(getattr(c, name), name)
