# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_add_invalid_8bit_bytes_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key = self._box.add(self._nonascii_msg.encode('latin-1'))
    self.assertEqual(len(self._box), 1)
    self.assertEqual(self._box.get_bytes(key), self._nonascii_msg.encode('latin-1'))
