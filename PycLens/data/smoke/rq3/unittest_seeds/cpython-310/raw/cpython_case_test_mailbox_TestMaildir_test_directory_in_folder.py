# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_directory_in_folder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(10):
        self._box.add(mailbox.Message(_sample_message))
    os.mkdir(os.path.join(self._path, 'cur', 'stray-dir'))
    for msg in self._box:
        pass
