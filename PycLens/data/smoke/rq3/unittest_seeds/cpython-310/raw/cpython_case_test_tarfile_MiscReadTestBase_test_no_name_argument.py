# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_no_name_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.requires_name_attribute()
    with open(self.tarname, 'rb') as fobj:
        self.assertIsInstance(fobj.name, str)
        with tarfile.open(fileobj=fobj, mode=self.mode) as tar:
            self.assertIsInstance(tar.name, str)
            self.assertEqual(tar.name, os.path.abspath(fobj.name))
