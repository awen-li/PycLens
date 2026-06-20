# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EventfdTests_test_eventfd_initval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def pack(value):
        """Pack as native uint64_t
            """
        return struct.pack('@Q', value)
    size = 8
    initval = 42
    fd = os.eventfd(initval)
    self.assertNotEqual(fd, -1)
    self.addCleanup(os.close, fd)
    self.assertFalse(os.get_inheritable(fd))
    res = os.read(fd, size)
    self.assertEqual(res, pack(initval))
    os.write(fd, pack(23))
    res = os.read(fd, size)
    self.assertEqual(res, pack(23))
    os.write(fd, pack(40))
    os.write(fd, pack(2))
    res = os.read(fd, size)
    self.assertEqual(res, pack(42))
    os.eventfd_write(fd, 20)
    os.eventfd_write(fd, 3)
    res = os.eventfd_read(fd)
    self.assertEqual(res, 23)
