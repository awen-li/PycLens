# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestPartialFile_test_initialize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._file.write(bytes('foo' + os.linesep + 'bar', 'ascii'))
    pos = self._file.tell()
    proxy = mailbox._PartialFile(self._file, 2, 5)
    self.assertEqual(proxy.tell(), 0)
    self.assertEqual(self._file.tell(), pos)
