# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_babyl_to_mboxmmdf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pairs = (('unseen', 'O'), ('deleted', 'ROD'), ('filed', 'RO'), ('answered', 'ROA'), ('forwarded', 'RO'), ('edited', 'RO'), ('resent', 'RO'))
    for (setting, result) in pairs:
        for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
            msg = mailbox.BabylMessage(_sample_message)
            msg.add_label(setting)
            self.assertEqual(class_(msg).get_flags(), result)
    msg = mailbox.BabylMessage(_sample_message)
    for label in ('unseen', 'deleted', 'filed', 'answered', 'forwarded', 'edited', 'resent'):
        msg.add_label(label)
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        self.assertEqual(class_(msg).get_flags(), 'ODA')
