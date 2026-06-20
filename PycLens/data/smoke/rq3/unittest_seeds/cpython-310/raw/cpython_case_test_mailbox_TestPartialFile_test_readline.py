# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestPartialFile_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._file.write(bytes('!!!!!foo%sbar%sfred%sbob!!!!!' % (os.linesep, os.linesep, os.linesep), 'ascii'))
    self._test_readline(mailbox._PartialFile(self._file, 5, 18 + 3 * len(os.linesep)))
