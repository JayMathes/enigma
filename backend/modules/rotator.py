from random import randint

class Rotator:
    def __init__(self, rotation_speed:int=1):
        self.chars: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rotation_speed: int = rotation_speed

    def rotate(self, rotations:int=None) -> None:
        if rotations is None:
            rotations = self.rotation_speed

        self.chars = self.chars[(rotations%len(self.chars)):] + self.chars[0:rotations%len(self.chars)]

    def get_char(self) -> str:
        char: str = self.chars[0]
        self.rotate()
        return char