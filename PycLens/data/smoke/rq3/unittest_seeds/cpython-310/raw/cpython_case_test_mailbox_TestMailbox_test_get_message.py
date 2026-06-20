# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_get_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    key1 = self._box.add(_sample_message)
    msg0 = self._box.get_message(key0)
    self.assertIsInstance(msg0, mailbox.Message)
    self.assertEqual(msg0['from'], 'foo')
    self.assertEqual(msg0.get_payload(), '0\n')
    self._check_sample(self._box.get_message(key1))
