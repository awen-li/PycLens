# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    self.assertEqual(str(Perm.R), 'Perm.R')
    self.assertEqual(str(Perm.W), 'Perm.W')
    self.assertEqual(str(Perm.X), 'Perm.X')
    self.assertEqual(str(Perm.R | Perm.W), 'Perm.R|W')
    self.assertEqual(str(Perm.R | Perm.W | Perm.X), 'Perm.R|W|X')
    self.assertEqual(str(Perm.R | 8), 'Perm.8|R')
    self.assertEqual(str(Perm(0)), 'Perm.0')
    self.assertEqual(str(Perm(8)), 'Perm.8')
    self.assertEqual(str(~Perm.R), 'Perm.W|X')
    self.assertEqual(str(~Perm.W), 'Perm.R|X')
    self.assertEqual(str(~Perm.X), 'Perm.R|W')
    self.assertEqual(str(~(Perm.R | Perm.W)), 'Perm.X')
    self.assertEqual(str(~(Perm.R | Perm.W | Perm.X)), 'Perm.-8')
    self.assertEqual(str(~(Perm.R | 8)), 'Perm.W|X')
    self.assertEqual(str(Perm(~0)), 'Perm.R|W|X')
    self.assertEqual(str(Perm(~8)), 'Perm.R|W|X')
    Open = self.Open
    self.assertEqual(str(Open.RO), 'Open.RO')
    self.assertEqual(str(Open.WO), 'Open.WO')
    self.assertEqual(str(Open.AC), 'Open.AC')
    self.assertEqual(str(Open.RO | Open.CE), 'Open.CE')
    self.assertEqual(str(Open.WO | Open.CE), 'Open.CE|WO')
    self.assertEqual(str(Open(4)), 'Open.4')
    self.assertEqual(str(~Open.RO), 'Open.CE|AC|RW|WO')
    self.assertEqual(str(~Open.WO), 'Open.CE|RW')
    self.assertEqual(str(~Open.AC), 'Open.CE')
    self.assertEqual(str(~(Open.RO | Open.CE)), 'Open.AC|RW|WO')
    self.assertEqual(str(~(Open.WO | Open.CE)), 'Open.RW')
    self.assertEqual(str(Open(~4)), 'Open.CE|AC|RW|WO')
