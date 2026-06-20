# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    self.assertEqual(repr(Perm.R), '<Perm.R: 4>')
    self.assertEqual(repr(Perm.W), '<Perm.W: 2>')
    self.assertEqual(repr(Perm.X), '<Perm.X: 1>')
    self.assertEqual(repr(Perm.R | Perm.W), '<Perm.R|W: 6>')
    self.assertEqual(repr(Perm.R | Perm.W | Perm.X), '<Perm.R|W|X: 7>')
    self.assertEqual(repr(Perm(0)), '<Perm.0: 0>')
    self.assertEqual(repr(~Perm.R), '<Perm.W|X: 3>')
    self.assertEqual(repr(~Perm.W), '<Perm.R|X: 5>')
    self.assertEqual(repr(~Perm.X), '<Perm.R|W: 6>')
    self.assertEqual(repr(~(Perm.R | Perm.W)), '<Perm.X: 1>')
    self.assertEqual(repr(~(Perm.R | Perm.W | Perm.X)), '<Perm.0: 0>')
    self.assertEqual(repr(Perm(~0)), '<Perm.R|W|X: 7>')
    Open = self.Open
    self.assertEqual(repr(Open.RO), '<Open.RO: 0>')
    self.assertEqual(repr(Open.WO), '<Open.WO: 1>')
    self.assertEqual(repr(Open.AC), '<Open.AC: 3>')
    self.assertEqual(repr(Open.RO | Open.CE), '<Open.CE: 524288>')
    self.assertEqual(repr(Open.WO | Open.CE), '<Open.CE|WO: 524289>')
    self.assertEqual(repr(~Open.RO), '<Open.CE|AC|RW|WO: 524291>')
    self.assertEqual(repr(~Open.WO), '<Open.CE|RW: 524290>')
    self.assertEqual(repr(~Open.AC), '<Open.CE: 524288>')
    self.assertEqual(repr(~(Open.RO | Open.CE)), '<Open.AC: 3>')
    self.assertEqual(repr(~(Open.WO | Open.CE)), '<Open.RW: 2>')
