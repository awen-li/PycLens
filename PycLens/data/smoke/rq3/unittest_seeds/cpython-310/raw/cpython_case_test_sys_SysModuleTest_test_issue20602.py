# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_issue20602

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import sys\n            class A:\n                def __del__(self, sys=sys):\n                    print(sys.flags)\n                    print(sys.float_info)\n            a = A()\n            '
    (rc, out, err) = assert_python_ok('-c', code)
    out = out.splitlines()
    self.assertIn(b'sys.flags', out[0])
    self.assertIn(b'sys.float_info', out[1])
