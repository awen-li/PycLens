# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_mh_to_maildir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pairs = (('unseen', ''), ('replied', 'RS'), ('flagged', 'FS'))
    for (setting, result) in pairs:
        msg = mailbox.MHMessage(_sample_message)
        msg.add_sequence(setting)
        self.assertEqual(mailbox.MaildirMessage(msg).get_flags(), result)
        self.assertEqual(mailbox.MaildirMessage(msg).get_subdir(), 'cur')
    msg = mailbox.MHMessage(_sample_message)
    msg.add_sequence('unseen')
    msg.add_sequence('replied')
    msg.add_sequence('flagged')
    self.assertEqual(mailbox.MaildirMessage(msg).get_flags(), 'FR')
    self.assertEqual(mailbox.MaildirMessage(msg).get_subdir(), 'cur')
