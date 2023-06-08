def merge_sort(list, start=0, end=None):
    if end is None:
        end = len(list)

    if (end - start) > 1:
        mid = (start + end) // 2

        # dividindo as listas
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)

        # unindo as listas
        merge(list, start, mid, end)


def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]

    left_index, right_index = 0, 0

    # percorrer sobre a lista inteira como se fosse uma
    for general_index in range(start, end):
        # se os elementos da esquerda acabaram, preenche o restante com
        # a lista da direita
        if left_index >= len(left):
            list[general_index] = right[right_index]
            right_index = right_index + 1

        # se os elementos da direita acabaram, preenche o restante com
        # a lista da esquerda
        elif right_index >= len(right):
            list[general_index] = left[left_index]
            left_index = left_index + 1

        # se o elemento do topo da esquerda for menor que o da direita,
        # ele será o escolhido
        elif left[left_index] < right[right_index]:
            list[general_index] = left[left_index]
            left_index = left_index + 1

        else:
            # caso o da direita seja menor, ele será o escolhido
            list[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_list, second_list = (
        list(first_string.lower()),
        list(second_string.lower()),
    )

    merge_sort(first_list, 0, len(first_list))
    merge_sort(second_list, 0, len(second_list))

    if first_list == second_list:
        return (
            "".join(first_list),
            "".join(second_list),
            True,
        )
    else:
        return (
            "".join(first_list),
            "".join(second_list),
            False,
        )
