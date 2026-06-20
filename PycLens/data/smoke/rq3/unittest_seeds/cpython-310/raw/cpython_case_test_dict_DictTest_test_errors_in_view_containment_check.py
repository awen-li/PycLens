# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_errors_in_view_containment_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __eq__(self, other):
            raise RuntimeError
    d1 = {1: C()}
    d2 = {1: C()}
    with self.assertRaises(RuntimeError):
        d1.items() == d2.items()
    with self.assertRaises(RuntimeError):
        d1.items() != d2.items()
    with self.assertRaises(RuntimeError):
        d1.items() <= d2.items()
    with self.assertRaises(RuntimeError):
        d1.items() >= d2.items()
    d3 = {1: C(), 2: C()}
    with self.assertRaises(RuntimeError):
        d2.items() < d3.items()
    with self.assertRaises(RuntimeError):
        d3.items() > d2.items()
