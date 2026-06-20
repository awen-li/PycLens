# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestMain_test_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    module = importlib.import_module('unittest')
    (_, out, err) = assert_python_failure('-m', 'inspect', 'sys')
    lines = err.decode().splitlines()
    self.assertEqual(lines, ["Can't get info for builtin modules."])
