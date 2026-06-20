# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_int_name_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(self.tarname, os.O_RDONLY)
    with open(fd, 'rb') as fobj:
        self.assertIsInstance(fobj.name, int)
        with tarfile.open(fileobj=fobj, mode=self.mode) as tar:
            self.assertIsNone(tar.name)
