# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CreateTest_test_create

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tmpname, self.mode) as tobj:
        tobj.add(self.file_path)
    with self.taropen(tmpname) as tobj:
        names = tobj.getnames()
    self.assertEqual(len(names), 1)
    self.assertIn('spameggs42', names[0])
