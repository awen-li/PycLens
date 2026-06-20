# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callable_proxy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = Callable()
    ref1 = weakref.proxy(o)
    self.check_proxy(o, ref1)
    self.assertIs(type(ref1), weakref.CallableProxyType, 'proxy is not of callable type')
    ref1('twinkies!')
    self.assertEqual(o.bar, 'twinkies!', 'call through proxy not passed through to original')
    ref1(x='Splat.')
    self.assertEqual(o.bar, 'Splat.', 'call through proxy not passed through to original')
    self.assertRaises(TypeError, ref1)
    self.assertRaises(TypeError, ref1, 1, 2, 3)
