# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_set_MM

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg0 = mailbox.MaildirMessage(self._template % 0)
    msg0.set_flags('TP')
    key = self._box.add(msg0)
    msg_returned = self._box.get_message(key)
    self.assertEqual(msg_returned.get_subdir(), 'new')
    self.assertEqual(msg_returned.get_flags(), 'PT')
    msg1 = mailbox.MaildirMessage(self._template % 1)
    self._box[key] = msg1
    msg_returned = self._box.get_message(key)
    self.assertEqual(msg_returned.get_subdir(), 'new')
    self.assertEqual(msg_returned.get_flags(), '')
    self.assertEqual(msg_returned.get_payload(), '1\n')
    msg2 = mailbox.MaildirMessage(self._template % 2)
    msg2.set_info('2,S')
    self._box[key] = msg2
    self._box[key] = self._template % 3
    msg_returned = self._box.get_message(key)
    self.assertEqual(msg_returned.get_subdir(), 'new')
    self.assertEqual(msg_returned.get_flags(), 'S')
    self.assertEqual(msg_returned.get_payload(), '3\n')
