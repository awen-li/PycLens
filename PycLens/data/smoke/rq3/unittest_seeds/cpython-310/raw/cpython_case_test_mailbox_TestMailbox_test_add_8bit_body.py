# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_add_8bit_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key = self._box.add(self._non_latin_bin_msg)
    self.assertEqual(self._box.get_bytes(key), self._non_latin_bin_msg)
    with self._box.get_file(key) as f:
        self.assertEqual(f.read(), self._non_latin_bin_msg.replace(b'\n', os.linesep.encode()))
    self.assertEqual(self._box[key].get_payload(), 'Да, они летят.\n')
