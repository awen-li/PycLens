# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: EnsurePipTest_test_devnull

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os.devnull, 'rb') as f:
        self.assertEqual(f.read(), b'')
    self.assertTrue(os.path.exists(os.devnull))
