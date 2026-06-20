# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_user

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uid = os.geteuid()
    test_users = [65534 if uid != 65534 else 65533, uid]
    name_uid = 'nobody' if sys.platform != 'darwin' else 'unknown'
    if pwd is not None:
        try:
            pwd.getpwnam(name_uid)
            test_users.append(name_uid)
        except KeyError:
            name_uid = None
    for user in test_users:
        for close_fds in (False, True):
            with self.subTest(user=user, close_fds=close_fds):
                try:
                    output = subprocess.check_output([sys.executable, '-c', 'import os; print(os.getuid())'], user=user, close_fds=close_fds)
                except PermissionError:
                    pass
                except OSError as e:
                    if e.errno not in (errno.EACCES, errno.EPERM):
                        raise
                else:
                    if isinstance(user, str):
                        user_uid = pwd.getpwnam(user).pw_uid
                    else:
                        user_uid = user
                    child_user = int(output)
                    self.assertEqual(child_user, user_uid)
    with self.assertRaises(ValueError):
        subprocess.check_call(ZERO_RETURN_CMD, user=-1)
    with self.assertRaises(OverflowError):
        subprocess.check_call(ZERO_RETURN_CMD, cwd=os.curdir, env=os.environ, user=2 ** 64)
    if pwd is None and name_uid is not None:
        with self.assertRaises(ValueError):
            subprocess.check_call(ZERO_RETURN_CMD, user=name_uid)
