from optimizer.transforms import clone_ast


class Optimizer:
    def __init__(self):
        self.optimizations = []

    def optimize(self, ast_root):
        cloned = clone_ast(ast_root)
        optimized = self.visit(cloned)
        return optimized

    def visit(self, node):
        if node is None:
            return None

        method_name = f"visit_{node.type}"
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        if hasattr(node, 'children'):
            for i in range(len(node.children)):
                node.children[i] = self.visit(node.children[i])

        return node
    def visit_BinaryOp(self, node):
        node.children[0] = self.visit(node.children[0])
        node.children[1] = self.visit(node.children[1])

        left = node.children[0]
        right = node.children[1]

        # CONSTANT FOLDING
        if left.type == "Number" and right.type == "Number":
            result = None

            if node.value == "+":
                result = left.value + right.value
            elif node.value == "-":
                result = left.value - right.value

            elif node.value == "*":
                result = left.value * right.value

            elif node.value == "/":
                if right.value != 0:
                    result = left.value / right.value

            if result is not None:
                self.optimizations.append({
                    "type": "Constant Folding",
                    "before": f"{left.value} {node.value} {right.value}",
                    "after": str(result)
                })

                return NumberNode(result)
        if node.value == "+":
            if right.type == "Number" and right.value == 0:
                self.optimizations.append({
                    "type": "Algebraic Simplification",
                    "before": "x + 0",
                    "after": "x"
                })
                return left

            if left.type == "Number" and left.value == 0:
                self.optimizations.append({
                    "type": "Algebraic Simplification",
                    "before": "0 + x",
                    "after": "x"
                })
                return right

        if node.value == "*":
            if right.type == "Number" and right.value == 1:
                self.optimizations.append({
                    "type": "Algebraic Simplification",
                    "before": "x * 1",
                    "after": "x"
                })
                return left
            if left.type == "Number" and left.value == 1:
                self.optimizations.append({
                    "type": "Algebraic Simplification",
                    "before": "1 * x",
                    "after": "x"
                })
                return right

        return node

    # -----------------------------------------
    # DEAD CODE ELIMINATION
    # -----------------------------------------

    def visit_Block(self, node):
        optimized_children = []
        found_return = False

        for child in node.children:
            if found_return:
                self.optimizations.append({
                    "type": "Dead Code Elimination",
                    "before": getattr(child, 'type', 'Unknown'),
                    "after": "Removed"
                })
                continue
            optimized_child = self.visit(child)
            optimized_children.append(optimized_child)

            if optimized_child.type == "Return":
                found_return = True

        node.children = optimized_children
        return node


# ---------------------------------------------------
# BASIC NODE CLASSES
# ---------------------------------------------------

class ASTNode:
    def __init__(self, type_, value=None, children=None):
        self.type = type_
        self.value = value
        self.children = children or []


class NumberNode(ASTNode):
    def __init__(self, value):
        super().__init__("Number", value, [])