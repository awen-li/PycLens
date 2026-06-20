# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestKeyedArchive_test_keyed_archive_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = {'$version': 100000, '$objects': ['$null', {'pytype': 1, '$class': UID(2), 'NS.string': 'KeyArchive UID Test'}, {'$classname': 'OC_BuiltinPythonUnicode', '$classes': ['OC_BuiltinPythonUnicode', 'OC_PythonUnicode', 'NSString', 'NSObject'], '$classhints': ['OC_PythonString', 'NSString']}], '$archiver': 'NSKeyedArchiver', '$top': {'root': UID(1)}}
    self.assertEqual(plistlib.loads(TESTDATA['KEYED_ARCHIVE']), data)
