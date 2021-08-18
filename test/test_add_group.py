import pytest


def test_add_group(app):
    with pytest.allure.step("Given a group list"):
        old_list = app.groups.get_group_list()
    with pytest.allure.step("When I add the group to the list"):
        app.groups.add_new_group("my group")
    with pytest.allure.step("Then the new group list is equal to the old list with the added group"):
        new_list = app.groups.get_group_list()
        old_list.append("my group")
        print(old_list)
        assert sorted(old_list) == sorted(new_list)