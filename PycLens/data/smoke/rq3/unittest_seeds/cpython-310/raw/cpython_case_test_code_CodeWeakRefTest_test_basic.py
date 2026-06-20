# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CodeWeakRefTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    namespace = {}
    exec('def f(): pass', globals(), namespace)
    f = namespace['f']
    del namespace
    self.called = False

    def callback(code):
        self.called = True
    coderef = weakref.ref(f.__code__, callback)
    self.assertTrue(bool(coderef()))
    del f
    gc_collect()
    self.assertFalse(bool(coderef()))
    self.assertTrue(self.called)
