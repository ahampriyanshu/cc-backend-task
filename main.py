list_1 = [
    {
        "id": "1",
        "name": "Shrey",
        "age": 25
    },
    {
        "id": "3",
        "age": 10,
        "name": "Hello"
    },
    {
        "id": "2",
        "name": "World",
        "age": 24
    },
]

list_2 = [
    {
        "id": "1",
        "marks": 100
    },
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """

      Args:
          list_1 [list], list_2 [list]

      Returns:
        [list]: List of merged dictionaries (no duplicates of instance 'id' ).

    """
    merged_list = {}
    for object in [*list_1, *list_2]:
        if object['id'] not in merged_list:
            merged_list[object['id']] = object
        else:
            merged_list[object['id']].update(object)

    return list(merged_list.values())


list_3 = merge_lists(list_1, list_2)
