# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gid = os.getegid()
    group_list = [65534 if gid != 65534 else 65533]
    name_group = _get_test_grp_name()
    if grp is not None:
        group_list.append(name_group)
    for group in group_list + [gid]:
        for close_fds in (False, True):
            with self.subTest(group=group, close_fds=close_fds):
                try:
                    output = subprocess.check_output([sys.executable, '-c', 'import os; print(os.getgid())'], group=group, close_fds=close_fds)
                except PermissionError:
                    pass
                else:
                    if isinstance(group, str):
                        group_gid = grp.getgrnam(group).gr_gid
                    else:
                        group_gid = group
                    child_group = int(output)
                    self.assertEqual(child_group, group_gid)
    with self.assertRaises(ValueError):
        subprocess.check_call(ZERO_RETURN_CMD, group=-1)
    with self.assertRaises(OverflowError):
        subprocess.check_call(ZERO_RETURN_CMD, cwd=os.curdir, env=os.environ, group=2 ** 64)
    if grp is None:
        with self.assertRaises(ValueError):
            subprocess.check_call(ZERO_RETURN_CMD, group=name_group)
