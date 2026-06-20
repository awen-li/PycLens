# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.change_cwd(TEMPDIR):
        tar = tarfile.open(tmpname, self.mode)
        try:
            tar.add('.')
        finally:
            tar.close()
        tar = tarfile.open(tmpname, 'r')
        try:
            for t in tar:
                if t.name != '.':
                    self.assertTrue(t.name.startswith('./'), t.name)
        finally:
            tar.close()
