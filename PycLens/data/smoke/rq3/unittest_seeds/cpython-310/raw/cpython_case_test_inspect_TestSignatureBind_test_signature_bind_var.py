# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(*args, **kwargs):
        return (args, kwargs)
    self.assertEqual(self.call(test), ((), {}))
    self.assertEqual(self.call(test, 1), ((1,), {}))
    self.assertEqual(self.call(test, 1, 2), ((1, 2), {}))
    self.assertEqual(self.call(test, foo='bar'), ((), {'foo': 'bar'}))
    self.assertEqual(self.call(test, 1, foo='bar'), ((1,), {'foo': 'bar'}))
    self.assertEqual(self.call(test, args=10), ((), {'args': 10}))
    self.assertEqual(self.call(test, 1, 2, foo='bar'), ((1, 2), {'foo': 'bar'}))
