# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_mlsd_test_entry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    type = 'type' if type is None else type
    perm = 'perm' if perm is None else perm
    unique = 'unique' if unique is None else unique
    name = 'name' if name is None else name
    set_data(line)
    (_name, facts) = next(self.client.mlsd())
    self.assertEqual(_name, name)
    self.assertEqual(facts['type'], type)
    self.assertEqual(facts['perm'], perm)
    self.assertEqual(facts['unique'], unique)
