# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_mboxmmdf_to_maildir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        msg_mboxMMDF = class_(_sample_message)
        msg_mboxMMDF.set_from('foo@bar', time.gmtime(0.0))
        pairs = (('R', 'S'), ('O', ''), ('D', 'T'), ('F', 'F'), ('A', 'R'), ('RODFA', 'FRST'))
        for (setting, result) in pairs:
            msg_mboxMMDF.set_flags(setting)
            msg = mailbox.MaildirMessage(msg_mboxMMDF)
            self.assertEqual(msg.get_flags(), result)
            self.assertEqual(msg.get_date(), 0.0)
        msg_mboxMMDF.set_flags('O')
        self.assertEqual(mailbox.MaildirMessage(msg_mboxMMDF).get_subdir(), 'cur')
