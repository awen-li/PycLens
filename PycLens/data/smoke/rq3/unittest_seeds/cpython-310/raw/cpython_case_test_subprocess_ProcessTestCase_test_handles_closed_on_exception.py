# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_handles_closed_on_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (ifhandle, ifname) = tempfile.mkstemp()
    (ofhandle, ofname) = tempfile.mkstemp()
    (efhandle, efname) = tempfile.mkstemp()
    try:
        subprocess.Popen(['*'], stdin=ifhandle, stdout=ofhandle, stderr=efhandle)
    except OSError:
        os.close(ifhandle)
        os.remove(ifname)
        os.close(ofhandle)
        os.remove(ofname)
        os.close(efhandle)
        os.remove(efname)
    self.assertFalse(os.path.exists(ifname))
    self.assertFalse(os.path.exists(ofname))
    self.assertFalse(os.path.exists(efname))
