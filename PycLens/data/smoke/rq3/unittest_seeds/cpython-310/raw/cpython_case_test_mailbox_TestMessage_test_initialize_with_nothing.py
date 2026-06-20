# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessage_test_initialize_with_nothing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = self._factory()
    self._post_initialize_hook(msg)
    self.assertIsInstance(msg, email.message.Message)
    self.assertIsInstance(msg, mailbox.Message)
    self.assertIsInstance(msg, self._factory)
    self.assertEqual(msg.keys(), [])
    self.assertFalse(msg.is_multipart())
    self.assertIsNone(msg.get_payload())
