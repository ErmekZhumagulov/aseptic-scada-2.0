import threading
import time
from datetime import datetime
from PyQt6.QtGui import QIcon
from df1.models.df1_base import BIT

def current_date_time(form):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d-%m-%y    %H-%M")
    form.time_overview.setText(str(formatted_date))

def alarm(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        main_alarm = client.read_integer(file_table=29, start=108, total_int=1)

        # n29:108
        alarm_overview = main_alarm[0]
        form.alarm_overview.setVisible(alarm_overview & 0x01 == 1 or (alarm_overview >> 1) & 0x01)

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- alarm")

def status(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        module_141_142 = client.read_integer(file_table=29, start=60, total_int=9)

        # n29:60
        frame_141_mech = module_141_142[0]
        if frame_141_mech & 0x01:
            form.frame_141_mech.setIcon(QIcon("library/overview-1.png"))
        elif (frame_141_mech >> 1) & 0x01:
            form.frame_141_mech.setIcon(QIcon("library/overview-2.png"))
        elif (frame_141_mech >> 2) & 0x01:
            form.frame_141_mech.setIcon(QIcon("library/overview-3.png"))
        elif (frame_141_mech >> 3) & 0x01:
            form.frame_141_mech.setIcon(QIcon("library/overview-4.png"))
        elif (frame_141_mech >> 4) & 0x01:
            form.frame_141_mech.setIcon(QIcon("library/overview-5.png"))
        elif (frame_141_mech >> 5) & 0x01:
            form.frame_141_mech.setIcon(QIcon("library/overview-6.png"))

        # n29:61
        form.label_module_141_data.setText(str(module_141_142[1]))

        # n29:62
        alarm_module_141 = module_141_142[2]
        form.alarm_module_141.setVisible(alarm_module_141 & 0x01 or (alarm_module_141 >> 1) & 0x01 or (alarm_module_141 >> 2) & 0x01 or (alarm_module_141 >> 3) & 0x01)

        # n29:66
        frame_142_mech = module_141_142[6]
        if frame_142_mech & 0x01:
            form.frame_142_mech.setIcon(QIcon("library/overview-1.png"))
        elif (frame_142_mech >> 1) & 0x01:
            form.frame_142_mech.setIcon(QIcon("library/overview-2.png"))
        elif (frame_142_mech >> 2) & 0x01:
            form.frame_142_mech.setIcon(QIcon("library/overview-3.png"))
        elif (frame_142_mech >> 3) & 0x01:
            form.frame_142_mech.setIcon(QIcon("library/overview-4.png"))
        elif (frame_142_mech >> 4) & 0x01:
            form.frame_142_mech.setIcon(QIcon("library/overview-5.png"))
        elif (frame_142_mech >> 5) & 0x01:
            form.frame_142_mech.setIcon(QIcon("library/overview-6.png"))

        # n29:67
        form.label_module_142_data.setText(str(module_141_142[7]))

        # n29:68
        alarm_module_142 = module_141_142[8]
        form.alarm_module_142.setVisible(alarm_module_142 & 0x01 or (alarm_module_142 >> 1) & 0x01 or (alarm_module_142 >> 2) & 0x01 or (alarm_module_142 >> 3) & 0x01)

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- status")

def data(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        data_module_141_142 = client.read_integer(file_table=29, start=190, total_int=6)

        # n29:190
        data_module_141_c = data_module_141_142[0] / 10.0
        form.data_module_141_c.setText(str(data_module_141_c))

        # n29:191
        data_module_141_m3_h = data_module_141_142[1] / 100.0
        form.data_module_141_m3_h.setText(str(data_module_141_m3_h))

        # n29:192
        data_module_141_ms_cm = data_module_141_142[2] / 10.0
        form.data_module_141_ms_cm.setText(str(data_module_141_ms_cm))

        # n29:193
        data_module_142_c = data_module_141_142[3] / 10.0
        form.data_module_142_c.setText(str(data_module_142_c))

        # n29:194
        data_module_142_m3_h = data_module_141_142[4] / 100.0
        form.data_module_142_m3_h.setText(str(data_module_142_m3_h))

        # n29:195
        data_module_142_ms_cm = data_module_141_142[5] / 10.0
        form.data_module_142_ms_cm.setText(str(data_module_142_ms_cm))

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- data_overview")



is_function_running = False
def thread_table(client, form):
    global current_widget
    global is_function_running

    if is_function_running:
        return

    current_widget = form.alcip_pages.currentWidget()

    if current_widget != form.overview:
        return

    is_function_running = True

    try:
        while True:
            current_widget = form.alcip_pages.currentWidget()

            if current_widget != form.overview or is_function_running == False:
                break

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time, "The overview tab is active! from def")

            current_date_time(form)
            alarm(client, form)
            status(client, form)
            data(client, form)
            # form.frame_142.clicked.connect(on_frame_142_btn_operate)

            time.sleep(5)
    finally:
        is_function_running = False

def thread(client, form):
    try:
        thread_overview = threading.Thread(target=thread_table, args=(client, form))
        thread_overview.start()
    except Exception as e:
        print(e)