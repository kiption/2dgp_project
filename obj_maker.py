import game_world
import enum

from ground import Ground
from box import BoxQuestion, Brick, Pipe, BluePipe, Flag
from item import Coin, Transform

class ObjType(enum.IntEnum):
    o_ground = 0
    o_box_q = enum.auto()
    o_brick = enum.auto()
    o_pipe = enum.auto()
    o_pipe_b = enum.auto()
    o_item_c = enum.auto()
    o_item_t = enum.auto()
    o_flag = enum.auto()


def make_obj(x, y, obj_type, value):
    if obj_type == ObjType.o_ground:
        new_obj = Ground()
        new_obj.value = value
    elif obj_type == ObjType.o_box_q:
        new_obj = BoxQuestion()
        new_obj.value = value
    elif obj_type == ObjType.o_brick:
        new_obj = Brick()
        new_obj.value = value
    elif obj_type == ObjType.o_pipe:
        new_obj = Pipe()
        new_obj.value = value
    elif obj_type == ObjType.o_pipe_b:
        new_obj = BluePipe()
        new_obj.value = value
    elif obj_type == ObjType.o_item_c:
        new_obj = Coin()
        new_obj.value = value
    elif obj_type == ObjType.o_item_t:
        new_obj = Transform()
        new_obj.value = value
    elif obj_type == ObjType.o_flag:
        new_obj = Flag()
        new_obj.value = None

    new_obj.x, new_obj.y = x, y

    game_world.add_object(new_obj, 0)