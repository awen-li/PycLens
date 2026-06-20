# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_get_MM

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(self._template % 0)
    msg.set_subdir('cur')
    msg.set_flags('RF')
    key = self._box.add(msg)
    msg_returned = self._box.get_message(key)
    self.assertIsInstance(msg_returned, mailbox.MaildirMessage)
    self.assertEqual(msg_returned.get_subdir(), 'cur')
    self.assertEqual(msg_returned.get_flags(), 'FR')
