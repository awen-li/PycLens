# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_add_nonascii_StringIO_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertWarns(DeprecationWarning):
        with self.assertRaisesRegex(ValueError, 'ASCII-only'):
            self._box.add(io.StringIO(self._nonascii_msg))
    self.assertEqual(len(self._box), 0)
    self._box.close()
    self.assertMailboxEmpty()
