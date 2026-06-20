# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicExternalTest_test_external

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = support.findfile('clinic.test')
    with open(source, 'r', encoding='utf-8') as f:
        orig_contents = f.read()
    with os_helper.temp_dir() as tmp_dir:
        testfile = os.path.join(tmp_dir, 'clinic.test.c')
        with open(testfile, 'w', encoding='utf-8') as f:
            f.write(orig_contents)
        old_mtime_ns = os.stat(testfile).st_mtime_ns
        clinic.parse_file(testfile)
        with open(testfile, 'r', encoding='utf-8') as f:
            new_contents = f.read()
        new_mtime_ns = os.stat(testfile).st_mtime_ns
    self.assertEqual(new_contents, orig_contents)
    self.assertEqual(new_mtime_ns, old_mtime_ns)
