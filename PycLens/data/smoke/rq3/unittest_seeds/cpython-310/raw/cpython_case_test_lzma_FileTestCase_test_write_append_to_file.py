# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_write_append_to_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    part1 = INPUT[:1024]
    part2 = INPUT[1024:1536]
    part3 = INPUT[1536:]
    expected = b''.join((lzma.compress(x) for x in (part1, part2, part3)))
    try:
        with LZMAFile(TESTFN, 'w') as f:
            f.write(part1)
        with LZMAFile(TESTFN, 'a') as f:
            f.write(part2)
        with LZMAFile(TESTFN, 'a') as f:
            f.write(part3)
        with open(TESTFN, 'rb') as f:
            self.assertEqual(f.read(), expected)
    finally:
        unlink(TESTFN)
