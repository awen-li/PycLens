# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestParameterObject_test_signature_parameter_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = inspect.Parameter('foo', default=10, kind=inspect.Parameter.POSITIONAL_ONLY)
    self.assertEqual(p.name, 'foo')
    self.assertEqual(p.default, 10)
    self.assertIs(p.annotation, p.empty)
    self.assertEqual(p.kind, inspect.Parameter.POSITIONAL_ONLY)
    with self.assertRaisesRegex(ValueError, "value '123' is not a valid Parameter.kind"):
        inspect.Parameter('foo', default=10, kind='123')
    with self.assertRaisesRegex(ValueError, 'not a valid parameter name'):
        inspect.Parameter('1', kind=inspect.Parameter.VAR_KEYWORD)
    with self.assertRaisesRegex(TypeError, 'name must be a str'):
        inspect.Parameter(None, kind=inspect.Parameter.VAR_KEYWORD)
    with self.assertRaisesRegex(ValueError, 'is not a valid parameter name'):
        inspect.Parameter('$', kind=inspect.Parameter.VAR_KEYWORD)
    with self.assertRaisesRegex(ValueError, 'is not a valid parameter name'):
        inspect.Parameter('.a', kind=inspect.Parameter.VAR_KEYWORD)
    with self.assertRaisesRegex(ValueError, 'cannot have default values'):
        inspect.Parameter('a', default=42, kind=inspect.Parameter.VAR_KEYWORD)
    with self.assertRaisesRegex(ValueError, 'cannot have default values'):
        inspect.Parameter('a', default=42, kind=inspect.Parameter.VAR_POSITIONAL)
    p = inspect.Parameter('a', default=42, kind=inspect.Parameter.POSITIONAL_OR_KEYWORD)
    with self.assertRaisesRegex(ValueError, 'cannot have default values'):
        p.replace(kind=inspect.Parameter.VAR_POSITIONAL)
    self.assertTrue(repr(p).startswith('<Parameter'))
    self.assertTrue('"a=42"' in repr(p))
