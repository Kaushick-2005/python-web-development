import wx
class Calculator(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Simple Calculator')
        self.panel = wx.Panel(self)
        self.display = wx.TextCtrl(self.panel, style=wx.TE_RIGHT, size=(250, 50))
        
        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Layout for buttons
        grid_sizer = wx.GridSizer(4, 4, 5, 5)

        for label in buttons:
            button = wx.Button(self.panel, label=label)
            grid_sizer.Add(button, 0, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.display, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 10)
        self.panel.SetSizer(vbox)

        self.SetSize((300, 400))
        self.Show()

        self.current_input = ''
        self.result = None

    def on_button_click(self, event):
        label = event.GetEventObject().GetLabel()
        
        if label == '=':
            self.calculate()
        else:
            self.current_input += label
            self.display.SetValue(self.current_input)

    def calculate(self):
        try:
            # Evaluate the expression
            self.result = eval(self.current_input)
            self.display.SetValue(str(self.result))
            self.current_input = str(self.result)
        except Exception as e:
            self.display.SetValue("Error")
            self.current_input = ''

if __name__ == '__main__':
    app = wx.App(False)
    calculator = Calculator()
    app.MainLoop()
