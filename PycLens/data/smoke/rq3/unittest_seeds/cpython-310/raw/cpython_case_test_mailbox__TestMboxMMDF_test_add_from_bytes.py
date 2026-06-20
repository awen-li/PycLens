# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDF_test_add_from_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key = self._box.add(b'From foo@bar blah\nFrom: foo\n\n0\n')
    self.assertEqual(self._box[key].get_from(), 'foo@bar blah')
    self.assertEqual(self._box[key].get_payload(), '0\n')
