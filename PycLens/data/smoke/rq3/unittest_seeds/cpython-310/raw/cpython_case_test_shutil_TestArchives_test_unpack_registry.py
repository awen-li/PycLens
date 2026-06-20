# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_unpack_registry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    formats = get_unpack_formats()

    def _boo(filename, extract_dir, extra):
        self.assertEqual(extra, 1)
        self.assertEqual(filename, 'stuff.boo')
        self.assertEqual(extract_dir, 'xx')
    register_unpack_format('Boo', ['.boo', '.b2'], _boo, [('extra', 1)])
    unpack_archive('stuff.boo', 'xx')
    self.assertRaises(RegistryError, register_unpack_format, 'Boo2', ['.boo'], _boo)
    unregister_unpack_format('Boo')
    register_unpack_format('Boo2', ['.boo'], _boo)
    self.assertIn(('Boo2', ['.boo'], ''), get_unpack_formats())
    self.assertNotIn(('Boo', ['.boo'], ''), get_unpack_formats())
    unregister_unpack_format('Boo2')
    self.assertEqual(get_unpack_formats(), formats)
