# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestPartialFile_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._file.write(bytes('&foo%sbar%s^' % (os.linesep, os.linesep), 'ascii'))
    self._test_close(mailbox._PartialFile(self._file, 1, 6 + 3 * len(os.linesep)))
