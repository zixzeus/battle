from typing import List
from agent.agent import Agent
from  env.env_cmd import CmdEnv
import collections


def no_ops(cmd_list):
    pass


def init_pos(cmd_list):
    pass


cmds=[
    CmdEnv.make_entityinitinfo,
    CmdEnv.make_linepatrolparam,
    CmdEnv.make_areapatrolparam,
    CmdEnv.make_motioncmdparam,
    CmdEnv.make_followparam,
    CmdEnv.make_attackparam
]


class Arg(collections.namedtuple('Arg',['name','type','range','values'])):
    def __str__(self):
        return "%s/%s %s" % (self.name, self.type, self.range,self.values)

    @classmethod
    def coordinate(cls,name,type,range):
        return cls(name,type,range,None)

    @classmethod
    def ally_id(cls,name,type,values):
        return cls(name,type,values)

    @classmethod
    def enemy_id(cls,name,type,values):
        return cls(name,type,)



class Arguments(collections.namedtuple('Arguments', ['id', 'name', 'id'])):
    def __init__(self):
        pass


class Actions():
    def __init__(self):
        pass


def FunctionCall(cmd_list,function_id, *args):
    func=cmds[function_id]
    cmd_list.append(func(*args))