# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_is_finalizing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(sys.is_finalizing(), False)
    code = 'if 1:\n            import sys\n\n            class AtExit:\n                is_finalizing = sys.is_finalizing\n                print = print\n\n                def __del__(self):\n                    self.print(self.is_finalizing(), flush=True)\n\n            # Keep a reference in the __main__ module namespace, so the\n            # AtExit destructor will be called at Python exit\n            ref = AtExit()\n        '
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    self.assertEqual(stdout.rstrip(), b'True')
