import threading
import time
from datetime import datetime
from PyQt6.QtGui import QIcon

def current_date_time(form):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d-%m-%y    %H-%M")
    form.time_detail_cip_unit.setText(str(formatted_date))

def flips(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        flips_and_others = client.read_integer(file_table=29, start=0, total_int=3)

        # n29:0
        flips_and_others_n290 = flips_and_others[0]
        # print("n29:0", flips_and_others_n290, "{:016b}".format(flips_and_others_n290))
        if flips_and_others_n290 & 0x01:
            form.scheme_detail_cip_unit_m1.setIcon(QIcon("library/vent-1.png"))
        if (flips_and_others_n290 >> 8) & 0x01:
            form.scheme_detail_cip_unit_flip_v100.setIcon(QIcon("library/type1-flip-1.png"))
        if (flips_and_others_n290 >> 9) & 0x01:
            form.scheme_detail_cip_unit_flip_v101.setIcon(QIcon("library/type1-flip-1.png"))
        if (flips_and_others_n290 >> 10) & 0x01:
            form.scheme_detail_cip_unit_flip_v102.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n290 >> 11) & 0x01:
            form.scheme_detail_cip_unit_flip_v103.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n290 >> 12) & 0x01:
            form.scheme_detail_cip_unit_flip_v104.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n290 >> 13) & 0x01:
            form.scheme_detail_cip_unit_flip_v135.setIcon(QIcon("library/type3-flip-1.png"))
        if (flips_and_others_n290 >> 14) & 0x01:
            form.scheme_detail_cip_unit_flip_v136.setIcon(QIcon("library/type2-flip-1.png"))

        # n29:1
        flips_and_others_n291 = flips_and_others[1]
        # print("n29:1", flips_and_others_n291, "{:016b}".format(flips_and_others_n291))
        if flips_and_others_n291 & 0x01:
            form.scheme_detail_cip_unit_flip_v138.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n291 >> 1) & 0x01:
            form.scheme_detail_cip_unit_flip_v139.setIcon(QIcon("library/type1-flip-1.png"))
        if (flips_and_others_n291 >> 2) & 0x01:
            form.scheme_detail_cip_unit_flip_v151.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n291 >> 3) & 0x01:
            form.scheme_detail_cip_unit_flip_v111.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n291 >> 4) & 0x01:
            form.scheme_detail_cip_unit_flip_v112.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n291 >> 5) & 0x01:
            form.scheme_detail_cip_unit_flip_v113.setIcon(QIcon("library/type5-flip-1.png"))
        if (flips_and_others_n291 >> 6) & 0x01:
            form.scheme_detail_cip_unit_flip_v114.setIcon(QIcon("library/type5-flip-1.png"))
        # if (flips_and_others_n291 >> 9) & 0x01:
        #     form.scheme_detail_cip_unit_flip_v109.setIcon(QIcon("library/"))
        # if (flips_and_others_n291 >> 10) & 0x01:
        #     form.scheme_detail_cip_unit_flip_v119.setIcon(QIcon("library/"))
        if (flips_and_others_n291 >> 11) & 0x01:
            form.scheme_detail_cip_unit_fs1.setIcon(QIcon("library/type2-circle-1.png"))

        # n29:2
        flips_and_others_n292 = flips_and_others[2]
        # print("n29:2", flips_and_others_n292, "{:016b}".format(flips_and_others_n292))
        if (flips_and_others_n292 >> 9) & 0x01 == False:
            form.scheme_detail_cip_unit_container_state_3.setIcon(QIcon("library/"))
        if (flips_and_others_n292 >> 10) & 0x01 == False:
            form.scheme_detail_cip_unit_container_state_2.setIcon(QIcon("library/"))
        if (flips_and_others_n292 >> 11) & 0x01 == False:
            form.scheme_detail_cip_unit_container_state_1.setIcon(QIcon("library/"))

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- flips")

