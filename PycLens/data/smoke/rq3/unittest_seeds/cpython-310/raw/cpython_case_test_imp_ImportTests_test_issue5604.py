# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue5604

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fs_encoding = sys.getfilesystemencoding()
    known_locales = {'utf-8': b'\xc3\xa4', 'cp1250': b'\x8c', 'cp1251': b'\xc0', 'cp1252': b'\xc0', 'cp1253': b'\xc1', 'cp1254': b'\xc0', 'cp1255': b'\xe0', 'cp1256': b'\xe0', 'cp1257': b'\xc0', 'cp1258': b'\xc0'}
    if sys.platform == 'darwin':
        self.assertEqual(fs_encoding, 'utf-8')
        special_char = b'a\xcc\x88'
    else:
        special_char = known_locales.get(fs_encoding)
    if not special_char:
        self.skipTest("can't run this test with %s as filesystem encoding" % fs_encoding)
    decoded_char = special_char.decode(fs_encoding)
    temp_mod_name = 'test_imp_helper_' + decoded_char
    test_package_name = 'test_imp_helper_package_' + decoded_char
    init_file_name = os.path.join(test_package_name, '__init__.py')
    try:
        sys.path.insert(0, os.curdir)
        with open(temp_mod_name + '.py', 'w', encoding='utf-8') as file:
            file.write('a = 1\n')
        (file, filename, info) = imp.find_module(temp_mod_name)
        with file:
            self.assertIsNotNone(file)
            self.assertTrue(filename[:-3].endswith(temp_mod_name))
            self.assertEqual(info[0], '.py')
            self.assertEqual(info[1], 'r')
            self.assertEqual(info[2], imp.PY_SOURCE)
            mod = imp.load_module(temp_mod_name, file, filename, info)
            self.assertEqual(mod.a, 1)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            mod = imp.load_source(temp_mod_name, temp_mod_name + '.py')
        self.assertEqual(mod.a, 1)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            if not sys.dont_write_bytecode:
                mod = imp.load_compiled(temp_mod_name, imp.cache_from_source(temp_mod_name + '.py'))
        self.assertEqual(mod.a, 1)
        if not os.path.exists(test_package_name):
            os.mkdir(test_package_name)
        with open(init_file_name, 'w', encoding='utf-8') as file:
            file.write('b = 2\n')
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            package = imp.load_package(test_package_name, test_package_name)
        self.assertEqual(package.b, 2)
    finally:
        del sys.path[0]
        for ext in ('.py', '.pyc'):
            os_helper.unlink(temp_mod_name + ext)
            os_helper.unlink(init_file_name + ext)
        os_helper.rmtree(test_package_name)
        os_helper.rmtree('__pycache__')
