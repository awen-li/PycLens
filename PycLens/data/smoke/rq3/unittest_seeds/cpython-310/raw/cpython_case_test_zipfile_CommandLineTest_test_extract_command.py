# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: CommandLineTest_test_extract_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zip_name = findfile('zipdir.zip')
    for opt in ('-e', '--extract'):
        with temp_dir() as extdir:
            out = self.zipfilecmd(opt, zip_name, extdir)
            self.assertEqual(out, b'')
            with zipfile.ZipFile(zip_name) as zf:
                for zi in zf.infolist():
                    path = os.path.join(extdir, zi.filename.replace('/', os.sep))
                    if zi.is_dir():
                        self.assertTrue(os.path.isdir(path))
                    else:
                        self.assertTrue(os.path.isfile(path))
                        with open(path, 'rb') as f:
                            self.assertEqual(f.read(), zf.read(zi))
