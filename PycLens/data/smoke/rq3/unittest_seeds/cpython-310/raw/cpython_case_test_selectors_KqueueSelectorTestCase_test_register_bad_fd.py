# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: KqueueSelectorTestCase_test_register_bad_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    bad_f = os_helper.make_bad_fd()
    with self.assertRaises(OSError) as cm:
        s.register(bad_f, selectors.EVENT_READ)
    self.assertEqual(cm.exception.errno, errno.EBADF)
    with self.assertRaises(KeyError):
        s.get_key(bad_f)
