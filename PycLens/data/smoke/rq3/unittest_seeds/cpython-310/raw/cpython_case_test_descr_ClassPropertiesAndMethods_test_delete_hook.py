# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_delete_hook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    log = []

    class C(object):

        def __del__(self):
            log.append(1)
    c = C()
    self.assertEqual(log, [])
    del c
    support.gc_collect()
    self.assertEqual(log, [1])

    class D(object):
        pass
    d = D()
    try:
        del d[0]
    except TypeError:
        pass
    else:
        self.fail("invalid del() didn't raise TypeError")
