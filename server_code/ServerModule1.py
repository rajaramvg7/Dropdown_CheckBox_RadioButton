import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def store_data(current_country, languages, vacation):
  app_tables.plan.add_row(languages =  languages,
                         residence_country = current_country
                         vacation_plan = vacation)
