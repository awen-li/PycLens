# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with PythonSymlink() as py:
        cmd = ('-c', 'import sysconfig; print(sysconfig.get_platform())')
        self.assertEqual(py.call_real(*cmd), py.call_link(*cmd))
