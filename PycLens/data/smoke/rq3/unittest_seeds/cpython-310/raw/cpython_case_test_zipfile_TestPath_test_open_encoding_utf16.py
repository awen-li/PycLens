# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_open_encoding_utf16

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    in_memory_file = io.BytesIO()
    zf = zipfile.ZipFile(in_memory_file, 'w')
    zf.writestr('path/16.txt', 'This was utf-16'.encode('utf-16'))
    zf.filename = 'test_open_utf16.zip'
    root = zipfile.Path(zf)
    (path,) = root.iterdir()
    u16 = path.joinpath('16.txt')
    with u16.open('r', 'utf-16') as strm:
        data = strm.read()
    self.assertEqual(data, 'This was utf-16')
    with u16.open(encoding='utf-16') as strm:
        data = strm.read()
    self.assertEqual(data, 'This was utf-16')
