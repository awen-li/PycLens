# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_metadata

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mtime = 123456789
    with gzip.GzipFile(self.filename, 'w', mtime=mtime) as fWrite:
        fWrite.write(data1)
    with open(self.filename, 'rb') as fRead:
        idBytes = fRead.read(2)
        self.assertEqual(idBytes, b'\x1f\x8b')
        cmByte = fRead.read(1)
        self.assertEqual(cmByte, b'\x08')
        try:
            expectedname = self.filename.encode('Latin-1') + b'\x00'
            expectedflags = b'\x08'
        except UnicodeEncodeError:
            expectedname = b''
            expectedflags = b'\x00'
        flagsByte = fRead.read(1)
        self.assertEqual(flagsByte, expectedflags)
        mtimeBytes = fRead.read(4)
        self.assertEqual(mtimeBytes, struct.pack('<i', mtime))
        xflByte = fRead.read(1)
        self.assertEqual(xflByte, b'\x02')
        osByte = fRead.read(1)
        self.assertEqual(osByte, b'\xff')
        nameBytes = fRead.read(len(expectedname))
        self.assertEqual(nameBytes, expectedname)
        fRead.seek(os.stat(self.filename).st_size - 8)
        crc32Bytes = fRead.read(4)
        self.assertEqual(crc32Bytes, b'\xaf\xd7d\x83')
        isizeBytes = fRead.read(4)
        self.assertEqual(isizeBytes, struct.pack('<i', len(data1)))
