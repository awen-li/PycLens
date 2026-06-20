# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: ShutdownTest_test_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import builtins\n            import sys\n\n            class C:\n                def __del__(self):\n                    print("before")\n                    # Check that builtins still exist\n                    len(())\n                    print("after")\n\n            c = C()\n            # Make this module survive until builtins and sys are cleaned\n            builtins.here = sys.modules[__name__]\n            sys.here = sys.modules[__name__]\n            # Create a reference loop so that this module needs to go\n            # through a GC phase.\n            here = sys.modules[__name__]\n            '
    (rc, out, err) = assert_python_ok('-c', code, PYTHONIOENCODING='ascii')
    self.assertEqual(['before', 'after'], out.decode().splitlines())
