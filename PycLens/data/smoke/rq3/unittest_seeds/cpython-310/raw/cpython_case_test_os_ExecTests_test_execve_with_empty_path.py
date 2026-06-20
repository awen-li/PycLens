# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ExecTests_test_execve_with_empty_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.execve('', ['arg'], {})
    except OSError as e:
        self.assertTrue(e.winerror is None or e.winerror != 0)
    else:
        self.fail('No OSError raised')
