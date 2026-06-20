# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_babyl_to_mh

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pairs = (('unseen', ['unseen']), ('deleted', []), ('filed', []), ('answered', ['replied']), ('forwarded', []), ('edited', []), ('resent', []))
    for (setting, result) in pairs:
        msg = mailbox.BabylMessage(_sample_message)
        msg.add_label(setting)
        self.assertEqual(mailbox.MHMessage(msg).get_sequences(), result)
    msg = mailbox.BabylMessage(_sample_message)
    for label in ('unseen', 'deleted', 'filed', 'answered', 'forwarded', 'edited', 'resent'):
        msg.add_label(label)
    self.assertEqual(mailbox.MHMessage(msg).get_sequences(), ['unseen', 'replied'])
