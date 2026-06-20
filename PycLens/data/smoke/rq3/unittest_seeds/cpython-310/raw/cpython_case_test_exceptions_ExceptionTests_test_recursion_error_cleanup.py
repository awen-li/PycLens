# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_recursion_error_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass
    wr = None

    def inner():
        nonlocal wr
        c = C()
        wr = weakref.ref(c)
        inner()
    try:
        inner()
    except RecursionError as e:
        self.assertNotEqual(wr(), None)
    else:
        self.fail('RecursionError not raised')
    gc_collect()
    self.assertEqual(wr(), None)
