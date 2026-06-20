# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_repl.py
# case: TestInteractiveInterpreter_test_close_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    user_input = dedent('\n            import os\n            print("before close")\n            os.close(0)\n        ')
    prepare_repl = dedent('\n            from test.support import suppress_msvcrt_asserts\n            suppress_msvcrt_asserts()\n        ')
    process = spawn_repl('-c', prepare_repl)
    output = process.communicate(user_input)[0]
    self.assertEqual(process.returncode, 0)
    self.assertIn('before close', output)
