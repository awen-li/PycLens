# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_set_item

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 'original 0')
    self.assertEqual(self._box.get_string(key0), self._template % 'original 0')
    key1 = self._box.add(self._template % 'original 1')
    self.assertEqual(self._box.get_string(key1), self._template % 'original 1')
    self._box[key0] = self._template % 'changed 0'
    self.assertEqual(self._box.get_string(key0), self._template % 'changed 0')
    self._box[key1] = self._template % 'changed 1'
    self.assertEqual(self._box.get_string(key1), self._template % 'changed 1')
    self._box[key0] = _sample_message
    self._check_sample(self._box[key0])
    self._box[key1] = self._box[key0]
    self._check_sample(self._box[key1])
    self._box[key0] = self._template % 'original 0'
    self.assertEqual(self._box.get_string(key0), self._template % 'original 0')
    self._check_sample(self._box[key1])
    self.assertRaises(KeyError, lambda : self._box.__setitem__('foo', 'bar'))
    self.assertRaises(KeyError, lambda : self._box['foo'])
    self.assertEqual(len(self._box), 2)
