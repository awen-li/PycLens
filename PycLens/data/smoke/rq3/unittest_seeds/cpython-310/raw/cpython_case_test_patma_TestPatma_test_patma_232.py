# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_232

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Eq:

        def __eq__(self, other):
            return True
    x = eq = Eq()
    y = None
    match x:
        case None:
            y = 0
    self.assertIs(x, eq)
    self.assertEqual(y, None)
