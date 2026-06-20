# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_dict_evaluation_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = 0

    def f():
        nonlocal i
        i += 1
        return i
    d = {f(): f(), f(): f()}
    self.assertEqual(d, {1: 2, 3: 4})
