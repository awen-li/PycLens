# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_extractall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tarname, encoding='iso8859-1')
    DIR = os.path.join(TEMPDIR, 'extractall')
    os.mkdir(DIR)
    try:
        directories = [t for t in tar if t.isdir()]
        tar.extractall(DIR, directories, filter='fully_trusted')
        for tarinfo in directories:
            path = os.path.join(DIR, tarinfo.name)
            if sys.platform != 'win32':
                self.assertEqual(tarinfo.mode & 511, os.stat(path).st_mode & 511, tarinfo.name)

            def format_mtime(mtime):
                if isinstance(mtime, float):
                    return '{} ({})'.format(mtime, mtime.hex())
                else:
                    return '{!r} (int)'.format(mtime)
            file_mtime = os.path.getmtime(path)
            errmsg = 'tar mtime {0} != file time {1} of path {2!a}'.format(format_mtime(tarinfo.mtime), format_mtime(file_mtime), path)
            self.assertEqual(tarinfo.mtime, file_mtime, errmsg)
    finally:
        tar.close()
        os_helper.rmtree(DIR)
