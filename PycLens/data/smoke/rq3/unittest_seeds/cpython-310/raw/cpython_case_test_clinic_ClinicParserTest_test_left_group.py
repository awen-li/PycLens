# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_left_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('\nmodule curses\ncurses.addch\n   [\n   y: int\n     Y-coordinate.\n   x: int\n     X-coordinate.\n   ]\n   ch: char\n     Character to add.\n   [\n   attr: long\n     Attributes for the character.\n   ]\n   /\n')
    for (name, group) in (('y', -1), ('x', -1), ('ch', 0), ('attr', 1)):
        p = function.parameters[name]
        self.assertEqual(p.group, group)
        self.assertEqual(p.kind, inspect.Parameter.POSITIONAL_ONLY)
    self.assertEqual(function.docstring.strip(), '\naddch([y, x,] ch, [attr])\n\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  ch\n    Character to add.\n  attr\n    Attributes for the character.\n            '.strip())
