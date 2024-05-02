from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.check_boxes = [self.cb1, self.cb2, self.cb3, self.cb4, self.cb5, self.cb6]
    # Any code you write here will run before the form opens.

  def store_data(current_country, languages, citizenship):
      a = 1
      current_country = 1
      languages = 2
      citizenship

  def button_1_click(self, **event_args):
    # Selected value from drop down is stored in current country field
    current_country = self.current_drpdwn.selected_value
    
    # Get the list of all langauges spoken
    for cb in self.check_boxes:
      if cb.checked == True:
        languages = languages + cb.text
    
    # Next vacation plan motivation
    vacation = self.rb1.get_group_value()

    if current_country and languages and vacation :
      # Stores the vanlue enterd in db.
      pass
    otherwise



    

    