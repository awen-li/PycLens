# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ClosingTestCase_test_closing_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    state = []

    class C:

        def close(self):
            state.append(1)
    x = C()
    self.assertEqual(state, [])
    with self.assertRaises(ZeroDivisionError):
        with closing(x) as y:
            self.assertEqual(x, y)
            1 / 0
    self.assertEqual(state, [1])
