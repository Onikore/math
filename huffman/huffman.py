from collections import Counter


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def huffman_code_tree(node, bin_string=''):
    if type(node) is str:
        return {node: bin_string}
    l, r = node.children()
    d = dict()
    d.update(huffman_code_tree(l, bin_string + '0'))
    d.update(huffman_code_tree(r, bin_string + '1'))
    return d


def make_tree(items):
    while len(items) > 1:
        char1, freq1 = items.pop()
        char2, freq2 = items.pop()
        node = Node(char1, char2)
        items.append((node, freq1 + freq2))
        items = sorted(items, key=lambda x: x[1], reverse=True)
        # print(items)
    return items[0][0]


if __name__ == '__main__':
    input_str = 'Первую версию предствать не позже указанного срока затем можно исправлять и досдавать'.lower()
    print(f'Исходный текст       - {input_str}')

    frequency = dict(Counter(input_str))
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    print(f'Частоты              - {frequency}')

    tree = make_tree(frequency)
    encoded_tree = huffman_code_tree(tree)
    encoded_text = ''.join(encoded_tree[i] for i in input_str)
    print(f"Закодированный текст - {encoded_text}")

    sorted_codes = sorted(encoded_tree.items(), key=lambda x: len(x[1]))
    for i in sorted_codes:
        print(f'{i[0]} - {i[1]}')

    decoded_text = ''
    char = ''
    for i in encoded_text:
        char += i
        for key, val in encoded_tree.items():
            if val == char:
                decoded_text += key
                char = ''
    print(decoded_text)
