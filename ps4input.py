#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Playstation 4 Controller
# in Python. Simply plug your PS4 controller into your computer using USB and run this
# script!
#
# NOTE: I assume in this script that the only joystick plugged in is the PS4 controller.
#       if this is not the case, you will need to change the class accordingly.
#
# Copyright © 2015 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.

import os
import pprint
import pygame
import threading


class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""


    def __init__(self):

        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()


        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def _monitor_controller(self):
        """Listen for events to happen"""
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        while True:
            for event in pygame.event.get():
                if(event.type == pygame.JOYAXISMOTION):
                    self.LeftJoystickX = joystick.get_axis(0)
                    self.LeftJoystickY = joystick.get_axis(1)
                if(event.type == pygame.JOYBUTTONDOWN):
                    self.X = joystick.get_button(0)
                    self.A = joystick.get_button(1)
                    self.RightBumper = joystick.get_button(5)



    def read(self):
        xAxis = self.LeftJoystickX
        yAxis = self.LeftJoystickY
        x = self.A
        square = self.X
        r1 = self.RightBumper
        return [xAxis, yAxis, x, square, r1]


if __name__ == "__main__":
    ps4 = PS4Controller()
