# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_truncated_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = io.BytesIO()
    with zipfile.ZipFile(fp, mode='w') as zipf:
        zipf.writestr('strfile', self.data, compress_type=self.compression)
        end_offset = fp.tell()
    zipfiledata = fp.getvalue()
    fp = io.BytesIO(zipfiledata)
    with zipfile.ZipFile(fp) as zipf:
        with zipf.open('strfile') as zipopen:
            fp.truncate(end_offset - 20)
            with self.assertRaises(EOFError):
                zipopen.read()
    fp = io.BytesIO(zipfiledata)
    with zipfile.ZipFile(fp) as zipf:
        with zipf.open('strfile') as zipopen:
            fp.truncate(end_offset - 20)
            with self.assertRaises(EOFError):
                while zipopen.read(100):
                    pass
    fp = io.BytesIO(zipfiledata)
    with zipfile.ZipFile(fp) as zipf:
        with zipf.open('strfile') as zipopen:
            fp.truncate(end_offset - 20)
            with self.assertRaises(EOFError):
                while zipopen.read1(100):
                    pass
