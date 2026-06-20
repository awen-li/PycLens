# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_del_on_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.do_create() as dir:
        for mod in ('builtins', 'os', 'shutil', 'sys', 'tempfile', 'warnings'):
            code = 'if True:\n                    import builtins\n                    import os\n                    import shutil\n                    import sys\n                    import tempfile\n                    import warnings\n\n                    tmp = tempfile.TemporaryDirectory(dir={dir!r})\n                    sys.stdout.buffer.write(tmp.name.encode())\n\n                    tmp2 = os.path.join(tmp.name, \'test_dir\')\n                    os.mkdir(tmp2)\n                    with open(os.path.join(tmp2, "test0.txt"), "w") as f:\n                        f.write("Hello world!")\n\n                    {mod}.tmp = tmp\n\n                    warnings.filterwarnings("always", category=ResourceWarning)\n                    '.format(dir=dir, mod=mod)
            (rc, out, err) = script_helper.assert_python_ok('-c', code)
            tmp_name = out.decode().strip()
            self.assertFalse(os.path.exists(tmp_name), 'TemporaryDirectory %s exists after cleanup' % tmp_name)
            err = err.decode('utf-8', 'backslashreplace')
            self.assertNotIn('Exception ', err)
            self.assertIn('ResourceWarning: Implicitly cleaning up', err)
