# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: AuditingTests_test_audit_run_startup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    startup = os.path.join(self.oldcwd, os_helper.TESTFN) + '.py'
    with open(startup, 'w', encoding='utf-8') as f:
        print('pass', file=f)
    try:
        env = {**remove_python_envvars(), 'PYTHONSTARTUP': startup}
        self.run_embedded_interpreter('test_audit_run_startup', timeout=support.SHORT_TIMEOUT, returncode=10, env=env)
    finally:
        os.unlink(startup)
