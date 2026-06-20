# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_bytes_name_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.requires_name_attribute()
    tarname = os.fsencode(self.tarname)
    with open(tarname, 'rb') as fobj:
        self.assertIsInstance(fobj.name, bytes)
        with tarfile.open(fileobj=fobj, mode=self.mode) as tar:
            self.assertIsInstance(tar.name, bytes)
            self.assertEqual(tar.name, os.path.abspath(fobj.name))
