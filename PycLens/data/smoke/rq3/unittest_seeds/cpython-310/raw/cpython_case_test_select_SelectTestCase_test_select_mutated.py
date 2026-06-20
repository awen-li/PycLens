# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_select.py
# case: SelectTestCase_test_select_mutated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = []

    class F:

        def fileno(self):
            del a[-1]
            return sys.__stdout__.fileno()
    a[:] = [F()] * 10
    self.assertEqual(select.select([], a, []), ([], a[:5], []))
