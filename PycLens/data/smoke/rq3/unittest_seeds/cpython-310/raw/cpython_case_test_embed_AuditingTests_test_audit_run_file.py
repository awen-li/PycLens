# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: AuditingTests_test_audit_run_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.run_embedded_interpreter('test_audit_run_file', timeout=support.SHORT_TIMEOUT, returncode=1)
