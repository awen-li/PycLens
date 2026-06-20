# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: PublicAPITests_test_module_all_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(hasattr(shutil, '__all__'))
    target_api = ['copyfileobj', 'copyfile', 'copymode', 'copystat', 'copy', 'copy2', 'copytree', 'move', 'rmtree', 'Error', 'SpecialFileError', 'ExecError', 'make_archive', 'get_archive_formats', 'register_archive_format', 'unregister_archive_format', 'get_unpack_formats', 'register_unpack_format', 'unregister_unpack_format', 'unpack_archive', 'ignore_patterns', 'chown', 'which', 'get_terminal_size', 'SameFileError']
    if hasattr(os, 'statvfs') or os.name == 'nt':
        target_api.append('disk_usage')
    self.assertEqual(set(shutil.__all__), set(target_api))
