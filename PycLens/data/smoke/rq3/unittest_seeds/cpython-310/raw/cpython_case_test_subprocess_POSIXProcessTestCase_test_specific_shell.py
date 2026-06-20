# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_specific_shell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    shells = []
    for prefix in ['/bin', '/usr/bin/', '/usr/local/bin']:
        for name in ['bash', 'ksh']:
            sh = os.path.join(prefix, name)
            if os.path.isfile(sh):
                shells.append(sh)
    if not shells:
        self.skipTest('bash or ksh required for this test')
    sh = '/bin/sh'
    if os.path.isfile(sh) and (not os.path.islink(sh)):
        shells.append(sh)
    for sh in shells:
        p = subprocess.Popen('echo $0', executable=sh, shell=True, stdout=subprocess.PIPE)
        with p:
            self.assertEqual(p.stdout.read().strip(), bytes(sh, 'ascii'))
