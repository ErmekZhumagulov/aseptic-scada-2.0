import threading
import time
from datetime import datetime
from PyQt6.QtGui import QIcon

def current_date_time(form):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d-%m-%y    %H-%M")
    form.time_operate.setText(str(formatted_date))

def data(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        data = client.read_integer(file_table=29, start=102, total_int=18)

        # n29:102
        control_panel_operate_image = data[0]
        if control_panel_operate_image & 0x01:
            form.control_panel_operate_image.setIcon(QIcon("library/will be image"))
        elif (control_panel_operate_image >> 1) & 0x01:
            form.control_panel_operate_image.setIcon(QIcon("library/will be image"))

        # n29:103
        info_operate_mech = data[1]
        if info_operate_mech & 0x01:
            form.info_operate_mech.setIcon(QIcon("library/overview-1.png"))
        elif (info_operate_mech >> 1) & 0x01:
            form.info_operate_mech.setIcon(QIcon("library/overview-2.png"))
        elif (info_operate_mech >> 2) & 0x01:
            form.info_operate_mech.setIcon(QIcon("library/overview-3.png"))
        elif (info_operate_mech >> 3) & 0x01:
            form.info_operate_mech.setIcon(QIcon("library/overview-4.png"))
        elif (info_operate_mech >> 4) & 0x01:
            form.info_operate_mech.setIcon(QIcon("library/overview-5.png"))
        elif (info_operate_mech >> 5) & 0x01:
            form.info_operate_mech.setIcon(QIcon("library/overview-6.png"))

        # n29:106
        secondary_alarm_operate = data[4]
        if (secondary_alarm_operate >> 2) & 0x01 or (secondary_alarm_operate >> 3) & 0x01:
            form.secondary_alarm_operate_text.setText("II")
        else:
            form.secondary_alarm_operate.setIcon(QIcon("library/"))
            form.secondary_alarm_operate_text.setText(" ")

        # n29:108
        main_alarm_operate = data[6]
        form.main_alarm_operate.setVisible(main_alarm_operate & 0x01 == 1 or (main_alarm_operate >> 1) & 0x01)

        # n29:110
        title_operate = data[8]
        form.title_operate.setText("MODULE " + str(title_operate))

        # n29:112 - n29:113 - n29:115
        info_operate_text = data[13]
        info_operate_set_text = "#"
        if info_operate_text == 0:
            info_operate_set_text = "l"
        elif info_operate_text & 0x01:
            info_operate_set_text = "s"
        elif (info_operate_text >> 1) & 0x01:
            info_operate_set_text = " "
        form.info_operate.setText(str(data[10]) + "    " + str(data[11]) + "    " + info_operate_set_text)
        form.info_operate_sh.setText(info_operate_set_text)

        # n29:114
        form.info_operate_bl.setText(str(data[12]))

        # n29:116
        control_panel_operate_ready = data[14]
        if control_panel_operate_ready == 0:
            form.control_panel_operate_ready.setStyleSheet("""
                        QPushButton {
                            background-color: transparent;
                        }
                    """)
        elif control_panel_operate_ready & 0x01:
            pass
        elif (control_panel_operate_ready >> 1) & 0x01:
            form.control_panel_operate_ready.setStyleSheet("""
                        QPushButton {
                            background-color: transparent;
                            border: 2px solid black;
                            border-color: black white white black;
                        }
                    """)

        # n29:117
        control_panel_operate_circle = data[15]
        if control_panel_operate_circle == 0:
            form.control_panel_operate_circle.setStyleSheet("""
                        QPushButton {
                            background-color: transparent;
                        }
                    """)
        elif control_panel_operate_circle & 0x01:
            pass
        elif (control_panel_operate_circle >> 1) & 0x01:
            form.control_panel_operate_circle.setStyleSheet("""
                        QPushButton {
                            background-color: transparent;
                            border: 2px solid black;
                            border-color: black white white black;
                        }
                    """)

        # n29:118
        control_panel_operate_ladder = data[16]
        if control_panel_operate_ladder == 0:
            form.control_panel_operate_ladder.setStyleSheet("""
                                QPushButton {
                                    background-color: transparent;
                                }
                            """)
        elif control_panel_operate_ladder & 0x01:
            pass
        elif (control_panel_operate_ladder >> 1) & 0x01:
            form.control_panel_operate_ladder.setStyleSheet("""
                                QPushButton {
                                    background-color: transparent;
                                    border: 2px solid black;
                                    border-color: black white white black;
                                }
                            """)

        # n29:119
        control_panel_operate_stop = data[17]
        if control_panel_operate_stop & 0x01:
            form.control_panel_operate_stop.setIcon(QIcon("library/stop.png"))
            form.control_panel_operate_stop.setStyleSheet("""
                                            QPushButton {
                                                background-color: transparent;
                                                border: 2px solid black;
                                                border-color: black white white black;
                                            }
                                        """)

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- data")

def data_block(client, form):
    # client.wait_while_com_clear()
    client.wait_no_pending_command()

    data_1 = client.read_integer(file_table=29, start=150, total_int=1)
    form.operate_data_block_1_data.setText(str(data_1[0] / 100.0))

    # client.wait_while_com_clear()
    client.wait_no_pending_command()

    data_2 = client.read_integer(file_table=29, start=145, total_int=1)
    form.operate_data_block_2_data.setText(str(data_2[0] / 10.0))

    # client.wait_while_com_clear()
    client.wait_no_pending_command()

    data_3 = client.read_integer(file_table=29, start=142, total_int=1)
    form.operate_data_block_3_data.setText(str(data_3[0] / 10.0))

def pushBtn_gr(bit):
    bit.setStyleSheet("""
                        QPushButton {
                            background-color: green;
                            border: 2px solid black;
                        }
                    """)

def bits(client, form):
    # client.wait_while_com_clear()
    client.wait_no_pending_command()

    bits = client.read_integer(file_table=29, start=4, total_int=5)

    # N29:4
    sq_operate_down_294 = bits[0]
    if sq_operate_down_294 & 0X01:
        pushBtn_gr(form.sq_operate_down_1)
    if (sq_operate_down_294 >> 1) & 0X01:
        pushBtn_gr(form.sq_operate_down_2)
    if (sq_operate_down_294 >> 2) & 0X01:
        pushBtn_gr(form.sq_operate_down_3)
    if (sq_operate_down_294 >> 3) & 0X01:
        pushBtn_gr(form.sq_operate_down_4)
    if (sq_operate_down_294 >> 4) & 0X01:
        pushBtn_gr(form.sq_operate_down_5)
    if (sq_operate_down_294 >> 5) & 0X01:
        pushBtn_gr(form.sq_operate_down_6)
    if (sq_operate_down_294 >> 6) & 0X01:
        pushBtn_gr(form.sq_operate_down_7)
    if (sq_operate_down_294 >> 7) & 0X01:
        pushBtn_gr(form.sq_operate_down_8)
    if (sq_operate_down_294 >> 8) & 0X01:
        pushBtn_gr(form.sq_operate_down_9)
    if (sq_operate_down_294 >> 9) & 0X01:
        pushBtn_gr(form.sq_operate_down_10)
    if (sq_operate_down_294 >> 10) & 0X01:
        pushBtn_gr(form.sq_operate_down_11)
    if (sq_operate_down_294 >> 11) & 0X01:
        pushBtn_gr(form.sq_operate_down_12)
    if (sq_operate_down_294 >> 12) & 0X01:
        pushBtn_gr(form.sq_operate_down_13)
    if (sq_operate_down_294 >> 13) & 0X01:
        pushBtn_gr(form.sq_operate_down_14)
    if (sq_operate_down_294 >> 14) & 0X01:
        pushBtn_gr(form.sq_operate_down_15)
    if (sq_operate_down_294 >> 15) & 0X01:
        pushBtn_gr(form.sq_operate_down_16)

    # N29:5
    sq_operate_down_295 = bits[1]
    if sq_operate_down_295 & 0X01:
        pushBtn_gr(form.sq_operate_down_17)
    if (sq_operate_down_295 >> 1) & 0X01:
        pushBtn_gr(form.sq_operate_down_18)
    if (sq_operate_down_295 >> 2) & 0X01:
        pushBtn_gr(form.sq_operate_down_19)
    if (sq_operate_down_295 >> 3) & 0X01:
        pushBtn_gr(form.sq_operate_down_20)
    if (sq_operate_down_295 >> 4) & 0X01:
        pushBtn_gr(form.sq_operate_down_21)
    if (sq_operate_down_295 >> 5) & 0X01:
        pushBtn_gr(form.sq_operate_down_22)
    if (sq_operate_down_295 >> 6) & 0X01:
        pushBtn_gr(form.sq_operate_down_23)
    if (sq_operate_down_295 >> 7) & 0X01:
        pushBtn_gr(form.sq_operate_down_24)
    if (sq_operate_down_295 >> 8) & 0X01:
        pushBtn_gr(form.sq_operate_down_25)
    if (sq_operate_down_295 >> 9) & 0X01:
        pushBtn_gr(form.sq_operate_down_26)
    if (sq_operate_down_295 >> 10) & 0X01:
        pushBtn_gr(form.sq_operate_down_27)
    if (sq_operate_down_295 >> 11) & 0X01:
        pushBtn_gr(form.sq_operate_down_28)
    if (sq_operate_down_295 >> 12) & 0X01:
        pushBtn_gr(form.sq_operate_down_29)
    if (sq_operate_down_295 >> 13) & 0X01:
        pushBtn_gr(form.sq_operate_down_30)
    if (sq_operate_down_295 >> 14) & 0X01:
        pushBtn_gr(form.sq_operate_down_31)
    if (sq_operate_down_295 >> 15) & 0X01:
        pushBtn_gr(form.sq_operate_down_32)

    # N29:6
    sq_operate_down_296 = bits[2]
    if sq_operate_down_296 & 0X01:
        pushBtn_gr(form.sq_operate_up_1)
    if (sq_operate_down_296 >> 1) & 0X01:
        pushBtn_gr(form.sq_operate_up_2)
    if (sq_operate_down_296 >> 2) & 0X01:
        pushBtn_gr(form.sq_operate_up_3)
    if (sq_operate_down_296 >> 3) & 0X01:
        pushBtn_gr(form.sq_operate_up_4)
    if (sq_operate_down_296 >> 4) & 0X01:
        pushBtn_gr(form.sq_operate_up_5)
    if (sq_operate_down_296 >> 5) & 0X01:
        pushBtn_gr(form.sq_operate_up_6)
    if (sq_operate_down_296 >> 6) & 0X01:
        pushBtn_gr(form.sq_operate_up_7)
    if (sq_operate_down_296 >> 7) & 0X01:
        pushBtn_gr(form.sq_operate_up_8)
    if (sq_operate_down_296 >> 8) & 0X01:
        pushBtn_gr(form.sq_operate_up_9)
    if (sq_operate_down_296 >> 9) & 0X01:
        pushBtn_gr(form.sq_operate_up_10)
    if (sq_operate_down_296 >> 10) & 0X01:
        pushBtn_gr(form.sq_operate_up_11)
    if (sq_operate_down_296 >> 11) & 0X01:
        pushBtn_gr(form.sq_operate_up_12)
    if (sq_operate_down_296 >> 12) & 0X01:
        pushBtn_gr(form.sq_operate_up_13)
    if (sq_operate_down_296 >> 13) & 0X01:
        pushBtn_gr(form.sq_operate_up_14)
    if (sq_operate_down_296 >> 14) & 0X01:
        pushBtn_gr(form.sq_operate_up_15)
    if (sq_operate_down_296 >> 15) & 0X01:
        pushBtn_gr(form.sq_operate_up_16)

    # N29:7
    sq_operate_down_297 = bits[3]
    if sq_operate_down_297 & 0X01:
        pushBtn_gr(form.sq_operate_up_17)
    if (sq_operate_down_297 >> 1) & 0X01:
        pushBtn_gr(form.sq_operate_up_18)
    if (sq_operate_down_297 >> 2) & 0X01:
        pushBtn_gr(form.sq_operate_up_19)
    if (sq_operate_down_297 >> 3) & 0X01:
        pushBtn_gr(form.sq_operate_up_20)
    if (sq_operate_down_297 >> 4) & 0X01:
        pushBtn_gr(form.sq_operate_up_21)
    if (sq_operate_down_297 >> 5) & 0X01:
        pushBtn_gr(form.sq_operate_up_22)
    if (sq_operate_down_297 >> 6) & 0X01:
        pushBtn_gr(form.sq_operate_up_23)
    if (sq_operate_down_297 >> 7) & 0X01:
        pushBtn_gr(form.sq_operate_up_24)
    if (sq_operate_down_297 >> 8) & 0X01:
        pushBtn_gr(form.sq_operate_up_25)
    if (sq_operate_down_297 >> 9) & 0X01:
        pushBtn_gr(form.sq_operate_up_26)
    if (sq_operate_down_297 >> 10) & 0X01:
        pushBtn_gr(form.sq_operate_up_27)
    if (sq_operate_down_297 >> 11) & 0X01:
        pushBtn_gr(form.sq_operate_up_28)
    if (sq_operate_down_297 >> 12) & 0X01:
        pushBtn_gr(form.sq_operate_up_29)
    if (sq_operate_down_297 >> 13) & 0X01:
        pushBtn_gr(form.sq_operate_up_30)
    if (sq_operate_down_297 >> 14) & 0X01:
        pushBtn_gr(form.sq_operate_up_31)
    if (sq_operate_down_297 >> 15) & 0X01:
        pushBtn_gr(form.sq_operate_up_32)

    # N29:8
    operate_btn_access = bits[4]
    # print("n29:8", labels_states, "{:016b}".format(labels_states))
    if (operate_btn_access >> 8) & 0x01:
        form.operate_btn_access.setIcon(QIcon("library/key-1.png"))

def cir_prg(client, form):
    # client.wait_while_com_clear()
    client.wait_no_pending_command()

    data = client.read_integer(file_table=28, start=19, total_int=2)
    data_cir = data[0]
    data_prg = data[1]
    form.downbar_operate_cir_data.setText(str(data_cir))
    form.downbar_operate_prg_data.setText(str(data_prg))

    form.downbar_operate_curcuit.setText("CURCUIT " + str(data_cir))


is_function_running = False
def thread_table(client, form):
    global current_widget
    global is_function_running

    # time.sleep(5)

    if is_function_running:
        return

    current_widget = form.alcip_pages.currentWidget()

    if current_widget != form.operate:
        return

    is_function_running = True

    try:
        while True:
            current_widget = form.alcip_pages.currentWidget()

            if current_widget != form.operate or is_function_running == False:
                break

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time, "The operate tab is active! from def")

            current_date_time(form)
            data(client, form)
            data_block(client, form)
            bits(client, form)
            cir_prg(client, form)

            time.sleep(5)
    finally:
        is_function_running = False

def thread(client, form):
    try:
        thread_operate = threading.Thread(target=thread_table, args=(client, form))
        thread_operate.start()
    except Exception as e:
        print(e)