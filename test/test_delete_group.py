import random
import pytest


def test_delete_group(app):
    with pytest.allure.step("Given a group list"):
        old_list = app.groups.get_group_list()
        if len(old_list) == 1:
            app.groups.add_new_group("my group")
            old_list = app.groups.get_group_list()
    with pytest.allure.step("When I deleted the group to the list"):
        index = old_list.index(random.choice(old_list))
        app.groups.delete_group_by_index(index)
    with pytest.allure.step("Then the new group list is equal to the old list without deleted group"):
        new_list = app.groups.get_group_list()
        old_list.remove(old_list[index])
        assert sorted(old_list) == sorted(new_list)