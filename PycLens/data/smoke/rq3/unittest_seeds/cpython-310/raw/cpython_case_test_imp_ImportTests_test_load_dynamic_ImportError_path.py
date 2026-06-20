# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_load_dynamic_ImportError_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = 'bogus file path'
    name = 'extension'
    with self.assertRaises(ImportError) as err:
        imp.load_dynamic(name, path)
    self.assertIn(path, err.exception.path)
    self.assertEqual(name, err.exception.name)
