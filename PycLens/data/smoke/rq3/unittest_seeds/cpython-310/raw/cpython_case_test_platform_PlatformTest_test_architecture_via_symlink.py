# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_architecture_via_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.PythonSymlink() as py:
        cmd = ('-c', 'import platform; print(platform.architecture())')
        self.assertEqual(py.call_real(*cmd), py.call_link(*cmd))
