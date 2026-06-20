# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_folder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def dummy_factory(s):
        return None
    box = self._factory(self._path, factory=dummy_factory)
    folder = box.add_folder('folder1')
    self.assertIs(folder._factory, dummy_factory)
    folder1_alias = box.get_folder('folder1')
    self.assertIs(folder1_alias._factory, dummy_factory)
