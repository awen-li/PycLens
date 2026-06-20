# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_3114

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyObject:

        def __del__(self):
            nonlocal e
            e = sys.exc_info()
    e = ()
    try:
        raise Exception(MyObject())
    except:
        pass
    gc_collect()
    self.assertEqual(e, (None, None, None))
