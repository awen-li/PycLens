# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_register_archive_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, register_archive_format, 'xxx', 1)
    self.assertRaises(TypeError, register_archive_format, 'xxx', lambda : x, 1)
    self.assertRaises(TypeError, register_archive_format, 'xxx', lambda : x, [(1, 2), (1, 2, 3)])
    register_archive_format('xxx', lambda : x, [(1, 2)], 'xxx file')
    formats = [name for (name, params) in get_archive_formats()]
    self.assertIn('xxx', formats)
    unregister_archive_format('xxx')
    formats = [name for (name, params) in get_archive_formats()]
    self.assertNotIn('xxx', formats)
