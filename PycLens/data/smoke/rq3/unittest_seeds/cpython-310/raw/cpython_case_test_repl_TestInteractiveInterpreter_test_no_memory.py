# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_repl.py
# case: TestInteractiveInterpreter_test_no_memory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    user_input = "\n            import sys, _testcapi\n            1/0\n            print('After the exception.')\n            _testcapi.set_nomemory(0)\n            sys.exit(0)\n        "
    user_input = dedent(user_input)
    p = spawn_repl()
    with SuppressCrashReport():
        p.stdin.write(user_input)
    output = kill_python(p)
    self.assertIn('After the exception.', output)
    self.assertIn(p.returncode, (1, 120))
