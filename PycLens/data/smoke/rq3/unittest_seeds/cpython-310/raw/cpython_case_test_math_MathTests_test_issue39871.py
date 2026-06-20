# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_issue39871

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class F:

        def __float__(self):
            self.converted = True
            1 / 0
    for func in (math.atan2, math.copysign, math.remainder):
        y = F()
        with self.assertRaises(TypeError):
            func('not a number', y)
        self.assertFalse(getattr(y, 'converted', False))
