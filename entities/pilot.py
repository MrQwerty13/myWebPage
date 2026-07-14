from typing import Any


class Pilot:
    def __init__(self, name: str, surname: str, current_number: int, points: float, team: str):
        self.name = name
        self.surname = surname
        self.current_number = current_number
        self.points = points
        self.team = team

    def change_current_number(self, new_number: int):
        self.current_number = new_number

    def change_points(self, new_points: float):
        self.points = new_points

    def change_team(self, new_team: str):
        self.team = new_team