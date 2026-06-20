# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_multiple_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for outer_reps in ('*', '+', '{1,2}'):
        for outer_mod in ('', '?'):
            outer_op = outer_reps + outer_mod
            for inner_reps in ('*', '+', '?', '{1,2}'):
                for inner_mod in ('', '?'):
                    inner_op = inner_reps + inner_mod
                    self.checkPatternError('x%s%s' % (inner_op, outer_op), 'multiple repeat', 1 + len(inner_op))
