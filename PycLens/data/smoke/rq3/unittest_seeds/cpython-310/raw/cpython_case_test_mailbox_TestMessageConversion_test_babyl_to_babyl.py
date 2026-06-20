# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_babyl_to_babyl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.BabylMessage(_sample_message)
    msg.update_visible()
    for label in ('unseen', 'deleted', 'filed', 'answered', 'forwarded', 'edited', 'resent'):
        msg.add_label(label)
    msg2 = mailbox.BabylMessage(msg)
    self.assertEqual(msg2.get_labels(), ['unseen', 'deleted', 'filed', 'answered', 'forwarded', 'edited', 'resent'])
    self.assertEqual(msg.get_visible().keys(), msg2.get_visible().keys())
    for key in msg.get_visible().keys():
        self.assertEqual(msg.get_visible()[key], msg2.get_visible()[key])
