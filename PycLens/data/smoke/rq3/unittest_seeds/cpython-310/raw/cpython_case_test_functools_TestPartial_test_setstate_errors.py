# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_setstate_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.partial(signature)
    self.assertRaises(TypeError, f.__setstate__, (capture, (), {}))
    self.assertRaises(TypeError, f.__setstate__, (capture, (), {}, {}, None))
    self.assertRaises(TypeError, f.__setstate__, [capture, (), {}, None])
    self.assertRaises(TypeError, f.__setstate__, (None, (), {}, None))
    self.assertRaises(TypeError, f.__setstate__, (capture, None, {}, None))
    self.assertRaises(TypeError, f.__setstate__, (capture, [], {}, None))
    self.assertRaises(TypeError, f.__setstate__, (capture, (), [], None))
