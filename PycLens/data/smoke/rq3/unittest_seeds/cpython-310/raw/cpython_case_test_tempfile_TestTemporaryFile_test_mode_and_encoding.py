# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryFile_test_mode_and_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def roundtrip(input, *args, **kwargs):
        with tempfile.TemporaryFile(*args, **kwargs) as fileobj:
            fileobj.write(input)
            fileobj.seek(0)
            self.assertEqual(input, fileobj.read())
    roundtrip(b'1234', 'w+b')
    roundtrip('abdc\n', 'w+')
    roundtrip('Λ', 'w+', encoding='utf-16')
    roundtrip('foo\r\n', 'w+', newline='')
