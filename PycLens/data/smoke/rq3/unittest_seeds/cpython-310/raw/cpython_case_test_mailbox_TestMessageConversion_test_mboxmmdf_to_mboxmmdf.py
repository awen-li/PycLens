# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_mboxmmdf_to_mboxmmdf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        msg_mboxMMDF = class_(_sample_message)
        msg_mboxMMDF.set_flags('RODFA')
        msg_mboxMMDF.set_from('foo@bar')
        for class2_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
            msg2 = class2_(msg_mboxMMDF)
            self.assertEqual(msg2.get_flags(), 'RODFA')
            self.assertEqual(msg2.get_from(), 'foo@bar')
