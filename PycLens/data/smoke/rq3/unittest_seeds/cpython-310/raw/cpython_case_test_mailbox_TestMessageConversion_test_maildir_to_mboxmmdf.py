# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_maildir_to_mboxmmdf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pairs = (('D', ''), ('F', 'F'), ('P', ''), ('R', 'A'), ('S', 'R'), ('T', 'D'), ('DFPRST', 'RDFA'))
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        msg_maildir = mailbox.MaildirMessage(_sample_message)
        msg_maildir.set_date(0.0)
        for (setting, result) in pairs:
            msg_maildir.set_flags(setting)
            msg = class_(msg_maildir)
            self.assertEqual(msg.get_flags(), result)
            self.assertEqual(msg.get_from(), 'MAILER-DAEMON %s' % time.asctime(time.gmtime(0.0)))
        msg_maildir.set_subdir('cur')
        self.assertEqual(class_(msg_maildir).get_flags(), 'RODFA')
