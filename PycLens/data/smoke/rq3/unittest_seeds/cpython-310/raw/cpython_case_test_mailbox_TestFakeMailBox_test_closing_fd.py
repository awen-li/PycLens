# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestFakeMailBox_test_closing_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    box = FakeMailBox()
    for i in range(10):
        self.assertFalse(box.files[i].closed)
    for i in range(10):
        box[i]
    for i in range(10):
        self.assertTrue(box.files[i].closed)
