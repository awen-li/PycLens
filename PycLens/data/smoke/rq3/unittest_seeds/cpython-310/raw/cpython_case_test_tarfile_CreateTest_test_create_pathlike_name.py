# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CreateTest_test_create_pathlike_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(pathlib.Path(tmpname), self.mode) as tobj:
        self.assertIsInstance(tobj.name, str)
        self.assertEqual(tobj.name, os.path.abspath(tmpname))
        tobj.add(pathlib.Path(self.file_path))
        names = tobj.getnames()
    self.assertEqual(len(names), 1)
    self.assertIn('spameggs42', names[0])
    with self.taropen(tmpname) as tobj:
        names = tobj.getnames()
    self.assertEqual(len(names), 1)
    self.assertIn('spameggs42', names[0])
