# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue7964

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'print("testing my pdb")\r\n')
    cmd = [sys.executable, '-m', 'pdb', os_helper.TESTFN]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    self.addCleanup(proc.stdout.close)
    (stdout, stderr) = proc.communicate(b'quit\n')
    self.assertNotIn(b'SyntaxError', stdout, 'Got a syntax error running test script under PDB')
