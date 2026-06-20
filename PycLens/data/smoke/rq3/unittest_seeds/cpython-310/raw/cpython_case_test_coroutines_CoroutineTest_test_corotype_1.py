# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_corotype_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ct = types.CoroutineType
    self.assertIn('into coroutine', ct.send.__doc__)
    self.assertIn('inside coroutine', ct.close.__doc__)
    self.assertIn('in coroutine', ct.throw.__doc__)
    self.assertIn('of the coroutine', ct.__dict__['__name__'].__doc__)
    self.assertIn('of the coroutine', ct.__dict__['__qualname__'].__doc__)
    self.assertEqual(ct.__name__, 'coroutine')

    async def f():
        pass
    c = f()
    self.assertIn('coroutine object', repr(c))
    c.close()