def flips_2(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        flips_and_others = client.read_integer(file_table=29, start=8, total_int=1)

        # n29:8
        labels_states = flips_and_others[0]
        # print("n29:8", labels_states, "{:016b}".format(labels_states))
        if (labels_states >> 7) & 0x01:
            form.detail_cip_unit_fc1_label_1_state.setText("%")
        if (labels_states >> 8) & 0x01:
            form.detail_cip_unit_btn_access.setIcon(QIcon("library/key-1.png"))
        if (labels_states >> 9) & 0x01:
            form.detail_cip_unit_qe1_label_1_state.setText("%")

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- flips_2")

def statebar(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        state_bar = client.read_integer(file_table=29, start=103, total_int=15)

        # n29:103
        downbar_mech = state_bar[0]
        if downbar_mech & 0x01:
            form.detail_cip_unit_mech.setIcon(QIcon("library/overview-1.png"))
        elif (downbar_mech >> 1) & 0x01:
            form.detail_cip_unit_mech.setIcon(QIcon("library/overview-2.png"))
        elif (downbar_mech >> 2) & 0x01:
            form.detail_cip_unit_mech.setIcon(QIcon("library/overview-3.png"))
        elif (downbar_mech >> 3) & 0x01:
            form.detail_cip_unit_mech.setIcon(QIcon("library/overview-4.png"))
        elif (downbar_mech >> 4) & 0x01:
            form.detail_cip_unit_mech.setIcon(QIcon("library/overview-5.png"))
        elif (downbar_mech >> 5) & 0x01:
            form.detail_cip_unit_mech.setIcon(QIcon("library/overview-6.png"))

        # n29:108
        alarm_cip_unit_state = state_bar[5]
        form.alarm_cip_unit.setVisible(alarm_cip_unit_state & 0x01 or (alarm_cip_unit_state >> 1) & 0x01)

        # n29:110
        scheme_label_main_cip_unit = state_bar[7]
        form.title_cip_unit.setText("MODULE " + str(scheme_label_main_cip_unit))
        if scheme_label_main_cip_unit == 141:
            form.scheme_label_main_cip_unit.setText("A")
        elif scheme_label_main_cip_unit == 142:
            form.scheme_label_main_cip_unit.setText("B")
        elif scheme_label_main_cip_unit == 143:
            form.scheme_label_main_cip_unit.setText("C")
        elif scheme_label_main_cip_unit == 144:
            form.scheme_label_main_cip_unit.setText("D")
        elif scheme_label_main_cip_unit == 145:
            form.scheme_label_main_cip_unit.setText("E")
        elif scheme_label_main_cip_unit == 146:
            form.scheme_label_main_cip_unit.setText("F")

        # n29:112 - n29:113 - n29:115
        info_cip_unit_text = state_bar[12]
        info_cip_unit_set_text = "#"
        if info_cip_unit_text == 0:
            info_cip_unit_set_text = "l"
        elif info_cip_unit_text & 0x01:
            info_cip_unit_set_text = "s"
        elif (info_cip_unit_text >> 1) & 0x01:
            info_cip_unit_set_text = " "
        form.info_cip_unit.setText(str(state_bar[9]) + "    " + str(state_bar[10]) + "    " + info_cip_unit_set_text)
        form.info_cip_unit_down.setText(info_cip_unit_set_text)

        # n29:114
        form.info_cip_unit_down_bl.setText(str(state_bar[11]))

        # n29:116
        detail_cip_unit_line = state_bar[13]
        if detail_cip_unit_line == 0:
            form.detail_cip_unit_line.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                }
            """)
        elif detail_cip_unit_line & 0x01:
            pass
        elif (detail_cip_unit_line >> 1) & 0x01:
            form.detail_cip_unit_line.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: 2px solid black;
                    border-color: black white white black;
                }
            """)

        # n29:117
        detail_cip_unit_circle = state_bar[14]
        if detail_cip_unit_circle == 0:
            form.detail_cip_unit_circle.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                }
            """)
        elif detail_cip_unit_circle & 0x01:
            pass
        elif (detail_cip_unit_circle >> 1) & 0x01:
            form.detail_cip_unit_circle.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: 2px solid black;
                    border-color: black white white black;
                }
            """)

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- statebar")

