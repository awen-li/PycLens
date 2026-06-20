# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDF_test_relock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'Subject: sub\n\nbody\n'
    key1 = self._box.add(msg)
    self._box.flush()
    self._box.close()
    self._box = self._factory(self._path)
    self._box.lock()
    key2 = self._box.add(msg)
    self._box.flush()
    self.assertTrue(self._box._locked)
    self._box.close()
