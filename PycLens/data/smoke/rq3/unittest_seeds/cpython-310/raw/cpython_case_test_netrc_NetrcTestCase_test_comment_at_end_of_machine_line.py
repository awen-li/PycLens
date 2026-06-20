# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_netrc.py
# case: NetrcTestCase_test_comment_at_end_of_machine_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_comment('            machine foo.domain.com login bar password pass # comment\n            machine bar.domain.com login foo password pass\n            ')
