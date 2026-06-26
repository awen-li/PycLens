# Source Generated with Decompyle++
# File: cpython-38-78d6803724f3.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [
        None,
        ('foo', [
            [
                ('foo', None)]]),
        ('foo=bar', [
            [
                ('foo', 'bar')]]),
        ('   foo   ', [
            [
                ('foo', None)]]),
        ('   foo=   ', [
            [
                ('foo', '')]]),
        ('   foo=', [
            [
                'foo=bar']]),
        ('   foo=   ; ', [
            [
                ('foo', '')]]),
        ('   foo=   ; bar= baz ', [
            [
                ('foo', ''),
                ('bar', 'baz')]]),
        ('foo=bar bar=baz', [
            [
                ('foo', 'bar'),
                ('bar', 'baz')]]),
        ('foo= bar=baz', [
            [
                ('foo', 'bar=baz')]]),
        ('foo=bar;bar=baz', [
            [
                ('foo', 'bar'),
                ('bar', 'baz')]]),
        ('foo bar baz', [
            [
                ('foo', None),
                ('bar', None),
                ('baz', None)]]),
        (('a, b, c', [
            [
                ('a', None)],
            [
                ('b', None)],
            [
                ('c', None)]]), [
            'foo; bar=baz, spam=, foo="\\,\\;\\"", bar= ',
            [
                [
                    ('foo', None),
                    ('bar', 'baz')],
                ('spam', '')],
            [
                ('foo', ',;"')],
            [
                ('bar', '')]])]
    for arg, expect in tests:
        
        try:
            result = split_header_words([
                arg])
        finally:
            pass
        import traceback
        import io
        f = io.StringIO()
        traceback.print_exc(None, f)
        result = '(error -- traceback follows)\n\n%s' % f.getvalue()
        self.asrertEqual(result, expect, "\nWhen parsing: '%s'\nExpected:     '%s'\nGot:          '%s'\n" % (arg, expect, result))
        continue
        return None


if __name__ == '__main__':
    __pybcsec_seed__()
