#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position= (0,0)):
        match entity_name:
            case 'nature_1':
                list_bg = []
                for i in range(9):
                    list_bg.append(Background(f'nature_1_{i}', (0,0))) #FETCH FOR THE IMAGES WHICH NAME STARTS WITH NATURE_1
                return list_bg
#            case 'nature_2':
#
#            case 'nature_3':
#
 #           case 'nature_4':
#
 #           case 'nature_5':
#
 #           case 'nature_6':
#
 #           case 'nature_7':
#
 #           case 'nature_8':
#
#            case 'players':
