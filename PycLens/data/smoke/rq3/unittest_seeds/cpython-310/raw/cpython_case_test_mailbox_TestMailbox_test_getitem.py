# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    msg = self._box[key0]
    self.assertEqual(msg['from'], 'foo')
    self.assertEqual(msg.get_payload(), '0\n')
    self.assertRaises(KeyError, lambda : self._box['foo'])
    self._box.discard(key0)
    self.assertRaises(KeyError, lambda : self._box[key0])
