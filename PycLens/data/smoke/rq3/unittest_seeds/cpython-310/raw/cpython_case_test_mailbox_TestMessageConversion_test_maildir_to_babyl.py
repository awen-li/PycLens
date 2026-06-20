# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_maildir_to_babyl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg_maildir = mailbox.MaildirMessage(_sample_message)
    pairs = (('D', ['unseen']), ('F', ['unseen']), ('P', ['unseen', 'forwarded']), ('R', ['unseen', 'answered']), ('S', []), ('T', ['unseen', 'deleted']), ('DFPRST', ['deleted', 'answered', 'forwarded']))
    for (setting, result) in pairs:
        msg_maildir.set_flags(setting)
        self.assertEqual(mailbox.BabylMessage(msg_maildir).get_labels(), result)
