# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_staticmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        @staticmethod
        def sm(x, y):
            """A static method"""
            ...
    self.assertEqual(self._get_summary_lines(X.__dict__['sm']), 'sm(x, y)\n    A static method\n')
    self.assertEqual(self._get_summary_lines(X.sm), 'sm(x, y)\n    A static method\n')
    self.assertIn('\n |  Static methods defined here:\n |  \n |  sm(x, y)\n |      A static method\n', pydoc.plain(pydoc.render_doc(X)))
