# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pwd.py
# case: PwdTest_test_values_extended

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entries = pwd.getpwall()
    entriesbyname = {}
    entriesbyuid = {}
    if len(entries) > 1000:
        self.skipTest('passwd file is huge; extended test skipped')
    for e in entries:
        entriesbyname.setdefault(e.pw_name, []).append(e)
        entriesbyuid.setdefault(e.pw_uid, []).append(e)
    for e in entries:
        if not e[0] or e[0] == '+':
            continue
        self.assertIn(pwd.getpwnam(e.pw_name), entriesbyname[e.pw_name])
        self.assertIn(pwd.getpwuid(e.pw_uid), entriesbyuid[e.pw_uid])
