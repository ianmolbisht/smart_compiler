from copy import deepcopy


def clone_ast(ast_root):
    return deepcopy(ast_root)