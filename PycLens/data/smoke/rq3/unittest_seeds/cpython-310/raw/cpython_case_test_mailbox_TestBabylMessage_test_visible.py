# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestBabylMessage_test_visible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.BabylMessage(_sample_message)
    visible = msg.get_visible()
    self.assertEqual(visible.keys(), [])
    self.assertIsNone(visible.get_payload())
    visible['User-Agent'] = 'FooBar 1.0'
    visible['X-Whatever'] = 'Blah'
    self.assertEqual(msg.get_visible().keys(), [])
    msg.set_visible(visible)
    visible = msg.get_visible()
    self.assertEqual(visible.keys(), ['User-Agent', 'X-Whatever'])
    self.assertEqual(visible['User-Agent'], 'FooBar 1.0')
    self.assertEqual(visible['X-Whatever'], 'Blah')
    self.assertIsNone(visible.get_payload())
    msg.update_visible()
    self.assertEqual(visible.keys(), ['User-Agent', 'X-Whatever'])
    self.assertIsNone(visible.get_payload())
    visible = msg.get_visible()
    self.assertEqual(visible.keys(), ['User-Agent', 'Date', 'From', 'To', 'Subject'])
    for header in ('User-Agent', 'Date', 'From', 'To', 'Subject'):
        self.assertEqual(visible[header], msg[header])
