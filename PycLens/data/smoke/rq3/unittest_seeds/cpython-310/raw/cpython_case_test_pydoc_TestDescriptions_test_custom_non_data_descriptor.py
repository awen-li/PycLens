# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_custom_non_data_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descr:

        def __get__(self, obj, cls):
            if obj is None:
                return self
            return 42

    class X:
        attr = Descr()
    self.assertEqual(self._get_summary_lines(X.attr), '<test.test_pydoc.TestDescriptions.test_custom_non_data_descriptor.<locals>.Descr object>')
    X.attr.__doc__ = 'Custom descriptor'
    self.assertEqual(self._get_summary_lines(X.attr), '<test.test_pydoc.TestDescriptions.test_custom_non_data_descriptor.<locals>.Descr object>\n    Custom descriptor\n')
    X.attr.__name__ = 'foo'
    self.assertEqual(self._get_summary_lines(X.attr), 'foo(...)\n    Custom descriptor\n')
