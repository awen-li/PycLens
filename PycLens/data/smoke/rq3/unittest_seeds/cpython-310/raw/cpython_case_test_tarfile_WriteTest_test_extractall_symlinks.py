# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_extractall_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tempdir = os.path.join(TEMPDIR, 'testsymlinks')
    temparchive = os.path.join(TEMPDIR, 'testsymlinks.tar')
    os.mkdir(tempdir)
    try:
        source_file = os.path.join(tempdir, 'source')
        target_file = os.path.join(tempdir, 'symlink')
        with open(source_file, 'w') as f:
            f.write('something\n')
        os.symlink(source_file, target_file)
        with tarfile.open(temparchive, 'w') as tar:
            tar.add(source_file, arcname='source')
            tar.add(target_file, arcname='symlink')
        with tarfile.open(temparchive, errorlevel=2) as tar:
            try:
                tar.extractall(path=tempdir, filter='fully_trusted')
            except OSError:
                self.fail('extractall failed with symlinked files')
    finally:
        os_helper.unlink(temparchive)
        os_helper.rmtree(tempdir)
