# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestBabylMessage_test_labels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.BabylMessage(_sample_message)
    self.assertEqual(msg.get_labels(), [])
    msg.set_labels(['foobar'])
    self.assertEqual(msg.get_labels(), ['foobar'])
    msg.set_labels([])
    self.assertEqual(msg.get_labels(), [])
    msg.add_label('filed')
    self.assertEqual(msg.get_labels(), ['filed'])
    msg.add_label('resent')
    self.assertEqual(msg.get_labels(), ['filed', 'resent'])
    msg.add_label('resent')
    self.assertEqual(msg.get_labels(), ['filed', 'resent'])
    msg.remove_label('filed')
    self.assertEqual(msg.get_labels(), ['resent'])
    msg.add_label('foobar')
    self.assertEqual(msg.get_labels(), ['resent', 'foobar'])
    msg.remove_label('unseen')
    self.assertEqual(msg.get_labels(), ['resent', 'foobar'])
    msg.set_labels(['foobar', 'answered'])
    self.assertEqual(msg.get_labels(), ['foobar', 'answered'])
