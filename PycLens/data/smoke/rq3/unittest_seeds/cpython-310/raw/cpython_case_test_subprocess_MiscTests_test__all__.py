# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: MiscTests_test__all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    intentionally_excluded = {'list2cmdline', 'Handle', 'pwd', 'grp', 'fcntl'}
    exported = set(subprocess.__all__)
    possible_exports = set()
    import types
    for (name, value) in subprocess.__dict__.items():
        if name.startswith('_'):
            continue
        if isinstance(value, (types.ModuleType,)):
            continue
        possible_exports.add(name)
    self.assertEqual(exported, possible_exports - intentionally_excluded)
