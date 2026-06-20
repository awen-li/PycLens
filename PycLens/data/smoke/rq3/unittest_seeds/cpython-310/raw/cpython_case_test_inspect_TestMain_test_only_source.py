# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestMain_test_only_source

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    module = importlib.import_module('unittest')
    (rc, out, err) = assert_python_ok('-m', 'inspect', 'unittest')
    lines = out.decode().splitlines()
    self.assertEqual(lines[:-1], inspect.getsource(module).splitlines())
    self.assertEqual(err, b'')
