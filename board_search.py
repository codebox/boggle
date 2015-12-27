def board_search(board, word_trie):
    results = set()

    def _search(pos, prefix_node, visited_positions):
        if prefix_node.is_word:
            results.add(prefix_node.value)

        for neighbour_position in board.get_neighbours(pos[0], pos[1]):
            if neighbour_position not in visited_positions:
                letter = board.get_letter(neighbour_position[0], neighbour_position[1])
                child_node = prefix_node.get_child(letter)

                if child_node:
                    if letter == 'Q':
                        child_node = child_node.get_child('U')
                        if not child_node:
                            return

                    _search(neighbour_position, child_node, visited_positions + [neighbour_position])

    for c in range(0, board.size):
        for r in range(0, board.size):
            _search((c, r), word_trie.root, [])

    return results