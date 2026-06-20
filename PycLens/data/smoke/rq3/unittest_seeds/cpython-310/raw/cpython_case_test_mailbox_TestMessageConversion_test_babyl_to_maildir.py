# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_babyl_to_maildir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pairs = (('unseen', ''), ('deleted', 'ST'), ('filed', 'S'), ('answered', 'RS'), ('forwarded', 'PS'), ('edited', 'S'), ('resent', 'PS'))
    for (setting, result) in pairs:
        msg = mailbox.BabylMessage(_sample_message)
        msg.add_label(setting)
        self.assertEqual(mailbox.MaildirMessage(msg).get_flags(), result)
        self.assertEqual(mailbox.MaildirMessage(msg).get_subdir(), 'cur')
    msg = mailbox.BabylMessage(_sample_message)
    for label in ('unseen', 'deleted', 'filed', 'answered', 'forwarded', 'edited', 'resent'):
        msg.add_label(label)
    self.assertEqual(mailbox.MaildirMessage(msg).get_flags(), 'PRT')
    self.assertEqual(mailbox.MaildirMessage(msg).get_subdir(), 'cur')
