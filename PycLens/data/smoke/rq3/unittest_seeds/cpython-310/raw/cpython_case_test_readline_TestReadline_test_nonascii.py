# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_readline.py
# case: TestReadline_test_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    loc = locale.setlocale(locale.LC_CTYPE, None)
    if loc in ('C', 'POSIX'):
        self.skipTest(f'the LC_CTYPE locale is {loc!r}')
    try:
        readline.add_history('ëï')
    except UnicodeEncodeError as err:
        self.skipTest('Locale cannot encode test data: ' + format(err))
    script = 'import readline\n\nis_editline = readline.__doc__ and "libedit" in readline.__doc__\ninserted = "[\\xEFnserted]"\nmacro = "|t\\xEB[after]"\nset_pre_input_hook = getattr(readline, "set_pre_input_hook", None)\nif is_editline or not set_pre_input_hook:\n    # The insert_line() call via pre_input_hook() does nothing with Editline,\n    # so include the extra text that would have been inserted here\n    macro = inserted + macro\n\nif is_editline:\n    readline.parse_and_bind(r\'bind ^B ed-prev-char\')\n    readline.parse_and_bind(r\'bind "\\t" rl_complete\')\n    readline.parse_and_bind(r\'bind -s ^A "{}"\'.format(macro))\nelse:\n    readline.parse_and_bind(r\'Control-b: backward-char\')\n    readline.parse_and_bind(r\'"\\t": complete\')\n    readline.parse_and_bind(r\'set disable-completion off\')\n    readline.parse_and_bind(r\'set show-all-if-ambiguous off\')\n    readline.parse_and_bind(r\'set show-all-if-unmodified off\')\n    readline.parse_and_bind(r\'Control-a: "{}"\'.format(macro))\n\ndef pre_input_hook():\n    readline.insert_text(inserted)\n    readline.redisplay()\nif set_pre_input_hook:\n    set_pre_input_hook(pre_input_hook)\n\ndef completer(text, state):\n    if text == "t\\xEB":\n        if state == 0:\n            print("text", ascii(text))\n            print("line", ascii(readline.get_line_buffer()))\n            print("indexes", readline.get_begidx(), readline.get_endidx())\n            return "t\\xEBnt"\n        if state == 1:\n            return "t\\xEBxt"\n    if text == "t\\xEBx" and state == 0:\n        return "t\\xEBxt"\n    return None\nreadline.set_completer(completer)\n\ndef display(substitution, matches, longest_match_length):\n    print("substitution", ascii(substitution))\n    print("matches", ascii(matches))\nreadline.set_completion_display_matches_hook(display)\n\nprint("result", ascii(input()))\nprint("history", ascii(readline.get_history_item(1)))\n'
    input = b'\x01'
    input += b'\x02' * len('[after]')
    input += b'\t\t'
    input += b'x\t'
    input += b'\r'
    output = run_pty(script, input)
    self.assertIn(b"text 't\\xeb'\r\n", output)
    self.assertIn(b"line '[\\xefnserted]|t\\xeb[after]'\r\n", output)
    if sys.platform == 'darwin' or not is_editline:
        self.assertIn(b'indexes 11 13\r\n', output)
    if not is_editline and hasattr(readline, 'set_pre_input_hook'):
        self.assertIn(b"substitution 't\\xeb'\r\n", output)
        self.assertIn(b"matches ['t\\xebnt', 't\\xebxt']\r\n", output)
    expected = b"'[\\xefnserted]|t\\xebxt[after]'"
    self.assertIn(b'result ' + expected + b'\r\n', output)
    self.assertIn(b'history ' + expected, output)
