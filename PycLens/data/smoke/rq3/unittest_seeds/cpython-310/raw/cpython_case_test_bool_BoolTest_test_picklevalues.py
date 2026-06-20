# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_picklevalues

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pickle
    self.assertEqual(pickle.dumps(True, protocol=0), b'I01\n.')
    self.assertEqual(pickle.dumps(False, protocol=0), b'I00\n.')
    self.assertEqual(pickle.dumps(True, protocol=1), b'I01\n.')
    self.assertEqual(pickle.dumps(False, protocol=1), b'I00\n.')
    self.assertEqual(pickle.dumps(True, protocol=2), b'\x80\x02\x88.')
    self.assertEqual(pickle.dumps(False, protocol=2), b'\x80\x02\x89.')
