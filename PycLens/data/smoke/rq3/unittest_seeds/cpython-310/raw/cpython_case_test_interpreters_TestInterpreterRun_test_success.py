# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterRun_test_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp = interpreters.create()
    (script, file) = _captured_script('print("it worked!", end="")')
    with file:
        interp.run(script)
        out = file.read()
    self.assertEqual(out, 'it worked!')
