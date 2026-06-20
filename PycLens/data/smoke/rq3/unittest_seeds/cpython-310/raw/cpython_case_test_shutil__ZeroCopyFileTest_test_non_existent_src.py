# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: _ZeroCopyFileTest_test_non_existent_src

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = tempfile.mktemp(dir=os.getcwd())
    with self.assertRaises(FileNotFoundError) as cm:
        shutil.copyfile(name, 'new')
    self.assertEqual(cm.exception.filename, name)
