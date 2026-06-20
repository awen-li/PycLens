# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestBabyl_test_labels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self._box.get_labels(), [])
    msg0 = mailbox.BabylMessage(self._template % 0)
    msg0.add_label('foo')
    key0 = self._box.add(msg0)
    self.assertEqual(self._box.get_labels(), ['foo'])
    msg1 = mailbox.BabylMessage(self._template % 1)
    msg1.set_labels(['bar', 'answered', 'foo'])
    key1 = self._box.add(msg1)
    self.assertEqual(set(self._box.get_labels()), set(['foo', 'bar']))
    msg0.set_labels(['blah', 'filed'])
    self._box[key0] = msg0
    self.assertEqual(set(self._box.get_labels()), set(['foo', 'bar', 'blah']))
    self._box.remove(key1)
    self.assertEqual(set(self._box.get_labels()), set(['blah']))
