from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def store_data(current_country, languages, citizenship):
      a = 1
      current_country = 1
      languages = 2
      citizenship

  def button_1_click(self, **event_args):
    # Selected value from drop down is stored in current country field
    current_country = self.current_drpdwn.selected_value
    
    """This method is called when the button is clicked"""
    pass
    

    