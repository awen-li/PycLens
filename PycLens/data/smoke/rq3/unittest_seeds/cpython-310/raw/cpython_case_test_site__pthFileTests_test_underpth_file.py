# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: _pthFileTests_test_underpth_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    libpath = os.path.dirname(os.path.dirname(encodings.__file__))
    exe_prefix = os.path.dirname(sys.executable)
    exe_file = self._create_underpth_exe(['fake-path-name', *[libpath for _ in range(200)], '', '# comment', 'import site'])
    sys_prefix = os.path.dirname(exe_file)
    env = os.environ.copy()
    env['PYTHONPATH'] = 'from-env'
    env['PATH'] = '{};{}'.format(exe_prefix, os.getenv('PATH'))
    rc = subprocess.call([exe_file, '-c', 'import sys; sys.exit(not sys.flags.no_site and %r in sys.path and %r in sys.path and %r not in sys.path and all("\\r" not in p and "\\n" not in p for p in sys.path))' % (os.path.join(sys_prefix, 'fake-path-name'), libpath, os.path.join(sys_prefix, 'from-env'))], env=env)
    self.assertTrue(rc, 'sys.path is incorrect')
