# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_seeking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    chunk_size = _default_chunk_size()
    prefix_size = chunk_size - 2
    u_prefix = 'a' * prefix_size
    prefix = bytes(u_prefix.encode('utf-8'))
    self.assertEqual(len(u_prefix), len(prefix))
    u_suffix = '袈\n'
    suffix = bytes(u_suffix.encode('utf-8'))
    line = prefix + suffix
    with self.open(os_helper.TESTFN, 'wb') as f:
        f.write(line * 2)
    with self.open(os_helper.TESTFN, 'r', encoding='utf-8') as f:
        s = f.read(prefix_size)
        self.assertEqual(s, str(prefix, 'ascii'))
        self.assertEqual(f.tell(), prefix_size)
        self.assertEqual(f.readline(), u_suffix)
