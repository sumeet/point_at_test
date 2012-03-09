#!/usr/bin/env python
import ast
import operator
import sys


def point_at_test(source, lineno):
    """Return the name of the test being pointed to in the source code.

    If pointing at a class name, returns ClassName. When pointing at a method
    name, returns ClassName.method_name. When pointing at anything else,
    returns the empty string.
    """
    clsdefs = []

    tree = ast.parse(source)

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            clsdefs.append(node)
        if not (hasattr(node, 'lineno') and node.lineno == lineno):
            continue
        if isinstance(node, ast.ClassDef):
            return node.name
        elif isinstance(node, ast.FunctionDef):
            earlier_clsdefs = (cd for cd in clsdefs if cd.lineno < node.lineno)
            previous_clsdef = max(earlier_clsdefs,
                                  key=operator.attrgetter('lineno'))
            return previous_clsdef.name + '.' + node.name

    return ''


if __name__ == '__main__':
    args = ' '.join(sys.argv[1:]).split()

    source = open(args[0]).read()
    lineno = int(args[1])

    test_name = point_at_test(source, lineno)
    print test_name if test_name else ''
