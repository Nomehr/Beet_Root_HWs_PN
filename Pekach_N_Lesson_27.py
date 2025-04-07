# Lesson 27
## Prog. Minimum

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def insert_tree(self, new_tree):
        self.children.append(new_tree)

    def remove_subtree(self, value):
        self.children = [child for child in self.children if child.value != value]
        for child in self.children:
            child.remove_subtree(value)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

# Пример использования
root = TreeNode('A')
child_b = TreeNode('B')
child_c = TreeNode('C')
child_d = TreeNode('D')
child_e = TreeNode('E')

root.add_child(child_b)
root.add_child(child_c)
child_b.add_child(child_d)
child_b.add_child(child_e)

print("Исходное дерево:")
print(root)

# Вставка нового дерева
new_tree = TreeNode('F')
new_tree.add_child(TreeNode('G'))
root.insert_tree(new_tree)

print("Дерево после вставки:")
print(root)

# Удаление поддерева
root.remove_subtree('B')
print("Дерево после удаления поддерева 'B':")
print(root)

## Prog. Maximum

from bs4 import BeautifulSoup

class DOMNode:
    def __init__(self, tag, text=None):
        self.tag = tag
        self.text = text
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_text_by_tag(self, tag):
        if self.tag == tag:
            return self.text
        for child in self.children:
            result = child.find_text_by_tag(tag)
            if result:
                return result
        return None

    def __repr__(self, level=0):
        ret = "\t" * level + f"Tag: {self.tag}, Text: {self.text}\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

def parse_html_to_dom(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    root = DOMNode(soup.find().name)
    build_dom_tree(soup.find(), root)
    return root

def build_dom_tree(soup_tag, dom_node):
    for child in soup_tag.children:
        if child.name:
            new_node = DOMNode(child.name, child.get_text(strip=True))
            dom_node.add_child(new_node)
            build_dom_tree(child, new_node)

# Пример использования
html_content = """
<html>
    <body>
        <h1>Заголовок</h1>
        <p>Параграф 1</p>
        <p>Параграф 2</p>
        <div>
            <p>Параграф 3</p>
        </div>
    </body>
</html>
"""

dom_tree = parse_html_to_dom(html_content)
print("DOM дерево:")
print(dom_tree)

# Поиск текста по тегу
tag_to_find = 'p'
found_text = dom_tree.find_text_by_tag(tag_to_find)
print(f"Текст по тегу '{tag_to_find}': {found_text}")