# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_extra_groups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gid = os.getegid()
    group_list = [65534 if gid != 65534 else 65533]
    name_group = _get_test_grp_name()
    perm_error = False
    if grp is not None:
        group_list.append(name_group)
    try:
        output = subprocess.check_output([sys.executable, '-c', 'import os, sys, json; json.dump(os.getgroups(), sys.stdout)'], extra_groups=group_list)
    except OSError as ex:
        if ex.errno != errno.EPERM:
            raise
        perm_error = True
    else:
        parent_groups = os.getgroups()
        child_groups = json.loads(output)
        if grp is not None:
            desired_gids = [grp.getgrnam(g).gr_gid if isinstance(g, str) else g for g in group_list]
        else:
            desired_gids = group_list
        if perm_error:
            self.assertEqual(set(child_groups), set(parent_groups))
        else:
            self.assertEqual(set(desired_gids), set(child_groups))
    with self.assertRaises(ValueError):
        subprocess.check_call(ZERO_RETURN_CMD, extra_groups=[-1])
    with self.assertRaises(ValueError):
        subprocess.check_call(ZERO_RETURN_CMD, cwd=os.curdir, env=os.environ, extra_groups=[2 ** 64])
    if grp is None:
        with self.assertRaises(ValueError):
            subprocess.check_call(ZERO_RETURN_CMD, extra_groups=[name_group])
