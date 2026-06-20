# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_python_lists

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(list):

        def __getitem__(self, i):
            if isinstance(i, slice):
                return (i.start, i.stop)
            return list.__getitem__(self, i) + 100
    a = C()
    a.extend([0, 1, 2])
    self.assertEqual(a[0], 100)
    self.assertEqual(a[1], 101)
    self.assertEqual(a[2], 102)
    self.assertEqual(a[100:200], (100, 200))
