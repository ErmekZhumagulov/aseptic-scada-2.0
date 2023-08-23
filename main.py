from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon

import time
from serial.serialutil import SerialTimeoutException, SerialException
from functools import partial
import threading

from codes import button_logics
from codes.alcip import overview
from codes.alcip import detail_cip_unit
from codes.alcip import operate

import serial
from df1.models.df1_serial_client import Df1SerialClient

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()

client = None
x1 = None
x2 = None

def connect_to_plc():
    global client
    try:
        client = Df1SerialClient(plc_type='SLC 5/04 CPU', src=0x1, dst=0x3,
                                 port='COM3',
                                 baudrate=9600, parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,
                                 timeout=5)
        print(client.connect())
        # timer.start(3500)
    except Exception as e:
        print("Error connecting to PLC:", str(e))
        client = None
        # timer.stop()  # Stop the timer
        reconnect_to_plc()  # Attempt to reconnect

def reconnect_to_plc():
    global client
    while client is None or not client.is_connected():  # Keep attempting to reconnect until successful
        try:
            time.sleep(1)
            print("try-----------------------------------------------------------------------------")
            connect_to_plc()
        except KeyboardInterrupt:
            app.quit()  # Exit the application if interrupted by the user
        except Exception as e:
            print(e)

def reconnect_to_plc_prevention():
    global client
    while True:
        try:
            time.sleep(12 * 60 * 60)
            time.sleep(0.5)
            client.close()
            time.sleep(1.5)
            connect_to_plc()
            time.sleep(0.1)
            form.alcip_pages.setCurrentIndex(3)
            time.sleep(6)
            form.alcip_pages.setCurrentIndex(0)
            overview.thread(client, form)
            print("try-------------reconnect_to_plc_prevention----------------------------------------")
        except KeyboardInterrupt:
            app.quit()  # Exit the application if interrupted by the user
        except Exception as e:
            print(e)

def on_close():
    if client is not None:
        client.close()
        # timer.stop()  # Stop the timer
    app.quit()

def active_tab_run_code():
    try:
        current_widget = form.alcip_pages.currentWidget()
        print (current_widget)

        if current_widget == form.overview:
            print("The overview tab is active!")
            overview.thread(client, form)
        elif current_widget == form.operate:
            print("The operate tab is active!")
            operate.thread(client, form)
        elif current_widget == form.detail_cip_unit:
            print("The detail_cip_unit tab is active!")
            detail_cip_unit.thread(client, form)
        elif current_widget == form.detail_cip_tank:
            print("The detail_cip_tank tab is active!")
        elif current_widget == form.parameter_edit:
            print("The parameter_edit tab is active!")
        elif current_widget == form.station_selection:
            print("The station_selection tab is active!")
        elif current_widget == form.trend_diagram:
            print("The trend_diagram tab is active!")
        elif current_widget == form.alarm_log:
            print("The alarm_log tab is active!")
        elif current_widget == form.service_menu:
            print("The service_menu tab is active!")
        elif current_widget == form.date_time:
            print("The date_time tab is active!")
        elif current_widget == form.language:
            print("The language tab is active!")
        elif current_widget == form.fc:
            print("The fc tab is active!")
        elif current_widget == form.tc:
            print("The tc tab is active!")
        elif current_widget == form.circuit_sign:
            print("The circuit_sign tab is active!")
        elif current_widget == form.program_sign:
            print("The program_sign tab is active!")
        elif current_widget == form.list_1:
            print("The list_1 tab is active!")

    except Exception as e:
        print (e)

def main():
    window.showFullScreen()
    app.aboutToQuit.connect(on_close)

    reconnect_to_plc()  # Start the initial connection process

    thread_conn = threading.Thread(target=reconnect_to_plc_prevention)
    thread_conn.start()

    overview.thread(client, form)
    form.alcip_pages.currentChanged.connect(active_tab_run_code)
    button_logics.switch_logic(client, form)
    button_logics.unvisable_tabs(form)

    app.exec()

if __name__ == '__main__':
    main()
