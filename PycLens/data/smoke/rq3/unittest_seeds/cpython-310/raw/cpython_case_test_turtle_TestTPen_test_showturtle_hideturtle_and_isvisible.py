# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTPen_test_showturtle_hideturtle_and_isvisible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tpen = turtle.TPen()
    self.assertTrue(tpen.isvisible())
    tpen.hideturtle()
    self.assertFalse(tpen.isvisible())
    tpen.showturtle()
    self.assertTrue(tpen.isvisible())
