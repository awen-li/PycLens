# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_wrapper_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        yield

    @types.coroutine
    def coro():
        return gen()
    wrapper = coro()
    self.assertIn('GeneratorWrapper', repr(wrapper))
    self.assertEqual(repr(wrapper), str(wrapper))
    self.assertTrue(set(dir(wrapper)).issuperset({'__await__', '__iter__', '__next__', 'cr_code', 'cr_running', 'cr_frame', 'gi_code', 'gi_frame', 'gi_running', 'send', 'close', 'throw'}))
