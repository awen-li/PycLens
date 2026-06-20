# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_nothing_to_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for reps in ('*', '+', '?', '{1,2}'):
        for mod in ('', '?'):
            self.checkPatternError('%s%s' % (reps, mod), 'nothing to repeat', 0)
            self.checkPatternError('(?:%s%s)' % (reps, mod), 'nothing to repeat', 3)
