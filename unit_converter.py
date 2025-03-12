# importing the necessary moduels
import sys #importing sys for clean exit avoiding crashes and cli based functionality
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton, QDesktopWidget) #library for gui based applications

class UnitConverter(QMainWindow): #making a class inhereted from the QMainWindow class

    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Unit Converter") #setting window title
        self.setGeometry(100, 100, 800 , 600) #setting window geometry
        self.CenterWindow() #calling center window method
        self.setFixedSize(800, 600) #making size fixed
        self.initUI() #calling the ui method

        self.units = {
            "Weight": ["Kilogram (Kg)", "Grams (g)", "Pounds (lb)","Ounces (oz)"],
            "Length": ["Kilometer (Km)", "Meter (m)", "Feet (ft)","Inch (in)", "Miles (mi)"],
            "Temperature": ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
            "Time": ["Seconds (s)", "Minutes (min)", "Hours (h)", "Days (d)"],
            "Speed": ["Meters per second (m/s)", "Kilometers per hour (km/h)", "Miles per hour (mph)"],
            "Data storage": ["Bytes (B)", "Kilobytes (KB)", "Megabytes (MB)", "Gigabytes (GB)", "Terabytes (TB)"],
            "Area": ["Square meters (m²)", "Square kilometers (km²)", "Square feet (ft²)", "Square miles (mi²)"]
        }

    def initUI(self): #method for adding ui
        label = QLabel("Input Conversion Value") #label for value
        label.setStyleSheet("background-color: rgb(58,158,153); color: white; padding-left: 20px; font-size: 30px; height: 45px;") #css stylesheet to style the label

        self.textbox = QLineEdit() #textbox to add value
        self.textbox.setFixedSize(400, 45) #setting fixed size ie width and height
        self.textbox.setStyleSheet("padding: 5px; background-color: rgb(210, 247, 241); font-size: 30px;") #stylesheet for textbox
         
        hbox = QHBoxLayout() #defining hbox as horizontal layout
        hbox.addWidget(label) #adding widget to horizontal layout
        hbox.addWidget(self.textbox) #adding widget to horizontal layout

        label_unit_type = QLabel("Input Unit Type") #label for value
        label_unit_type.setStyleSheet("background-color: rgb(58,158,153); color: white; padding-left: 20px; font-size: 30px; height: 45px;")

        self.unit_type = QComboBox()
        self.unit_type.addItems(["--Select unit type--", "Weight", "Length", "Temperature", "Time", "Speed", "Data storage", "Area"])
        self.unit_type.setStyleSheet("margin-top: 2px; padding: 5px; background-color: rgb(210, 247, 241); font-size: 30px;")
        self.unit_type.setFixedSize(400, 50)
        self.unit_type.currentTextChanged.connect(self.update_units)

        hbox_unit = QHBoxLayout()
        hbox_unit.addWidget(label_unit_type)
        hbox_unit.addWidget(self.unit_type)

        label_from_unit = QLabel("Input Current Unit") #label for value
        label_from_unit.setStyleSheet("background-color: rgb(58,158,153); color: white; padding-left: 20px; font-size: 30px; height: 45px;")

        self.from_unit = QComboBox()
        self.from_unit.setStyleSheet("margin-top: 2px; padding: 5px; background-color: rgb(210, 247, 241); font-size: 30px;")
        self.from_unit.setFixedSize(400, 50)
        self.from_unit.addItem("--Select Current Unit--")

        hbox_from_unit = QHBoxLayout()
        hbox_from_unit.addWidget(label_from_unit)
        hbox_from_unit.addWidget(self.from_unit)

        label_to_unit = QLabel("Input Result Unit") 
        label_to_unit.setStyleSheet("background-color: rgb(58,158,153); color: white; padding-left: 20px; font-size: 30px; height: 45px;")

        self.to_unit = QComboBox()
        self.to_unit.setStyleSheet("margin-top: 2px; padding: 5px; background-color: rgb(210, 247, 241); font-size: 30px;")
        self.to_unit.setFixedSize(400, 50)
        self.to_unit.addItem("--Select Result Unit--")

        hbox_to_unit = QHBoxLayout()
        hbox_to_unit.addWidget(label_to_unit)
        hbox_to_unit.addWidget(self.to_unit)

        self.convert_button = QPushButton("CONVERT")
        self.convert_button.setStyleSheet("background-color: rgb(58,158,153); color: white; font-size: 45px; height: 100px; width: 200px; border: 2px solid cyan; font-weight: bold; font-family: Times New Roman")
        self.convert_button.setFixedSize(300,65)
        self.convert_button.clicked.connect(self.convert_units)

        hbox_convert_button = QHBoxLayout()
        hbox_convert_button.addWidget(self.convert_button)

        self.label_result_box = QLabel("Result :")
        self.label_result_box.setStyleSheet("background-color: rgb(58,158,153); color: white; padding-left: 10px; font-size: 35px; height: 100px; width: 200px;")
        self.label_result_box.setFixedSize(600, 60)

        hbox_label_result = QHBoxLayout()
        hbox_label_result.addWidget(self.label_result_box)

        vbox = QVBoxLayout() #defining vbox as vertical layout
        vbox.addLayout(hbox) #adding the horiontal layout to vertical layout
        vbox.addLayout(hbox_unit)
        vbox.addLayout(hbox_from_unit)
        vbox.addLayout(hbox_to_unit)
        vbox.addLayout(hbox_convert_button)
        vbox.addLayout(hbox_label_result)

        widget = QWidget() #creates a central widget
        widget.setLayout(vbox) #adds vbox to the widget
        self.setCentralWidget(widget) #sets widget as central layout

    def update_units(self):
        selected_type = self.unit_type.currentText()

        self.from_unit.clear()
        self.to_unit.clear()

        if selected_type in self.units:
            self.from_unit.addItems(self.units[selected_type])
            self.to_unit.addItems(self.units[selected_type])

    def convert_units(self):
        input_text = self.textbox.text().strip()

        if not input_text:
            self.label_result_box.setText("PLEASE PROVIDE INPUT")
            return

        try:
            input_value = float(input_text)

        except ValueError:
            self.label_result_box.setText("PLEASE INPUT VALID NUMBER")
            return

        from_unit = self.from_unit.currentText()
        to_unit = self.to_unit.currentText()
        
        conversion_factors_weight = {
            "Kilogram (Kg)": {"Grams (g)": 1000, "Pounds (lb)": 2.20462, "Ounces (oz)": 35.274},
            "Grams (g)": {"Kilogram (Kg)": 0.001, "Pounds (lb)": 0.00220462, "Ounces (oz)": 0.035274},
            "Pounds (lb)": {"Kilogram (Kg)": 0.453592, "Grams (g)": 453.592, "Ounces (oz)": 16},
            "Ounces (oz)": {"Kilogram (Kg)": 0.0283495, "Grams (g)": 28.3495, "Pounds (lb)": 0.0625}
            }

        conversion_factors_length = {
            "Kilometer (Km)": {"Meter (m)": 1000, "Feet (ft)": 3280.84, "Inch (in)": 39370.1, "Miles (mi)": 0.621371},
            "Meter (m)": {"Kilometer (Km)": 0.001, "Feet (ft)": 3.28084, "Inch (in)": 39.3701, "Miles (mi)": 0.000621371},
            "Feet (ft)": {"Kilometer (Km)": 0.0003048, "Meter (m)": 0.3048, "Inch (in)": 12, "Miles (mi)": 0.000189394},
            "Inch (in)": {"Kilometer (Km)": 2.54e-5, "Meter (m)": 0.0254, "Feet (ft)": 0.0833333, "Miles (mi)": 1.5783e-5},
            "Miles (mi)": {"Kilometer (Km)": 1.60934, "Meter (m)": 1609.34, "Feet (ft)": 5280, "Inch (in)": 63360}
            }
        
        conversion_factors_speed = {
            "Meters per second (m/s)": {"Kilometers per hour (km/h)": 3.6, "Miles per hour (mph)": 2.23694},
            "Kilometers per hour (km/h)": {"Meters per second (m/s)": 0.277778, "Miles per hour (mph)": 0.621371},
            "Miles per hour (mph)": {"Meters per second (m/s)": 0.44704, "Kilometers per hour (km/h)": 1.60934}
            }
        
        conversion_factors_area = {
            "Square meters (m²)": {"Square kilometers (km²)": 1e-6, "Square feet (ft²)": 10.7639, "Square miles (mi²)": 3.861e-7},
            "Square kilometers (km²)": {"Square meters (m²)": 1e6, "Square feet (ft²)": 1.076e7, "Square miles (mi²)": 0.386102},
            "Square feet (ft²)": {"Square meters (m²)": 0.092903, "Square kilometers (km²)": 9.2903e-8, "Square miles (mi²)": 3.587e-8},
            "Square miles (mi²)": {"Square meters (m²)": 2.59e6, "Square kilometers (km²)": 2.58999, "Square feet (ft²)": 2.788e7}
            }
        
        conversion_factors_time = {
            "Seconds (s)": {"Minutes (min)": 1/60, "Hours (h)": 1/3600, "Days (d)": 1/86400},
            "Minutes (min)": {"Seconds (s)": 60, "Hours (h)": 1/60, "Days (d)": 1/1440},
            "Hours (h)": {"Seconds (s)": 3600, "Minutes (min)": 60, "Days (d)": 1/24},
            "Days (d)": {"Seconds (s)": 86400, "Minutes (min)": 1440, "Hours (h)": 24}
        }

        conversion_factors_data_storage = {
            "Bytes (B)": {"Kilobytes (KB)": 1/1024, "Megabytes (MB)": 1/1048576, "Gigabytes (GB)": 1/1073741824, "Terabytes (TB)": 1/1099511627776},
            "Kilobytes (KB)": {"Bytes (B)": 1024, "Megabytes (MB)": 1/1024, "Gigabytes (GB)": 1/1048576, "Terabytes (TB)": 1/1073741824},
            "Megabytes (MB)": {"Bytes (B)": 1048576, "Kilobytes (KB)": 1024, "Gigabytes (GB)": 1/1024, "Terabytes (TB)": 1/1048576},
            "Gigabytes (GB)": {"Bytes (B)": 1073741824, "Kilobytes (KB)": 1048576, "Megabytes (MB)": 1024, "Terabytes (TB)": 1/1024},
            "Terabytes (TB)": {"Bytes (B)": 1099511627776, "Kilobytes (KB)": 1073741824, "Megabytes (MB)": 1048576, "Gigabytes (GB)": 1024}
        }


        try:
            
            result = "Invalid Conversion"

            if self.unit_type.currentText() == "Weight":

                if from_unit == "Kilogram (Kg)":
                    factor = conversion_factors_weight["Kilogram (Kg)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Grams (g)":
                    factor = conversion_factors_weight["Grams (g)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Pounds (lb)":
                    factor = conversion_factors_weight["Pounds (lb)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Ounces (oz)":
                    factor = conversion_factors_weight["Ounces (oz)"][to_unit]
                    result = factor * input_value

            elif self.unit_type.currentText() == "Length":

                if from_unit == "Kilometer (Km)":
                    factor = conversion_factors_length["Kilometer (Km)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Meter (m)":
                    factor = conversion_factors_length["Meter (m)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Feet (ft)":
                    factor = conversion_factors_length["Feet (ft)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Inch (in)":
                    factor = conversion_factors_length["Inch (in)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Miles (mi)":
                    factor = conversion_factors_length["Miles (mi)"][to_unit]
                    result = factor * input_value

            elif self.unit_type.currentText() == "Temperature":

                if from_unit == "Celsius (°C)":

                    if to_unit == "Fahrenheit (°F)":
                        result = (input_value * 9/5) + 32

                    elif to_unit == "Kelvin (K)":
                        result = input_value + 273.15

                elif from_unit == "Fahrenheit (°F)":

                    if to_unit == "Celsius (°C)":
                        result = (input_value - 32) * 5/9

                    elif to_unit == "Kelvin (K)":
                        result = (input_value - 32) * 5/9 + 273.15

                elif from_unit == "Kelvin (K)":
                         
                    if to_unit == "Celsius (°C)":
                        result = input_value - 273.15

                    elif to_unit == "Fahrenheit (°F)":
                        result = (input_value - 273.15) * 9/5 + 32

            elif self.unit_type.currentText() == "Time":

                if from_unit == "Seconds (s)":
                    factor = conversion_factors_time["Seconds (s)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Minutes (min)":
                    factor = conversion_factors_time["Minutes (min)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Hours (h)":
                    factor = conversion_factors_time["Hours (h)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Days (d)":
                    factor = conversion_factors_time["Days (d)"][to_unit]
                    result = factor * input_value

            elif self.unit_type.currentText() == "Speed":

                if from_unit == "Meters per second (m/s)":
                    factor = conversion_factors_speed["Meters per second (m/s)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Kilometers per hour (km/h)":
                    factor = conversion_factors_speed["Kilometers per hour (km/h)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Miles per hour (mph)":
                    factor = conversion_factors_speed["Miles per hour (mph)"][to_unit]
                    result = factor * input_value

            elif self.unit_type.currentText() == "Data storage":
                
                if from_unit == "Bytes (B)":
                    factor = conversion_factors_data_storage["Bytes (B)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Kilobytes (KB)":
                    factor = conversion_factors_data_storage["Kilobytes (KB)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Megabytes (MB)":
                    factor = conversion_factors_data_storage["Megabytes (MB)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Gigabytes (GB)":
                    factor = conversion_factors_data_storage["Gigabytes (GB)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Terabytes (TB)":
                    factor = conversion_factors_data_storage["Terabytes (TB)"][to_unit]
                    result = factor * input_value

            elif self.unit_type.currentText() == "Area":

                if from_unit == "Square meters (m²)":
                    factor = conversion_factors_area["Square meters (m²)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Square kilometers (km²)":
                    factor = conversion_factors_area["Square kilometers (km²)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Square feet (ft²)":
                    factor = conversion_factors_area["Square feet (ft²)"][to_unit]
                    result = factor * input_value

                elif from_unit == "Square miles (mi²)":
                    factor = conversion_factors_area["Square miles (mi²)"][to_unit]
                    result = factor * input_value

            self.label_result_box.setText(str(round(result , 15)))

        except Exception as e:
            self.label_result_box.setText("ERROR OCCURED !")
            print(f"error occured as {e}")

    def CenterWindow(self): #method for centering the window
        frame = self.frameGeometry()
        screen = QDesktopWidget().screenGeometry()
        frame.moveCenter(screen.center())
        self.move(frame.topLeft())

# Main code execution block , using if name == main so that when file is imported as module uncessesary functions dont execute
if __name__ == "__main__":
    app = QApplication(sys.argv) #passing sys argv argument for terminal based commands
    window = UnitConverter() #setting window variable with a class of unit converter
    window.show() #important to show window as windows are hidden by default
    sys.exit(app.exec()) #starting main execution loop it is wrapped around sys.exit to ensure clean exit and     prevent app from running in background