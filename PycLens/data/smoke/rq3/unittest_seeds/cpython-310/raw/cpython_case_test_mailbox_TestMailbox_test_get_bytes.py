# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_get_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    key1 = self._box.add(_sample_message)
    self.assertEqual(self._box.get_bytes(key0), (self._template % 0).encode('ascii'))
    self.assertEqual(self._box.get_bytes(key1), _bytes_sample_message)
