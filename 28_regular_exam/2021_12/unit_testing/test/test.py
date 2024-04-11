from unittest import TestCase, main

from project.team import Team

if __name__ == "__main__":
    main()


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team = Team("test")

    def test_init(self):
        self.assertEqual(self.team.name, "test")
        self.assertEqual(self.team.members, {})

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "test1,.#$"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_only_new_players(self):
        self.assertEqual(self.team.members, {})
        result = self.team.add_member(**{"Pesho": 20})
        self.assertEqual(self.team.members, {"Pesho": 20})
        self.assertEqual(result, "Successfully added: Pesho")
        result = self.team.add_member(**{"Pesho": 20, "Gosho": 25, "Pesha": 30})
        self.team.add_member(**{"Pesho": 20, "Gosho": 25, "Pesha": 30})
        self.assertEqual(self.team.members, {"Pesho": 20, "Gosho": 25, "Pesha": 30})
        self.assertEqual(20, self.team.members["Pesho"])
        self.assertEqual(25, self.team.members["Gosho"])
        self.assertEqual(30, self.team.members["Pesha"])
        self.assertEqual(result, "Successfully added: Gosho, Pesha")

    def test_remove_member_but_does_not_exist(self):
        self.team.add_member(**{"Pesho": 20})
        result = self.team.remove_member("Gosho")
        self.assertEqual(self.team.members, {"Pesho": 20})
        self.assertEqual(result, "Member with name Gosho does not exist")
        self.assertEqual(len(self.team.members), 1)

    def test_remove_member_valid(self):
        self.team.add_member(**{"Pesho": 20, "Gosho": 25})
        result = self.team.remove_member("Pesho")
        self.assertEqual(self.team.members, {"Gosho": 25})
        self.assertEqual(result, "Member Pesho removed")
        self.assertEqual(len(self.team.members), 1)

    def test_greater_than_if_other_is(self):
        self.team.add_member(**{"Pesho": 20})
        other_team = Team("other")
        other_team.add_member(**{"Pesha": 20, "Gosho": 25})
        self.assertEqual(False, self.team > other_team)
        self.assertEqual(True, other_team > self.team)

    def test_greater_than_if_self_is(self):
        self.team.add_member(**{"Pesho": 20, "Gosho": 25, "Ivan": 20})
        other_team = Team("other")
        other_team.add_member(**{"Pesha": 20, "Gosha": 25})
        self.assertEqual(True, self.team > other_team)
        self.assertEqual(False, other_team > self.team)

    def test_len(self):
        self.team.add_member(**{"Pesho": 20, "Gosho": 25})
        self.assertEqual(len(self.team), 2)
        # self.assertEqual(len(self.team.members), 2)

    def test_add(self):
        self.team.add_member(**{"Pesho": 20, "Gosho": 25})
        other_team = Team("other")
        other_team.add_member(**{"Pesha": 20, "Gosha": 25})
        self.team = self.team.__add__(other_team)
        self.assertEqual(len(self.team), 4)
        self.assertEqual(self.team.members, {"Pesho": 20, "Gosho": 25, "Pesha": 20, "Gosha": 25})
        self.assertEqual(self.team.name, "testother")
        # self.assertEqual(len(self.team.members), 4)

    def test_str(self):
        self.team.add_member(**{"Pesho": 20, "Gosho": 25, "Pesha": 20})
        result = str(self.team)
        self.assertEqual(result, "Team name: test\nMember: Gosho - 25-years old\nMember: Pesha - 20-years old\nMember: Pesho - 20-years old")
