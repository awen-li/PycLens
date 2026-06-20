# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_199

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Color(int, enum.Enum):
        RED = 0
        GREEN = 1
        BLUE = 2

    def f(color):
        match color:
            case Color.RED:
                return 'I see red!'
            case Color.GREEN:
                return 'Grass is green'
            case Color.BLUE:
                return "I'm feeling the blues :("
    self.assertEqual(f(Color.RED), 'I see red!')
    self.assertEqual(f(Color.GREEN), 'Grass is green')
    self.assertEqual(f(Color.BLUE), "I'm feeling the blues :(")
    self.assertIs(f(Color), None)
    self.assertEqual(f(0), 'I see red!')
    self.assertEqual(f(1), 'Grass is green')
    self.assertEqual(f(2), "I'm feeling the blues :(")
    self.assertIs(f(3), None)
    self.assertEqual(f(False), 'I see red!')
    self.assertEqual(f(True), 'Grass is green')
    self.assertEqual(f(2 + 0j), "I'm feeling the blues :(")
    self.assertIs(f(3.0), None)
