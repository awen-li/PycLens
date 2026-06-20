# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_consistent_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(self._template % 0)
    msg.set_subdir('cur')
    msg.set_flags('RF')
    key = self._box.add(msg)

    class FakeMessage(mailbox.MaildirMessage):
        pass
    box = mailbox.Maildir(self._path, factory=FakeMessage)
    box.colon = self._box.colon
    msg2 = box.get_message(key)
    self.assertIsInstance(msg2, FakeMessage)
