# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_braced_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyTemplate(Template):
        pattern = '\n            \\$(?:\n              (?P<escaped>$)                     |\n              (?P<named>[_a-z][_a-z0-9]*)        |\n              @@(?P<braced>[_a-z][_a-z0-9]*)@@   |\n              (?P<invalid>)                      |\n           )\n           '
    tmpl = 'PyCon in $@@location@@'
    t = MyTemplate(tmpl)
    self.assertRaises(KeyError, t.substitute, {})
    val = t.substitute({'location': 'Cleveland'})
    self.assertEqual(val, 'PyCon in Cleveland')
