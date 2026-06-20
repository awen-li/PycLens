# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_longexp.py
# case: LongExpText_test_longexp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    REPS = 65580
    l = eval('[' + '2,' * REPS + ']')
    self.assertEqual(len(l), REPS)
