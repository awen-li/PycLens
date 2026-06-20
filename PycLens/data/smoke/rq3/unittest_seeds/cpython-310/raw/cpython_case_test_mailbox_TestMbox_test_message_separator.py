# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMbox_test_message_separator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._box.add('From: foo\n\n0')
    with open(self._path, encoding='utf-8') as f:
        data = f.read()
        self.assertEqual(data[-3:], '0\n\n')
    self._box.add('From: foo\n\n0\n')
    with open(self._path, encoding='utf-8') as f:
        data = f.read()
        self.assertEqual(data[-3:], '0\n\n')
