# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_print_traceback_at_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            import traceback\n\n            class PrintExceptionAtExit(object):\n                def __init__(self):\n                    try:\n                        x = 1 / 0\n                    except Exception:\n                        self.exc_info = sys.exc_info()\n                        # self.exc_info[1] (traceback) contains frames:\n                        # explicitly clear the reference to self in the current\n                        # frame to break a reference cycle\n                        self = None\n\n                def __del__(self):\n                    traceback.print_exception(*self.exc_info)\n\n            # Keep a reference in the module namespace to call the destructor\n            # when the module is unloaded\n            obj = PrintExceptionAtExit()\n        ')
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    expected = [b'Traceback (most recent call last):', b'  File "<string>", line 8, in __init__', b'ZeroDivisionError: division by zero']
    self.assertEqual(stderr.splitlines(), expected)
