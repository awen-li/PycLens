# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_open_encoding_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    in_memory_file = io.BytesIO()
    zf = zipfile.ZipFile(in_memory_file, 'w')
    zf.writestr('path/bad-utf8.bin', b'invalid utf-8: \xff\xff.')
    zf.filename = 'test_read_text_encoding_errors.zip'
    root = zipfile.Path(zf)
    (path,) = root.iterdir()
    u16 = path.joinpath('bad-utf8.bin')
    data = u16.read_text('utf-8', errors='ignore')
    self.assertEqual(data, 'invalid utf-8: .')
    with u16.open('r', 'utf-8', errors='surrogateescape') as f:
        self.assertEqual(f.read(), 'invalid utf-8: \udcff\udcff.')
    with self.assertRaisesRegex(TypeError, 'encoding'):
        data = u16.read_text('utf-8', encoding='utf-8')
    with u16.open('r', encoding='utf-8', errors='strict') as f:
        with self.assertRaises(UnicodeDecodeError):
            f.read()
