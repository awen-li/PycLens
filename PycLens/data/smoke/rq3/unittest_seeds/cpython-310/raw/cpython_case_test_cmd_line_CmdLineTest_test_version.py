# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    version = ('Python %d.%d' % sys.version_info[:2]).encode('ascii')
    for switch in ('-V', '--version', '-VV'):
        (rc, out, err) = assert_python_ok(switch)
        self.assertFalse(err.startswith(version))
        self.assertTrue(out.startswith(version))
