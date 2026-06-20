# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AllTests_test_all_exported_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actual_all = set(typing.__all__)
    computed_all = {k for (k, v) in vars(typing).items() if k in actual_all or (not k.startswith('_') and k not in typing.io.__all__ and (k not in typing.re.__all__) and (k not in {'io', 're'}) and (not k.endswith(('Meta', '_contra', '_co'))) and (not k.upper() == k) and (getattr(v, '__module__', None) == typing.__name__))}
    self.assertSetEqual(computed_all, actual_all)
