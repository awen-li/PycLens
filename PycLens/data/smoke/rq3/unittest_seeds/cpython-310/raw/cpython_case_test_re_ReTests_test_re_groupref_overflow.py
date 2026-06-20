# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_groupref_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from sre_constants import MAXGROUPS
    self.checkTemplateError('()', '\\g<%s>' % MAXGROUPS, 'xx', 'invalid group reference %d' % MAXGROUPS, 3)
    self.checkPatternError('(?P<a>)(?(%d))' % MAXGROUPS, 'invalid group reference %d' % MAXGROUPS, 10)
