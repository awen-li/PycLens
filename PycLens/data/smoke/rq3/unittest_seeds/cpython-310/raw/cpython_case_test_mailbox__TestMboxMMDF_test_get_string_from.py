# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDF_test_get_string_from

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unixfrom = 'From foo@bar blah\n'
    key0 = self._box.add(unixfrom + self._template % 0)
    key1 = self._box.add(unixfrom + _sample_message)
    self.assertEqual(self._box.get_string(key0, from_=False), self._template % 0)
    self.assertEqual(self._box.get_string(key1, from_=False).split('\n'), _sample_message.split('\n'))
    self.assertEqual(self._box.get_string(key0, from_=True), unixfrom + self._template % 0)
    self.assertEqual(self._box.get_string(key1, from_=True).split('\n'), (unixfrom + _sample_message).split('\n'))
