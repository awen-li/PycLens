# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_side_effect_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __init__(self):
            self.i = 0

        def __format__(self, spec):
            self.i += 1
            return str(self.i)
    x = X()
    self.assertEqual(f'{x} {x}', '1 2')
