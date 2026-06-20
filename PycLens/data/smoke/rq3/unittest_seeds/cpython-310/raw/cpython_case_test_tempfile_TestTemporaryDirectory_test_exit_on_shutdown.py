# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_exit_on_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.do_create() as dir:
        code = 'if True:\n                import sys\n                import tempfile\n                import warnings\n\n                def generator():\n                    with tempfile.TemporaryDirectory(dir={dir!r}) as tmp:\n                        yield tmp\n                g = generator()\n                sys.stdout.buffer.write(next(g).encode())\n\n                warnings.filterwarnings("always", category=ResourceWarning)\n                '.format(dir=dir)
        (rc, out, err) = script_helper.assert_python_ok('-c', code)
        tmp_name = out.decode().strip()
        self.assertFalse(os.path.exists(tmp_name), 'TemporaryDirectory %s exists after cleanup' % tmp_name)
        err = err.decode('utf-8', 'backslashreplace')
        self.assertNotIn('Exception ', err)
        self.assertIn('ResourceWarning: Implicitly cleaning up', err)
