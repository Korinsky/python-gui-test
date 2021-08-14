import random

def test_delete_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 1:
        app.groups.add_new_group("my group")
        old_list = app.groups.get_group_list()
    index = old_list.index(random.choice(old_list))
    app.groups.delete_group_by_index(index)
    new_list = app.groups.get_group_list()
    old_list.remove(old_list[index])
    assert sorted(old_list) == sorted(new_list)