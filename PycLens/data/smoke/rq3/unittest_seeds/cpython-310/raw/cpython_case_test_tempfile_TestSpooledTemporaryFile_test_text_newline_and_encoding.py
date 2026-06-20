# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_text_newline_and_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tempfile.SpooledTemporaryFile(mode='w+', max_size=10, newline='', encoding='utf-8', errors='ignore')
    f.write('Λ\r\n')
    f.seek(0)
    self.assertEqual(f.read(), 'Λ\r\n')
    self.assertFalse(f._rolled)
    self.assertEqual(f.mode, 'w+')
    self.assertIsNone(f.name)
    self.assertIsNotNone(f.newlines)
    self.assertEqual(f.encoding, 'utf-8')
    self.assertEqual(f.errors, 'ignore')
    f.write('Μ' * 10 + '\r\n')
    f.write('Ν' * 20)
    f.seek(0)
    self.assertEqual(f.read(), 'Λ\r\n' + 'Μ' * 10 + '\r\n' + 'Ν' * 20)
    self.assertTrue(f._rolled)
    self.assertEqual(f.mode, 'w+')
    self.assertIsNotNone(f.name)
    self.assertIsNotNone(f.newlines)
    self.assertEqual(f.encoding, 'utf-8')
    self.assertEqual(f.errors, 'ignore')
