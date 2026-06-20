# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_copy_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyCounter(Counter):
        pass
    c = MyCounter('slartibartfast')
    d = c.copy()
    self.assertEqual(d, c)
    self.assertEqual(len(d), len(c))
    self.assertEqual(type(d), type(c))
