from django.db import models
from hero.models import Hero

class Item(models.Model):
    HEAD = 1
    TORSO = 2
    FEET = 3
    HANDS = 4
    SHOULDERS = 5
    LEGS = 6
    BRACERS = 7
    MAIN_HAND = 8
    OFF_HAND = 9
    WAIST = 10
    RIGHT_FINGER = 11
    LEFT_FINGER = 12
    NECK = 13

    SLOTS = (
        (HEAD, 'Head'),
        (TORSO, 'Torso'),
        (FEET, 'Feet'),
        (HANDS, 'Hands'),
        (SHOULDERS, 'Shoulders'),
        (LEGS, 'Legs'),
        (BRACERS, 'Bracers'),
        (MAIN_HAND, 'Main Hand'),
        (OFF_HAND, 'Off Hand'),
        (WAIST, 'Waist'),
        (RIGHT_FINGER, 'Right Finger'),
        (LEFT_FINGER, 'Left Finger'),
        (NECK, 'Neck'),
    )

    GRAY = 1
    WHITE = 2
    BLUE = 3
    YELLOW = 4
    ORANGE = 5
    GREEN = 6

    COLORS = (
        (GRAY, 'Gray'),
        (WHITE, 'White'),
        (BLUE, 'Blue'),
        (YELLOW, 'Yellow'),
        (ORANGE, 'Orange'),
        (GREEN, 'Green'),
    )


    hero = models.ForeignKey(Hero)

    slot = models.SmallIntegerField(choices=SLOTS)
    name = models.CharField(max_length=100)
    item_level = models.SmallIntegerField()
    icon = models.CharField(max_length=100)
    color = models.SmallIntegerField(choices=COLORS)
    tooltip = models.CharField(max_length=200)
