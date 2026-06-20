# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestParameterObject_test_signature_parameter_implicit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(ValueError, 'implicit arguments must be passed as positional or keyword arguments, not positional-only'):
        inspect.Parameter('.0', kind=inspect.Parameter.POSITIONAL_ONLY)
    param = inspect.Parameter('.0', kind=inspect.Parameter.POSITIONAL_OR_KEYWORD)
    self.assertEqual(param.kind, inspect.Parameter.POSITIONAL_ONLY)
    self.assertEqual(param.name, 'implicit0')
