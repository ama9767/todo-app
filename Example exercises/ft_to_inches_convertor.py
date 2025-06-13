import FreeSimpleGUI as sg
from ft_inch_function import convert

sg.theme("Topanga")

label_ft = sg.Text("Enter feet:")
input_ft = sg.Input(key="feet")

label_inch = sg.Text("Enter inches:")
input_inch = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_result = sg.Text("", key="output")

window = sg.Window("Convert in to m",
                   layout= [[label_ft, input_ft],
                            [label_inch, input_inch],
                            [convert_button, exit_button, output_result]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m")


window.close()