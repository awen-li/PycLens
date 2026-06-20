# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_absolute_cmd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rv = shutil.which(self.temp_file.name, path=self.temp_dir)
    self.assertEqual(rv, self.temp_file.name)
