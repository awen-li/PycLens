# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_repl.py
# case: TestInteractiveInterpreter_test_multiline_string_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    user_input = '        x = """<?xml version="1.0" encoding="iso-8859-1"?>\n        <test>\n            <Users>\n                <fun25>\n                    <limits>\n                        <total>0KiB</total>\n                        <kbps>0</kbps>\n                        <rps>1.3</rps>\n                        <connections>0</connections>\n                    </limits>\n                    <usages>\n                        <total>16738211KiB</total>\n                        <kbps>237.15</kbps>\n                        <rps>1.3</rps>\n                        <connections>0</connections>\n                    </usages>\n                    <time_to_refresh>never</time_to_refresh>\n                    <limit_exceeded_URL>none</limit_exceeded_URL>\n                </fun25>\n            </Users>\n        </test>"""\n        '
    user_input = dedent(user_input)
    p = spawn_repl()
    p.stdin.write(user_input)
    output = kill_python(p)
    self.assertEqual(p.returncode, 0)
