# provider.py

from program import Program

class Provider(object):
  def __init__(self, name, **kwargs):
    self.name = name
    self.address = kwargs.get("address", "")
    self.logo = kwargs.get("logo", "")
    self.programs = {}

  def add_program(self, program_name, **kwargs):
    if not program_name:
      raise "A program name must be given"

    program = Program(program_name, **kwargs)

    self.programs[program_name] = program

    return program

  def list_programs(self):
    for program in self.programs:
      print self.programs[program]
