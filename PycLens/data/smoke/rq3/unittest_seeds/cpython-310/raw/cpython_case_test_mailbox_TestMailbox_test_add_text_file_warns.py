# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_add_text_file_warns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryFile('w+', encoding='utf-8') as f:
        f.write(_sample_message)
        f.seek(0)
        with self.assertWarns(DeprecationWarning):
            key = self._box.add(f)
    self.assertEqual(self._box.get_bytes(key).split(b'\n'), _bytes_sample_message.split(b'\n'))
