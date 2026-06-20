# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMisc_test_chown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirname = self.mkdtemp()
    filename = tempfile.mktemp(dir=dirname)
    write_file(filename, 'testing chown function')
    with self.assertRaises(ValueError):
        shutil.chown(filename)
    with self.assertRaises(LookupError):
        shutil.chown(filename, user='non-existing username')
    with self.assertRaises(LookupError):
        shutil.chown(filename, group='non-existing groupname')
    with self.assertRaises(TypeError):
        shutil.chown(filename, b'spam')
    with self.assertRaises(TypeError):
        shutil.chown(filename, 3.14)
    uid = os.getuid()
    gid = os.getgid()

    def check_chown(path, uid=None, gid=None):
        s = os.stat(filename)
        if uid is not None:
            self.assertEqual(uid, s.st_uid)
        if gid is not None:
            self.assertEqual(gid, s.st_gid)
    shutil.chown(filename, uid, gid)
    check_chown(filename, uid, gid)
    shutil.chown(filename, uid)
    check_chown(filename, uid)
    shutil.chown(filename, user=uid)
    check_chown(filename, uid)
    shutil.chown(filename, group=gid)
    check_chown(filename, gid=gid)
    shutil.chown(dirname, uid, gid)
    check_chown(dirname, uid, gid)
    shutil.chown(dirname, uid)
    check_chown(dirname, uid)
    shutil.chown(dirname, user=uid)
    check_chown(dirname, uid)
    shutil.chown(dirname, group=gid)
    check_chown(dirname, gid=gid)
    try:
        user = pwd.getpwuid(uid)[0]
        group = grp.getgrgid(gid)[0]
    except KeyError:
        pass
    else:
        shutil.chown(filename, user, group)
        check_chown(filename, uid, gid)
        shutil.chown(dirname, user, group)
        check_chown(dirname, uid, gid)
