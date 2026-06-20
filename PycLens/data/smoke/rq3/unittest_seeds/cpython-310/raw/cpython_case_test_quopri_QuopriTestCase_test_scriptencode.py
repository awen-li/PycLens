# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_quopri.py
# case: QuopriTestCase_test_scriptencode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (p, e) = self.STRINGS[-1]
    process = subprocess.Popen([sys.executable, '-mquopri'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    self.addCleanup(process.stdout.close)
    (cout, cerr) = process.communicate(p)
    cout = cout.decode('latin-1').splitlines()
    e = e.decode('latin-1').splitlines()
    assert len(cout) == len(e)
    for i in range(len(cout)):
        self.assertEqual(cout[i], e[i])
    self.assertEqual(cout, e)
