# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_subtype_resurrection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        container = []

        def __del__(self):
            C.container.append(self)
    c = C()
    c.attr = 42
    del c
    support.gc_collect()
    self.assertEqual(len(C.container), 1)
    del C.__del__
