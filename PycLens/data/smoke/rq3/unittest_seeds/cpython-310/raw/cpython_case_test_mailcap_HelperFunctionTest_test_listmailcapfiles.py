# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: HelperFunctionTest_test_listmailcapfiles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mcfiles = mailcap.listmailcapfiles()
    self.assertIsInstance(mcfiles, list)
    for m in mcfiles:
        self.assertIsInstance(m, str)
    with os_helper.EnvironmentVarGuard() as env:
        if 'MAILCAPS' in env:
            env_mailcaps = env['MAILCAPS'].split(os.pathsep)
        else:
            env_mailcaps = ['/testdir1/.mailcap', '/testdir2/mailcap']
            env['MAILCAPS'] = os.pathsep.join(env_mailcaps)
            mcfiles = mailcap.listmailcapfiles()
    self.assertEqual(env_mailcaps, mcfiles)
