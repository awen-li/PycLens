# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_mh_to_mboxmmdf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pairs = (('unseen', 'O'), ('replied', 'ROA'), ('flagged', 'ROF'))
    for (setting, result) in pairs:
        msg = mailbox.MHMessage(_sample_message)
        msg.add_sequence(setting)
        for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
            self.assertEqual(class_(msg).get_flags(), result)
    msg = mailbox.MHMessage(_sample_message)
    msg.add_sequence('unseen')
    msg.add_sequence('replied')
    msg.add_sequence('flagged')
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        self.assertEqual(class_(msg).get_flags(), 'OFA')
