# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    msg = self._box.get(key0)
    self.assertEqual(msg['from'], 'foo')
    self.assertEqual(msg.get_payload(), '0\n')
    self.assertIsNone(self._box.get('foo'))
    self.assertIs(self._box.get('foo', False), False)
    self._box.close()
    self._box = self._factory(self._path)
    key1 = self._box.add(self._template % 1)
    msg = self._box.get(key1)
    self.assertEqual(msg['from'], 'foo')
    self.assertEqual(msg.get_payload(), '1\n')
