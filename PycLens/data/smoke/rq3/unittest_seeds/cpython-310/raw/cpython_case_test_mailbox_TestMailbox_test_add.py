# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    keys = []
    keys.append(self._box.add(self._template % 0))
    self.assertEqual(len(self._box), 1)
    keys.append(self._box.add(mailbox.Message(_sample_message)))
    self.assertEqual(len(self._box), 2)
    keys.append(self._box.add(email.message_from_string(_sample_message)))
    self.assertEqual(len(self._box), 3)
    keys.append(self._box.add(io.BytesIO(_bytes_sample_message)))
    self.assertEqual(len(self._box), 4)
    keys.append(self._box.add(_sample_message))
    self.assertEqual(len(self._box), 5)
    keys.append(self._box.add(_bytes_sample_message))
    self.assertEqual(len(self._box), 6)
    with self.assertWarns(DeprecationWarning):
        keys.append(self._box.add(io.TextIOWrapper(io.BytesIO(_bytes_sample_message), encoding='utf-8')))
    self.assertEqual(len(self._box), 7)
    self.assertEqual(self._box.get_string(keys[0]), self._template % 0)
    for i in (1, 2, 3, 4, 5, 6):
        self._check_sample(self._box[keys[i]])
