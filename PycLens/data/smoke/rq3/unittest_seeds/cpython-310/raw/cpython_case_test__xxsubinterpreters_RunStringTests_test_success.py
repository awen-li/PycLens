# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (script, file) = _captured_script('print("it worked!", end="")')
    with file:
        interpreters.run_string(self.id, script)
        out = file.read()
    self.assertEqual(out, 'it worked!')
