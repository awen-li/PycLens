# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_modes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add('all_bits', mode='?rwsrwsrwt')
        arc.add('perm_bits', mode='?rwxrwxrwx')
        arc.add('exec_group_other', mode='?rw-rwxrwx')
        arc.add('read_group_only', mode='?---r-----')
        arc.add('no_bits', mode='?---------')
        arc.add('dir/', mode='?---rwsrwt')
    tmp_filename = os.path.join(TEMPDIR, 'tmp.file')
    with open(tmp_filename, 'w'):
        pass
    os.chmod(tmp_filename, os.stat(tmp_filename).st_mode | stat.S_ISVTX)
    have_sticky_files = os.stat(tmp_filename).st_mode & stat.S_ISVTX
    os.unlink(tmp_filename)
    os.mkdir(tmp_filename)
    os.chmod(tmp_filename, os.stat(tmp_filename).st_mode | stat.S_ISVTX)
    have_sticky_dirs = os.stat(tmp_filename).st_mode & stat.S_ISVTX
    os.rmdir(tmp_filename)
    with self.check_context(arc.open(), 'fully_trusted'):
        if have_sticky_files:
            self.expect_file('all_bits', mode='?rwsrwsrwt')
        else:
            self.expect_file('all_bits', mode='?rwsrwsrwx')
        self.expect_file('perm_bits', mode='?rwxrwxrwx')
        self.expect_file('exec_group_other', mode='?rw-rwxrwx')
        self.expect_file('read_group_only', mode='?---r-----')
        self.expect_file('no_bits', mode='?---------')
        if have_sticky_dirs:
            self.expect_file('dir/', mode='?---rwsrwt')
        else:
            self.expect_file('dir/', mode='?---rwsrwx')
    with self.check_context(arc.open(), 'tar'):
        self.expect_file('all_bits', mode='?rwxr-xr-x')
        self.expect_file('perm_bits', mode='?rwxr-xr-x')
        self.expect_file('exec_group_other', mode='?rw-r-xr-x')
        self.expect_file('read_group_only', mode='?---r-----')
        self.expect_file('no_bits', mode='?---------')
        self.expect_file('dir/', mode='?---r-xr-x')
    with self.check_context(arc.open(), 'data'):
        normal_dir_mode = stat.filemode(stat.S_IMODE(self.outerdir.stat().st_mode))
        self.expect_file('all_bits', mode='?rwxr-xr-x')
        self.expect_file('perm_bits', mode='?rwxr-xr-x')
        self.expect_file('exec_group_other', mode='?rw-r--r--')
        self.expect_file('read_group_only', mode='?rw-r-----')
        self.expect_file('no_bits', mode='?rw-------')
        self.expect_file('dir/', mode=normal_dir_mode)
