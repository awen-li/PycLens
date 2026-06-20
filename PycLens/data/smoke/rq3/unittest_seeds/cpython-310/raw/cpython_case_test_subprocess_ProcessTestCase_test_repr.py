# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path_cmd = pathlib.Path('my-tool.py')
    pathlib_cls = path_cmd.__class__.__name__
    cases = [('ls', True, 123, "<Popen: returncode: 123 args: 'ls'>"), ('a' * 100, True, 0, "<Popen: returncode: 0 args: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...>"), (['ls'], False, None, "<Popen: returncode: None args: ['ls']>"), (['ls', '--my-opts', 'a' * 100], False, None, "<Popen: returncode: None args: ['ls', '--my-opts', 'aaaaaaaaaaaaaaaaaaaaaaaa...>"), (path_cmd, False, 7, f"<Popen: returncode: 7 args: {pathlib_cls}('my-tool.py')>")]
    with unittest.mock.patch.object(subprocess.Popen, '_execute_child'):
        for (cmd, shell, code, sx) in cases:
            p = subprocess.Popen(cmd, shell=shell)
            p.returncode = code
            self.assertEqual(repr(p), sx)
