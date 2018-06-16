from openpyxl import load_workbook
from dustbin import *

def load_data(file_name):
    wb = load_workbook(file_name)
    print(wb.get_sheet_names())
    ws = wb.get_sheet_by_name('address')
    print(ws)

    for row in range(2, 31):
        code = ws.cell(row=row, column=1).value
        address = ws.cell(row=row, column=3).value
        print(code, ' | ', address)

        # node = Node(code=code, address=address)

        RouteManager.addDustbin(Dustbin(address))

        # nodes.append(node)

        # visualizer = Visualizer()
        # visualizer.draw_node(node)

    # visualizer.show()