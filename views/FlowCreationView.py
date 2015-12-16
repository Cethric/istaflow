# coding: utf-8
import ui
dbo = None
class FlowCreationView(object):
	def __init__(self, elements, saveCallBack):
		self.elements = elements
		self.saveCallBack = saveCallBack

	def tableview_did_select(self, tableview, section, row):
		pass
		
	def tableview_title_for_header(self, tableview, section):
		pass

	def tableview_number_of_sections(self, tableview):
		return 1

	def tableview_number_of_rows(self, tableview, section):
		return len(self.elements)
		
	def tableview_cell_for_row(self, tableview, section, row):
		cell = ui.TableViewCell('subtitle')
		cell.text_label.text = self.elements[row].get_title()
		cell.detail_text_label.text = self.elements[row].get_description()
		cell.image_view.image = ui.Image.named(self.elements[row].get_icon())
		cell.selectable = True
		return cell

def get_view(elements, cb):
	dbo = FlowCreationView(elements = elements, saveCallBack = cb)
	table_view = ui.TableView()
	table_view.name = 'Flow'
	table_view.data_source = dbo
	table_view.delegate = dbo
	return table_view
	