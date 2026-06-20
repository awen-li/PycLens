# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_introspection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Number(IntEnum):
        one = 100
        two = 200
    self.assertIs(Number.one._member_type_, int)
    self.assertIs(Number._member_type_, int)

    class String(str, Enum):
        yarn = 'soft'
        rope = 'rough'
        wire = 'hard'
    self.assertIs(String.yarn._member_type_, str)
    self.assertIs(String._member_type_, str)

    class Plain(Enum):
        vanilla = 'white'
        one = 1
    self.assertIs(Plain.vanilla._member_type_, object)
    self.assertIs(Plain._member_type_, object)
