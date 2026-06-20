# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_access_denied

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = os.path.join(os.environ['TEMP'], self.fname)
    self.addCleanup(os_helper.unlink, fname)
    create_file(fname, b'ABC')
    DETACHED_PROCESS = 8
    subprocess.check_call(['icacls.exe', fname, '/deny', '*S-1-5-32-545:(S)'], creationflags=DETACHED_PROCESS)
    result = os.stat(fname)
    self.assertNotEqual(result.st_size, 0)
