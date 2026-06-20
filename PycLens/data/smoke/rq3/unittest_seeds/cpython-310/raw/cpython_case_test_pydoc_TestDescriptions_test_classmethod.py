# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_classmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        @classmethod
        def cm(cls, x):
            """A class method"""
            ...
    self.assertEqual(self._get_summary_lines(X.__dict__['cm']), 'cm(...)\n    A class method\n')
    self.assertEqual(self._get_summary_lines(X.cm), 'cm(x) method of builtins.type instance\n    A class method\n')
    self.assertIn('\n |  Class methods defined here:\n |  \n |  cm(x) from builtins.type\n |      A class method\n', pydoc.plain(pydoc.render_doc(X)))
