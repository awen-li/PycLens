# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocWithMetaClasses_test_resolve_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with captured_stdout() as help_io:
        pydoc.help('enum.Enum')
    helptext = help_io.getvalue()
    self.assertIn('class Enum', helptext)
