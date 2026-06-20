# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_dont_copy_file_onto_link_to_itself

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN)
    src = os.path.join(TESTFN, 'cheese')
    dst = os.path.join(TESTFN, 'shop')
    try:
        with open(src, 'w', encoding='utf-8') as f:
            f.write('cheddar')
        try:
            os.link(src, dst)
        except PermissionError as e:
            self.skipTest('os.link(): %s' % e)
        self.assertRaises(shutil.SameFileError, shutil.copyfile, src, dst)
        with open(src, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'cheddar')
        os.remove(dst)
    finally:
        shutil.rmtree(TESTFN, ignore_errors=True)
