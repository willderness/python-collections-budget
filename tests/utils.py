import ast
import inspect
import json
import os
import collections


def load_ast_tree(filename):
    try:
        with open(filename) as f:
            fstr = f.read()
            return ast.parse(fstr, filename=filename)
    except:
        return ast.parse("()")

def convert_ast(node, return_type='string', include_type=False, sep=':'):
    count = 1
    def _flatten_dict(d, parent_key='', sep=':'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(_flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def _flatten_list(lst):
        return sum(([x] if not isinstance(x, list) else _flatten_list(x) for x in lst), [])

    def _format(node):
        nonlocal count
        if isinstance(node, ast.AST):
            d = _flatten_dict({ key: _format(value) for key, value in ast.iter_fields(node) if key != 'ctx' and key != 'type_comment' and key != 'kind'})

            if include_type:
                d['type'] = node.__class__.__name__

            return d

        elif isinstance(node, list):
            return sep.join(_flatten_list([value for list_node in node for value in _format(list_node).values() if value]))

        return str(node)

    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)

    if return_type == 'string':
        return sep.join([value for value in _format(node).values() if value])
    elif return_type == 'list':
        return list(_format(node).values())
    else:
        return _format(node)

def get_calls(source, return_type='string', include_type=False):
    calls = []

    def visit_Call(node):
        calls.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    try:
        node_iter.visit(ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return calls

def get_assignments(source, return_type='string', include_type=False):
    assignments = []

    def visit_Assign(node):
        assignments.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Assign = visit_Assign
    
    try:
        node_iter.visit(ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return assignments

def get_calls_from_child(child_node, return_type='string', include_type=False):
    calls = []

    def visit_Call(node):
        calls.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    try:
        node_iter.visit(child_node) #ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return calls

def get_returns_from_child(child_node, return_type='string', include_type=False):
    returns = []

    def visit_Return(node):
        returns.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Return = visit_Return
    try:
        node_iter.visit(child_node) #ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return returns

def get_classes(source, return_type='string', include_type=False):
    classes = []

    def visit_ClassDef(node):
        classes.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_ClassDef = visit_ClassDef
    
    try:
        node_iter.visit(ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return classes

def get_assignments_from_child(child_node, return_type='string', include_type=False):
    assignments = []

    def visit_Assign(node):
        assignments.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Assign = visit_Assign
    
    try:
        node_iter.visit(child_node) #ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return assignments

def get_augassignments_from_child(child_node, return_type='string', include_type=False):
    assignments = []

    def visit_AugAssign(node):
        assignments.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_AugAssign = visit_AugAssign
    
    try:
        node_iter.visit(child_node) #ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return assignments

def get_if_statements_from_child(child_node, return_type='string', include_type=False):
    ifs = []

    def visit_If(node):
        ifs.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_If = visit_If
    try:
        node_iter.visit(child_node) #ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return ifs

def get_functions(source, return_type='string', include_type=False):
    functions = []

    def visit_FunctionDef(node):
        functions.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_FunctionDef = visit_FunctionDef
    
    try:
        node_iter.visit(ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return functions

def get_if_statements(source, return_type='string', include_type=False):
    ifs = []

    def visit_If(node):
        ifs.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_If = visit_If
    try:
        node_iter.visit(ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return ifs

def get_for_loops(source, return_type='string', include_type=False):
    loops = []

    def visit_For(node):
        loops.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_For = visit_For
    try:
        node_iter.visit(ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return loops

def get_for_loops_from_child(child_node, return_type='string', include_type=False):
    loops = []

    def visit_For(node):
        loops.append(convert_ast(node, return_type, include_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_For = visit_For
    try:
        node_iter.visit(child_node) #ast.parse(inspect.getsource(source)))
    except OSError:
        return []

    return loops