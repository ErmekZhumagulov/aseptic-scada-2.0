from PyQt6.QtWidgets import QTabBar
from df1.models.df1_base import BIT

def switch_logic(client, form):
    def on_overview_btn_goto_service_menu():
        form.alcip_pages.setCurrentWidget(form.service_menu)
    form.overview_btn_goto_service_menu.clicked.connect(on_overview_btn_goto_service_menu)
    def on_overview_btn_goto_alarm_log():
        form.alcip_pages.setCurrentWidget(form.alarm_log)
    form.overview_btn_goto_alarm_log.clicked.connect(on_overview_btn_goto_alarm_log)

    # client.wait_while_com_clear()
    client.wait_no_pending_command()
    def on_frame_141_btn_operate():
        form.alcip_pages.setCurrentWidget(form.operate)
        # print("read_data_to_write --- ", client.read_integer(file_table=28, start=0)) # , data=[0b0001], total_int=1, bit=BIT.BIT0
    form.frame_141.clicked.connect(on_frame_141_btn_operate)
    def on_frame_142_btn_operate():
        form.alcip_pages.setCurrentWidget(form.operate)
    form.frame_142.clicked.connect(on_frame_142_btn_operate)

    def on_info_operate_sec_frame_btn_detail_cip_unit():
        form.alcip_pages.setCurrentWidget(form.detail_cip_unit)
    form.info_operate_sec_frame.clicked.connect(on_info_operate_sec_frame_btn_detail_cip_unit)
    def on_detail_cip_unit_btn_goto_operate_141():
        form.alcip_pages.setCurrentWidget(form.operate)
    form.detail_cip_unit_btn_goto_operate.clicked.connect(on_detail_cip_unit_btn_goto_operate_141)
    def on_operate_btn_back():
        form.alcip_pages.setCurrentWidget(form.overview)
    form.operate_btn_back.clicked.connect(on_operate_btn_back)

def unvisable_tabs(form):
    form.alcip_pages.tabBar().hide()
