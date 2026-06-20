# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_get_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key0 = self._box.add(self._template % 0)
    key1 = self._box.add(_sample_message)
    with self._box.get_file(key0) as file:
        data0 = file.read()
    with self._box.get_file(key1) as file:
        data1 = file.read()
    self.assertEqual(data0.decode('ascii').replace(os.linesep, '\n'), self._template % 0)
    self.assertEqual(data1.decode('ascii').replace(os.linesep, '\n'), _sample_message)
