# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_mboxmmdf_to_babyl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        msg = class_(_sample_message)
        pairs = (('R', []), ('O', ['unseen']), ('D', ['unseen', 'deleted']), ('F', ['unseen']), ('A', ['unseen', 'answered']), ('RODFA', ['deleted', 'answered']))
        for (setting, result) in pairs:
            msg.set_flags(setting)
            self.assertEqual(mailbox.BabylMessage(msg).get_labels(), result)