def data(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        scheme_data = client.read_integer(file_table=29, start=140, total_int=14)

        # n29:140
        scheme_data_n29_140 = scheme_data[0] / 10.0
        form.detail_cip_unit_te2_data_2.setText(str(scheme_data_n29_140))

        # n29:141
        scheme_data_n29_141 = scheme_data[1] / 10.0
        form.detail_cip_unit_te2_data_1.setText(str(scheme_data_n29_141))

        # n29:143
        scheme_data_n29_143 = scheme_data[3] / 10.0
        form.detail_cip_unit_te3_data_2.setText(str(scheme_data_n29_143))

        # n29:144
        scheme_data_n29_144 = scheme_data[4] / 10.0
        form.detail_cip_unit_te3_data_1.setText(str(scheme_data_n29_144))

        # n29:145
        scheme_data_n29_145 = scheme_data[5] / 10.0
        form.detail_cip_unit_qe1_data_3.setText(str(scheme_data_n29_145))

        # n29:146
        scheme_data_n29_146 = scheme_data[6] / 100.0
        form.detail_cip_unit_qe1_data_2.setText(str(scheme_data_n29_146))

        # n29:148
        scheme_data_n29_148 = scheme_data[8] / 100.0
        form.detail_cip_unit_qe1_data_1.setText(str(scheme_data_n29_148))

        # n29:150
        scheme_data_n29_150 = scheme_data[10] / 100.0
        form.detail_cip_unit_fc1_data_2.setText(str(scheme_data_n29_150))

        # n29:152
        scheme_data_n29_152 = scheme_data[12] / 100.0
        form.detail_cip_unit_fc1_data_1.setText(str(scheme_data_n29_152))

        # n29:153
        scheme_data_n29_153 = scheme_data[13]
        form.detail_cip_unit_ft1_data.setText(str(scheme_data_n29_153))

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- data")

def data_2(client, form):
    try:
        # client.wait_while_com_clear()
        client.wait_no_pending_command()

        scheme_data_2 = client.read_integer(file_table=29, start=160, total_int=3)

        # n29:160
        scheme_data_n29_160 = scheme_data_2[0] / 10.0
        form.detail_cip_unit_tc1_data_2.setText(str(scheme_data_n29_160))

        # n29:162
        scheme_data_n29_162 = scheme_data_2[2] / 10.0
        form.detail_cip_unit_tc1_data_1.setText(str(scheme_data_n29_162))

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- data_2")

def label_state(client, form):
    try:
        client.wait_no_pending_command()
        # client.wait_while_com_clear()

        green_light = client.read_integer(file_table=29, start=189, total_int=1)

        scheme_detail_cip_unit_flip_v151_circle = green_light[0]
        # n29:189/0
        if scheme_detail_cip_unit_flip_v151_circle & 0x01:
            form.scheme_detail_cip_unit_flip_v151_circle.setIcon(QIcon("library/type1-circle-1.png"))
        else:
            form.scheme_detail_cip_unit_flip_v151_circle.setIcon(QIcon("library/"))
        # n29:189/1
        if (scheme_detail_cip_unit_flip_v151_circle >> 1) & 0x01:
            form.scheme_detail_cip_unit_flip_v151_circle.setIcon(QIcon("library/type1-circle-2.png"))
            form.scheme_detail_cip_unit_flip_v104_circle.setIcon(QIcon("library/type1-circle-1.png"))
        else:
            form.scheme_detail_cip_unit_flip_v104_circle.setIcon(QIcon("library/"))
        # n29:189/2
        if (scheme_detail_cip_unit_flip_v151_circle >> 2) & 0x01:
            form.scheme_detail_cip_unit_flip_v104_circle.setIcon(QIcon("library/type1-circle-2.png"))
            form.scheme_detail_cip_unit_flip_v102_circle.setIcon(QIcon("library/type1-circle-1.png"))
        else:
            form.scheme_detail_cip_unit_flip_v102_circle.setIcon(QIcon("library/"))
        # n29:189/3
        if (scheme_detail_cip_unit_flip_v151_circle >> 3) & 0x01:
            form.scheme_detail_cip_unit_flip_v102_circle.setIcon(QIcon("library/type1-circle-2.png"))
            form.scheme_detail_cip_unit_flip_v103_circle.setIcon(QIcon("library/type1-circle-1.png"))
        else:
            form.scheme_detail_cip_unit_flip_v103_circle.setIcon(QIcon("library/"))
        # n29:189/4
        if (scheme_detail_cip_unit_flip_v151_circle >> 4) & 0x01:
            form.scheme_detail_cip_unit_green_light.setIcon(QIcon("library/type1-circle-1.png"))
            form.scheme_detail_cip_unit_flip_v103_circle.setIcon(QIcon("library/type1-circle-2.png"))
        else:
            form.scheme_detail_cip_unit_green_light.setIcon(QIcon("library/"))

    except Exception as e:
        print("[WARNING] An error occurred while reading PLC data --- label_state")



is_function_running = False
def thread_table(client, form):
    global current_widget
    global is_function_running

    if is_function_running:
        return

    current_widget = form.alcip_pages.currentWidget()

    if current_widget != form.detail_cip_unit:
        return

    is_function_running = True

    try:
        while True:
            current_widget = form.alcip_pages.currentWidget()

            if current_widget != form.detail_cip_unit or is_function_running == False:
                break

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time, "The detail_cip_unit tab is active! from def")

            current_date_time(form)
            flips(client, form)
            flips_2(client, form)
            statebar(client, form)
            data(client, form)
            data_2(client, form)
            label_state(client, form)

            time.sleep(5)
    finally:
        is_function_running = False

def thread(client, form):
    try:
        thread_detail_cip_unit = threading.Thread(target=thread_table, args=(client, form))
        thread_detail_cip_unit.start()
    except Exception as e:
        print(e)