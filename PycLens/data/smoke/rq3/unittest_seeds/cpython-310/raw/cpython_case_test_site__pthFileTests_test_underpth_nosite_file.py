# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: _pthFileTests_test_underpth_nosite_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    libpath = os.path.dirname(os.path.dirname(encodings.__file__))
    exe_prefix = os.path.dirname(sys.executable)
    pth_lines = ['fake-path-name', *[libpath for _ in range(200)], '', '# comment']
    exe_file = self._create_underpth_exe(pth_lines)
    sys_path = self._calc_sys_path_for_underpth_nosite(os.path.dirname(exe_file), pth_lines)
    env = os.environ.copy()
    env['PYTHONPATH'] = 'from-env'
    env['PATH'] = '{};{}'.format(exe_prefix, os.getenv('PATH'))
    output = subprocess.check_output([exe_file, '-c', 'import sys; print("\\n".join(sys.path) if sys.flags.no_site else "")'], env=env, encoding='ansi')
    actual_sys_path = output.rstrip().split('\n')
    self.assertTrue(actual_sys_path, 'sys.flags.no_site was False')
    self.assertEqual(actual_sys_path, sys_path, 'sys.path is incorrect')
