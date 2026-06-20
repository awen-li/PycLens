# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: DecryptionTests_test_seek_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.zip.setpassword(b'python')
    txt = self.plain
    test_word = b'encryption'
    bloc = txt.find(test_word)
    bloc_len = len(test_word)
    with self.zip.open('test.txt', 'r') as fp:
        fp.seek(bloc, os.SEEK_SET)
        self.assertEqual(fp.tell(), bloc)
        fp.seek(-bloc, os.SEEK_CUR)
        self.assertEqual(fp.tell(), 0)
        fp.seek(bloc, os.SEEK_CUR)
        self.assertEqual(fp.tell(), bloc)
        self.assertEqual(fp.read(bloc_len), txt[bloc:bloc + bloc_len])
        old_read_size = fp.MIN_READ_SIZE
        fp.MIN_READ_SIZE = 1
        fp._readbuffer = b''
        fp._offset = 0
        fp.seek(0, os.SEEK_SET)
        self.assertEqual(fp.tell(), 0)
        fp.seek(bloc, os.SEEK_CUR)
        self.assertEqual(fp.read(bloc_len), txt[bloc:bloc + bloc_len])
        fp.MIN_READ_SIZE = old_read_size
        fp.seek(0, os.SEEK_END)
        self.assertEqual(fp.tell(), len(txt))
        fp.seek(0, os.SEEK_SET)
        self.assertEqual(fp.tell(), 0)
        fp.read()
