# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: BasicUnicodeTest_test_seek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '%s\n%s\n' % (100 * 'abc123', 100 * 'def456')
    for encoding in all_unicode_encodings:
        if encoding == 'idna':
            continue
        if encoding in broken_unicode_with_stateful:
            continue
        reader = codecs.getreader(encoding)(io.BytesIO(s.encode(encoding)))
        for t in range(5):
            reader.seek(0, 0)
            data = reader.read()
            self.assertEqual(s, data)
