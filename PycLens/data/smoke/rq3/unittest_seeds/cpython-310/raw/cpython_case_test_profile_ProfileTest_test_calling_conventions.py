# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_profile.py
# case: ProfileTest_test_calling_conventions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stmts = ['max([0])', 'max([0], key=int)', 'max([0], **dict(key=int))', 'max(*([0],))', 'max(*([0],), key=int)', 'max(*([0],), **dict(key=int))']
    for stmt in stmts:
        s = StringIO()
        prof = self.profilerclass(timer, 0.001)
        prof.runctx(stmt, globals(), locals())
        stats = pstats.Stats(prof, stream=s)
        stats.print_stats()
        res = s.getvalue()
        self.assertIn(self.expected_max_output, res, "Profiling {0!r} didn't report max:\n{1}".format(stmt, res))
