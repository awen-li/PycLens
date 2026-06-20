# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirname = os.path.join(self.tmptestdir, 'test_python_123')
    os.mkdir(dirname)
    filename = os.path.join(self.tmptestdir, 'test_python_456')
    open(filename, 'wb').close()
    names = [dirname, filename]
    cmdargs = ['-m', 'test', '--tempdir=%s' % self.tmptestdir, '--cleanup']
    self.run_python(cmdargs)
    for name in names:
        self.assertFalse(os.path.exists(name), name)
