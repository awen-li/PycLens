# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rmtree(self.env_dir)
    self.run_with_capture(venv.create, self.env_dir)
    self.isdir(self.bindir)
    self.isdir(self.include)
    self.isdir(*self.lib)
    p = self.get_env_file('lib64')
    conditions = struct.calcsize('P') == 8 and os.name == 'posix' and (sys.platform != 'darwin')
    if conditions:
        self.assertTrue(os.path.islink(p))
    else:
        self.assertFalse(os.path.exists(p))
    data = self.get_text_file_contents('pyvenv.cfg')
    executable = sys._base_executable
    path = os.path.dirname(executable)
    self.assertIn('home = %s' % path, data)
    fn = self.get_env_file(self.bindir, self.exe)
    if not os.path.exists(fn):
        bd = self.get_env_file(self.bindir)
        print('Contents of %r:' % bd)
        print('    %r' % os.listdir(bd))
    self.assertTrue(os.path.exists(fn), 'File %r should exist.' % fn)
