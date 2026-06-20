# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetsourceInteractive_test_getclasses_interactive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "import sys, inspect;                 assert not hasattr(sys.modules['__main__'], '__file__');                 A = type('A', (), {});                 inspect.getsource(A)"
    (_, _, stderr) = assert_python_failure('-c', code, __isolated=True)
    self.assertIn(b'OSError: source code not available', stderr)
