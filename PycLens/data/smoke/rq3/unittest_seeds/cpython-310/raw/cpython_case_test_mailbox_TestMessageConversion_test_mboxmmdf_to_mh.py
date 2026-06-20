# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_mboxmmdf_to_mh

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        msg_mboxMMDF = class_(_sample_message)
        pairs = (('R', []), ('O', ['unseen']), ('D', ['unseen']), ('F', ['unseen', 'flagged']), ('A', ['unseen', 'replied']), ('RODFA', ['replied', 'flagged']))
        for (setting, result) in pairs:
            msg_mboxMMDF.set_flags(setting)
            self.assertEqual(mailbox.MHMessage(msg_mboxMMDF).get_sequences(), result)
