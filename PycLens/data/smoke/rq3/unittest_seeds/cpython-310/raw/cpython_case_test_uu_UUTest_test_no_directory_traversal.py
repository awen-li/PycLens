# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUTest_test_no_directory_traversal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    relative_bad = b'begin 644 ../../../../../../../../tmp/test1\n$86)C"@``\n`\nend\n'
    with self.assertRaisesRegex(uu.Error, 'directory'):
        uu.decode(io.BytesIO(relative_bad))
    if os.altsep:
        relative_bad_bs = relative_bad.replace(b'/', b'\\')
        with self.assertRaisesRegex(uu.Error, 'directory'):
            uu.decode(io.BytesIO(relative_bad_bs))
    absolute_bad = b'begin 644 /tmp/test2\n$86)C"@``\n`\nend\n'
    with self.assertRaisesRegex(uu.Error, 'directory'):
        uu.decode(io.BytesIO(absolute_bad))
    if os.altsep:
        absolute_bad_bs = absolute_bad.replace(b'/', b'\\')
        with self.assertRaisesRegex(uu.Error, 'directory'):
            uu.decode(io.BytesIO(absolute_bad_bs))
