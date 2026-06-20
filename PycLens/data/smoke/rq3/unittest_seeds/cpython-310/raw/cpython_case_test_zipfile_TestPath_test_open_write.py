# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_open_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zf = zipfile.Path(zipfile.ZipFile(io.BytesIO(), mode='w'))
    with zf.joinpath('file.bin').open('wb') as strm:
        strm.write(b'binary contents')
    with zf.joinpath('file.txt').open('w', encoding='utf-8') as strm:
        strm.write('text file')
