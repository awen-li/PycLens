# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_rmtree

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirpath = os_helper.TESTFN + 'd'
    subdirpath = os.path.join(dirpath, 'subdir')
    os.mkdir(dirpath)
    os.mkdir(subdirpath)
    os_helper.rmtree(dirpath)
    self.assertFalse(os.path.exists(dirpath))
    with support.swap_attr(support, 'verbose', 0):
        os_helper.rmtree(dirpath)
    os.mkdir(dirpath)
    os.mkdir(subdirpath)
    os.chmod(dirpath, stat.S_IRUSR | stat.S_IXUSR)
    with support.swap_attr(support, 'verbose', 0):
        os_helper.rmtree(dirpath)
    self.assertFalse(os.path.exists(dirpath))
    os.mkdir(dirpath)
    os.mkdir(subdirpath)
    os.chmod(dirpath, 0)
    with support.swap_attr(support, 'verbose', 0):
        os_helper.rmtree(dirpath)
    self.assertFalse(os.path.exists(dirpath))
