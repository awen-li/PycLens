# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = 'file.name'
    for f in get_files(self):
        with zipfile.ZipFile(f, 'w', self.compression) as zipfp:
            zipfp.write(TESTFN, fname)
            r = repr(zipfp)
            self.assertIn("mode='w'", r)
        with zipfile.ZipFile(f, 'r') as zipfp:
            r = repr(zipfp)
            if isinstance(f, str):
                self.assertIn('filename=%r' % f, r)
            else:
                self.assertIn('file=%r' % f, r)
            self.assertIn("mode='r'", r)
            r = repr(zipfp.getinfo(fname))
            self.assertIn('filename=%r' % fname, r)
            self.assertIn('filemode=', r)
            self.assertIn('file_size=', r)
            if self.compression != zipfile.ZIP_STORED:
                self.assertIn('compress_type=', r)
                self.assertIn('compress_size=', r)
            with zipfp.open(fname) as zipopen:
                r = repr(zipopen)
                self.assertIn('name=%r' % fname, r)
                self.assertIn("mode='r'", r)
                if self.compression != zipfile.ZIP_STORED:
                    self.assertIn('compress_type=', r)
            self.assertIn('[closed]', repr(zipopen))
        self.assertIn('[closed]', repr(zipfp))
