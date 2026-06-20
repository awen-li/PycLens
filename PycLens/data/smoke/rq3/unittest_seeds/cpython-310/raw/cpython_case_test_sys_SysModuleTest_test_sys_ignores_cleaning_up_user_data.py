# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_sys_ignores_cleaning_up_user_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "if 1:\n            import struct, sys\n\n            class C:\n                def __init__(self):\n                    self.pack = struct.pack\n                def __del__(self):\n                    self.pack('I', -42)\n\n            sys.x = C()\n            "
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    self.assertEqual(rc, 0)
    self.assertEqual(stdout.rstrip(), b'')
    self.assertEqual(stderr.rstrip(), b'')
