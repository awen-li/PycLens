# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CTextIOWrapperTest_test_internal_buffer_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    chunk_size = 8192

    class MockIO(self.MockRawIO):

        def write(self, data):
            if len(data) > chunk_size:
                raise RuntimeError
            return super().write(data)
    buf = MockIO()
    t = self.TextIOWrapper(buf, encoding='ascii')
    chunk_size = t._CHUNK_SIZE
    t.write('abc')
    t.write('def')
    self.assertEqual([], buf._write_stack)
    with self.assertRaises(RuntimeError):
        t.write('x' * (chunk_size + 1))
    self.assertEqual([b'abcdef'], buf._write_stack)
    t.write('ghi')
    t.write('x' * chunk_size)
    self.assertEqual([b'abcdef', b'ghi', b'x' * chunk_size], buf._write_stack)
