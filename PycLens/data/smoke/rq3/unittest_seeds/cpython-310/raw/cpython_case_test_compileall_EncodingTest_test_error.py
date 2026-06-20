# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: EncodingTest_test_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        orig_stdout = sys.stdout
        sys.stdout = io.TextIOWrapper(io.BytesIO(), encoding='ascii')
        compileall.compile_dir(self.directory)
    finally:
        sys.stdout = orig_stdout
