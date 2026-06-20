# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestMain_test_qualname_source

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-m', 'inspect', 'concurrent.futures:ThreadPoolExecutor')
    lines = out.decode().splitlines()
    self.assertEqual(lines[:-1], inspect.getsource(ThreadPoolExecutor).splitlines())
    self.assertEqual(err, b'')
