# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_pathext_with_empty_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ext = '.xyz'
    temp_filexyz = tempfile.NamedTemporaryFile(dir=self.temp_dir, prefix='Tmp2', suffix=ext)
    self.addCleanup(temp_filexyz.close)
    program = os.path.basename(temp_filexyz.name)
    program = os.path.splitext(program)[0]
    with os_helper.EnvironmentVarGuard() as env:
        env['PATHEXT'] = f'{ext};'
        rv = shutil.which(program, path=self.temp_dir)
        self.assertEqual(rv, temp_filexyz.name)
