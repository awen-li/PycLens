# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_quopri.py
# case: QuopriTestCase_test_scriptdecode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (p, e) = self.STRINGS[-1]
    process = subprocess.Popen([sys.executable, '-mquopri', '-d'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    self.addCleanup(process.stdout.close)
    (cout, cerr) = process.communicate(e)
    cout = cout.decode('latin-1')
    p = p.decode('latin-1')
    self.assertEqual(cout.splitlines(), p.splitlines())
