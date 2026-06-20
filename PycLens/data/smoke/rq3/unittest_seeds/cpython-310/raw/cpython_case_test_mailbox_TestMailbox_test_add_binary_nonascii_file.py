# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_add_binary_nonascii_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryFile('wb+') as f:
        f.write(self._non_latin_bin_msg)
        f.seek(0)
        key = self._box.add(f)
    self.assertEqual(self._box.get_bytes(key).split(b'\n'), self._non_latin_bin_msg.split(b'\n'))
