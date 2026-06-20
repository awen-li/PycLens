# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_CREAT | os.O_WRONLY)
    self.assertRaises(TypeError, os.write, fd, 'beans')
    os.write(fd, b'bacon\n')
    os.write(fd, bytearray(b'eggs\n'))
    os.write(fd, memoryview(b'spam\n'))
    os.close(fd)
    with open(os_helper.TESTFN, 'rb') as fobj:
        self.assertEqual(fobj.read().splitlines(), [b'bacon', b'eggs', b'spam'])
