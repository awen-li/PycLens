# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_lock_unlock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(os.path.exists(self._get_lock_path()))
    self._box.lock()
    self.assertTrue(os.path.exists(self._get_lock_path()))
    self._box.unlock()
    self.assertFalse(os.path.exists(self._get_lock_path()))
