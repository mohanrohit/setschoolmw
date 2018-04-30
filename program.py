# program.py

import datetime

class Program(object):
  def __init__(self, name, **kwargs):
    self.name = name
    self.start_date = kwargs.get("start_date", datetime.date.today())
    self.end_date = kwargs.get("end_date", datetime.date.today())

  def __repr__(self):
    #return "%s: %s-%s" % (self.name, self.start_date, self.end_date)
    return "{name}: {start}-{end}".format(name=self.name, start=self.start_date, end=self.end_date)
