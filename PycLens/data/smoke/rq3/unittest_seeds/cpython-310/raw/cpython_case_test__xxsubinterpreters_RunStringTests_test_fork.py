# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import tempfile
    with tempfile.NamedTemporaryFile('w+', encoding='utf-8') as file:
        file.write('')
        file.flush()
        expected = 'spam spam spam spam spam'
        script = dedent(f"\n                import os\n                try:\n                    os.fork()\n                except RuntimeError:\n                    with open('{file.name}', 'w', encoding='utf-8') as out:\n                        out.write('{expected}')\n                ")
        interpreters.run_string(self.id, script)
        file.seek(0)
        content = file.read()
        self.assertEqual(content, expected)
