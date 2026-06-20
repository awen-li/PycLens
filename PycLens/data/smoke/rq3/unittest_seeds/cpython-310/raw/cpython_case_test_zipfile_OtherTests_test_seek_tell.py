# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_seek_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = b"Where's Bruce?"
    bloc = txt.find(b'Bruce')
    with zipfile.ZipFile(TESTFN, 'w') as zipf:
        zipf.writestr('foo.txt', txt)
    with zipfile.ZipFile(TESTFN, 'r') as zipf:
        with zipf.open('foo.txt', 'r') as fp:
            fp.seek(bloc, os.SEEK_SET)
            self.assertEqual(fp.tell(), bloc)
            fp.seek(-bloc, os.SEEK_CUR)
            self.assertEqual(fp.tell(), 0)
            fp.seek(bloc, os.SEEK_CUR)
            self.assertEqual(fp.tell(), bloc)
            self.assertEqual(fp.read(5), txt[bloc:bloc + 5])
            fp.seek(0, os.SEEK_END)
            self.assertEqual(fp.tell(), len(txt))
            fp.seek(0, os.SEEK_SET)
            self.assertEqual(fp.tell(), 0)
    data = io.BytesIO()
    with zipfile.ZipFile(data, mode='w') as zipf:
        zipf.writestr('foo.txt', txt)
    with zipfile.ZipFile(data, mode='r') as zipf:
        with zipf.open('foo.txt', 'r') as fp:
            fp.seek(bloc, os.SEEK_SET)
            self.assertEqual(fp.tell(), bloc)
            fp.seek(-bloc, os.SEEK_CUR)
            self.assertEqual(fp.tell(), 0)
            fp.seek(bloc, os.SEEK_CUR)
            self.assertEqual(fp.tell(), bloc)
            self.assertEqual(fp.read(5), txt[bloc:bloc + 5])
            fp.seek(0, os.SEEK_END)
            self.assertEqual(fp.tell(), len(txt))
            fp.seek(0, os.SEEK_SET)
            self.assertEqual(fp.tell(), 0)
