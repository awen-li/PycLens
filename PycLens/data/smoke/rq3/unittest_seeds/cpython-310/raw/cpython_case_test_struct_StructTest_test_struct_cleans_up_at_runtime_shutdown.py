# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_struct_cleans_up_at_runtime_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "if 1:\n            import struct\n\n            class C:\n                def __init__(self):\n                    self.pack = struct.pack\n                def __del__(self):\n                    self.pack('I', -42)\n\n            struct.x = C()\n            "
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    self.assertEqual(rc, 0)
    self.assertEqual(stdout.rstrip(), b'')
    self.assertIn(b'Exception ignored in:', stderr)
    self.assertIn(b'C.__del__', stderr)
