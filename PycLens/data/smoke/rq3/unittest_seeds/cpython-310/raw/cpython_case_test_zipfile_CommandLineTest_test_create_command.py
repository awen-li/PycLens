# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: CommandLineTest_test_create_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(unlink, TESTFN)
    with open(TESTFN, 'w', encoding='utf-8') as f:
        f.write('test 1')
    os.mkdir(TESTFNDIR)
    self.addCleanup(rmtree, TESTFNDIR)
    with open(os.path.join(TESTFNDIR, 'file.txt'), 'w', encoding='utf-8') as f:
        f.write('test 2')
    files = [TESTFN, TESTFNDIR]
    namelist = [TESTFN, TESTFNDIR + '/', TESTFNDIR + '/file.txt']
    for opt in ('-c', '--create'):
        try:
            out = self.zipfilecmd(opt, TESTFN2, *files)
            self.assertEqual(out, b'')
            with zipfile.ZipFile(TESTFN2) as zf:
                self.assertEqual(zf.namelist(), namelist)
                self.assertEqual(zf.read(namelist[0]), b'test 1')
                self.assertEqual(zf.read(namelist[2]), b'test 2')
        finally:
            unlink(TESTFN2)
