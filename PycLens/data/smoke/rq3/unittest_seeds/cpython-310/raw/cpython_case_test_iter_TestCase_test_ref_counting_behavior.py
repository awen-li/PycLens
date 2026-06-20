# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_ref_counting_behavior

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        count = 0

        def __new__(cls):
            cls.count += 1
            return object.__new__(cls)

        def __del__(self):
            cls = self.__class__
            assert cls.count > 0
            cls.count -= 1
    x = C()
    self.assertEqual(C.count, 1)
    del x
    self.assertEqual(C.count, 0)
    l = [C(), C(), C()]
    self.assertEqual(C.count, 3)
    try:
        (a, b) = iter(l)
    except ValueError:
        pass
    del l
    self.assertEqual(C.count, 0)
