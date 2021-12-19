
from PyQt5 import QtCore, QtGui, QtWidgets
from Evaluate import Ui_Evaluate_team
import data as dt
from new_team import Ui_newteam_Dialog
from PyQt5.QtWidgets import QMessageBox
from open_team import Ui_Dialog
batsman_count = 0
bowler_count = 0
allrounder_count = 0
wk_count = 0
total_points = 1000
used_points = 0
no_of_team = 0
class Ui_Fantasy_app_window(object):
    def setupUi(self, Fantasy_app_window):
        Fantasy_app_window.setObjectName("Fantasy_app_window")
        Fantasy_app_window.resize(897, 822)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        Fantasy_app_window.setFont(font)
        Fantasy_app_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        Fantasy_app_window.setIconSize(QtCore.QSize(10, 10))
        self.widget = QtWidgets.QWidget(Fantasy_app_window)
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 50, 781, 691))
        self.layoutWidget.setObjectName("layoutWidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.vertical_selection = QtWidgets.QVBoxLayout()
        self.vertical_selection.setObjectName("vertical_selection")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    background-color: #F0FFF;\n"
"}")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setIndent(9)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.vertical_selection.addLayout(self.horizontalLayout_2)
        self.horizontal_players_no = QtWidgets.QHBoxLayout()
        self.horizontal_players_no.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontal_players_no.setContentsMargins(9, -1, 0, -1)
        self.horizontal_players_no.setObjectName("horizontal_players_no")
        self.bat_2 = QtWidgets.QLabel(self.layoutWidget)
        self.bat_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.bat_2.setFont(font)
        self.bat_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bat_2.setIndent(1)
        self.bat_2.setObjectName("bat_2")
        self.horizontal_players_no.addWidget(self.bat_2)
        self.bat_label = QtWidgets.QLabel(self.layoutWidget)
        self.bat_label.setText("")
        self.bat_label.setObjectName("bat_label")
        self.horizontal_players_no.addWidget(self.bat_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_players_no.addItem(spacerItem1)
        self.bow_2 = QtWidgets.QLabel(self.layoutWidget)
        self.bow_2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.bow_2.setFont(font)
        self.bow_2.setObjectName("bow_2")
        self.horizontal_players_no.addWidget(self.bow_2)
        self.now_label = QtWidgets.QLabel(self.layoutWidget)
        self.now_label.setText("")
        self.now_label.setObjectName("now_label")
        self.horizontal_players_no.addWidget(self.now_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_players_no.addItem(spacerItem2)
        self.ar_2 = QtWidgets.QLabel(self.layoutWidget)
        self.ar_2.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.ar_2.setFont(font)
        self.ar_2.setObjectName("ar_2")
        self.horizontal_players_no.addWidget(self.ar_2)
        self.ar_label = QtWidgets.QLabel(self.layoutWidget)
        self.ar_label.setText("")
        self.ar_label.setObjectName("ar_label")
        self.horizontal_players_no.addWidget(self.ar_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_players_no.addItem(spacerItem3)
        self.wk_2 = QtWidgets.QLabel(self.layoutWidget)
        self.wk_2.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.wk_2.setFont(font)
        self.wk_2.setObjectName("wk_2")
        self.horizontal_players_no.addWidget(self.wk_2)
        self.wk_label = QtWidgets.QLabel(self.layoutWidget)
        self.wk_label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.wk_label.setText("")
        self.wk_label.setObjectName("wk_label")
        self.horizontal_players_no.addWidget(self.wk_label)
        self.vertical_selection.addLayout(self.horizontal_players_no)
        self.main_layout.addLayout(self.vertical_selection)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem4)
        self.horizontalpoints = QtWidgets.QHBoxLayout()
        self.horizontalpoints.setContentsMargins(52, -1, 185, -1)
        self.horizontalpoints.setObjectName("horizontalpoints")
        self.point_available = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.point_available.setFont(font)
        self.point_available.setObjectName("point_available")
        self.horizontalpoints.addWidget(self.point_available)
        self.point_available_lable = QtWidgets.QLabel(self.layoutWidget)
        self.point_available_lable.setText("")
        self.point_available_lable.setObjectName("point_available_lable")
        self.horizontalpoints.addWidget(self.point_available_lable)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalpoints.addItem(spacerItem5)
        self.points_used = QtWidgets.QLabel(self.layoutWidget)
        self.points_used.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.points_used.setFont(font)
        self.points_used.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.points_used.setIndent(17)
        self.points_used.setObjectName("points_used")
        self.horizontalpoints.addWidget(self.points_used)
        self.points_used_label = QtWidgets.QLabel(self.layoutWidget)
        self.points_used_label.setText("")
        self.points_used_label.setObjectName("points_used_label")
        self.horizontalpoints.addWidget(self.points_used_label)
        self.main_layout.addLayout(self.horizontalpoints)
        self.horizontal_radio = QtWidgets.QHBoxLayout()
        self.horizontal_radio.setContentsMargins(6, -1, 0, -1)
        self.horizontal_radio.setObjectName("horizontal_radio")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_radio.addItem(spacerItem6)
        self.bat_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.bat_button.setFont(font)
        self.bat_button.setObjectName("bat_button")
        self.horizontal_radio.addWidget(self.bat_button)
        self.bow_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.bow_button.setFont(font)
        self.bow_button.setObjectName("bow_button")
        self.horizontal_radio.addWidget(self.bow_button)
        self.ar_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.ar_button.setFont(font)
        self.ar_button.setObjectName("ar_button")
        self.horizontal_radio.addWidget(self.ar_button)
        self.wk_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.wk_button.setFont(font)
        self.wk_button.setObjectName("wk_button")
        self.horizontal_radio.addWidget(self.wk_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_radio.addItem(spacerItem7)
        self.team_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.team_name.setFont(font)
        self.team_name.setIndent(0)
        self.team_name.setObjectName("team_name")
        self.horizontal_radio.addWidget(self.team_name)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontal_radio.addWidget(self.lineEdit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_radio.addItem(spacerItem8)
        self.horizontal_radio.setStretch(1, 1)
        self.horizontal_radio.setStretch(2, 1)
        self.horizontal_radio.setStretch(3, 1)
        self.horizontal_radio.setStretch(4, 1)
        self.horizontal_radio.setStretch(5, 4)
        self.horizontal_radio.setStretch(6, 2)
        self.main_layout.addLayout(self.horizontal_radio)
        self.horizontal_list = QtWidgets.QHBoxLayout()
        self.horizontal_list.setObjectName("horizontal_list")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_list.addItem(spacerItem9)
        self.player_list = QtWidgets.QListWidget(self.layoutWidget)
        self.player_list.setObjectName("player_list")
        self.horizontal_list.addWidget(self.player_list)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_list.addItem(spacerItem10)
        self.salected_list = QtWidgets.QListWidget(self.layoutWidget)
        self.salected_list.setObjectName("salected_list")
        self.horizontal_list.addWidget(self.salected_list)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_list.addItem(spacerItem11)
        self.horizontal_list.setStretch(2, 1)
        self.main_layout.addLayout(self.horizontal_list)
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(2, 1)
        self.main_layout.setStretch(3, 1)
        self.main_layout.setStretch(4, 25)
        self.full_frame = QtWidgets.QFrame(self.widget)
        self.full_frame.setGeometry(QtCore.QRect(30, 29, 821, 731))
        self.full_frame.setStyleSheet("QFrame{\n"
"    background-color:#f0efef;\n"
"}")
        self.full_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.full_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.full_frame.setObjectName("full_frame")
        self.head_frame = QtWidgets.QFrame(self.full_frame)
        self.head_frame.setGeometry(QtCore.QRect(0, 0, 821, 101))
        self.head_frame.setStyleSheet("QFrame{\n"
"background-color: #ddeedd;\n"
"}")
        self.head_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.head_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.head_frame.setObjectName("head_frame")
        self.full_frame.raise_()
        self.layoutWidget.raise_()
        Fantasy_app_window.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(Fantasy_app_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.menuManage_teams.setFont(font)
        self.menuManage_teams.setObjectName("menuManage_teams")
        Fantasy_app_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fantasy_app_window)
        self.statusbar.setObjectName("statusbar")
        Fantasy_app_window.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(Fantasy_app_window)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(Fantasy_app_window)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(Fantasy_app_window)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(Fantasy_app_window)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_teams.addAction(self.actionOpen_Team)
        self.menuManage_teams.addAction(self.actionNew_Team)
        self.menuManage_teams.addAction(self.actionSave_Team)
        self.menuManage_teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_teams.menuAction())

        self.retranslateUi(Fantasy_app_window)
        QtCore.QMetaObject.connectSlotsByName(Fantasy_app_window)

        self.actionEvaluate_Team.triggered.connect(self.evaluate_team)
        self.bat_button.toggled.connect(self.radio_status)
        self.bow_button.toggled.connect(self.radio_status)
        self.ar_button.toggled.connect(self.radio_status)
        self.wk_button.toggled.connect(self.radio_status)
        self.player_list.itemDoubleClicked.connect(self.remove_player_list)
        self.salected_list.itemDoubleClicked.connect(self.remove_selected_list)
        self.actionSave_Team.triggered.connect(self.save_team)
        self.actionOpen_Team.triggered.connect(self.open_team)
        self.actionNew_Team.triggered.connect(self.new_team)
    def retranslateUi(self, Fantasy_app_window):
        _translate = QtCore.QCoreApplication.translate
        Fantasy_app_window.setWindowTitle(_translate("Fantasy_app_window", "CRICKET APP"))
        self.label.setText(_translate("Fantasy_app_window", "Your Selection"))
        self.bat_2.setText(_translate("Fantasy_app_window", "Batsman(BAT)"))
        self.bow_2.setText(_translate("Fantasy_app_window", "Bowlers(BOW)"))
        self.ar_2.setText(_translate("Fantasy_app_window", "Allrounders(AR)"))
        self.wk_2.setText(_translate("Fantasy_app_window", "Wicket_keeper(WK)"))
        self.point_available.setText(_translate("Fantasy_app_window", "Points Available"))
        self.points_used.setText(_translate("Fantasy_app_window", "Points Used"))
        self.bat_button.setText(_translate("Fantasy_app_window", "BAT"))
        self.bow_button.setText(_translate("Fantasy_app_window", "BOW"))
        self.ar_button.setText(_translate("Fantasy_app_window", "AR"))
        self.wk_button.setText(_translate("Fantasy_app_window", "WK"))
        self.team_name.setText(_translate("Fantasy_app_window", "Team Name"))
        self.menuManage_teams.setTitle(_translate("Fantasy_app_window", "Manage teams"))
        self.actionNew_Team.setText(_translate("Fantasy_app_window", "New Team"))
        self.actionOpen_Team.setText(_translate("Fantasy_app_window", "Open Team"))
        self.actionSave_Team.setText(_translate("Fantasy_app_window", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("Fantasy_app_window", "Evaluate Team"))

    def evaluate_team(self):
        name = dt.get_team_names()
        if not name:
            self.no_team()
        else:
            Evaluate_team = QtWidgets.QDialog()
            ui = Ui_Evaluate_team()
            ui.setupUi(Evaluate_team)
            ui.team_list()
            ui.match_list()
            Evaluate_team.show()
            Evaluate_team.exec_()

    def radio_status(self):
        if self.bat_button.isChecked() == True:
            self.player_list.clear()
            for i in dt.batsman:
                self.player_list.addItem(i)
        if self.bow_button.isChecked() == True:
            self.player_list.clear()
            for i in dt.bowlers:
                self.player_list.addItem(i)
        if self.ar_button.isChecked() == True:
            self.player_list.clear()
            for i in dt.all_rounder:
                self.player_list.addItem(i)
        if self.wk_button.isChecked() == True:
            self.player_list.clear()
            for i in dt.wicket_keeper:
                self.player_list.addItem(i)

    def remove_player_list(self, item):
        global batsman_count, bowler_count, allrounder_count, wk_count, total_points, used_points

        if item.text() in dt.batsman:
            if batsman_count <= 3:
                total_points = total_points - dt.name_value[item.text()]
                if total_points>=0:
                    batsman_count += 1
                    dt.final_team_list.append(item.text())
                    self.player_list.takeItem(self.player_list.row(item))
                    self.salected_list.addItem(item.text())
                    dt.batsman.remove(item.text())
                    used_points = used_points + dt.name_value[item.text()]
                    self.maintain_points()
                else:
                    total_points = total_points + dt.name_value[item.text()]
                    self.error_msg("Running Shortage Of Points !!!!")
            else:
                self.alert_message("4", "Batsman")

        if item.text() in dt.bowlers:

            if bowler_count<=2:
                total_points = total_points - dt.name_value[item.text()]
                if total_points>=0:
                    bowler_count += 1
                    dt.final_team_list.append(item.text())
                    self.player_list.takeItem(self.player_list.row(item))
                    self.salected_list.addItem(item.text())
                    dt.bowlers.remove(item.text())
                    used_points = used_points + dt.name_value[item.text()]
                    self.maintain_points()
                else:
                    total_points = total_points + dt.name_value[item.text()]
                    self.error_msg("Running Shortage Of Points !!!!")
            else:
                self.alert_message("3", "Bowler")
        if item.text() in dt.all_rounder:
            if allrounder_count<=2:
                total_points = total_points - dt.name_value[item.text()]
                if total_points>=0:
                    allrounder_count += 1
                    dt.final_team_list.append(item.text())
                    self.player_list.takeItem(self.player_list.row(item))
                    self.salected_list.addItem(item.text())
                    dt.all_rounder.remove(item.text())
                    used_points = used_points + dt.name_value[item.text()]
                    self.maintain_points()
                else:
                    total_points = total_points + dt.name_value[item.text()]
                    self.error_msg("Running Shortage Of Points !!!!")
            else:
                self.alert_message("3", "AllRounder")
        if item.text() in dt.wicket_keeper:
            if wk_count <= 0:
                total_points = total_points - dt.name_value[item.text()]
                if total_points>=0:
                    wk_count += 1
                    dt.final_team_list.append(item.text())
                    self.player_list.takeItem(self.player_list.row(item))
                    self.salected_list.addItem(item.text())
                    dt.wicket_keeper.remove(item.text())
                    used_points = used_points + dt.name_value[item.text()]
                    self.maintain_points()
                else:
                    total_points=total_points+dt.name_value[item.text()]
                    self.error_msg("Running Shortage Of Points !!!!")
            else:
                self.alert_message("1", "WeeketKeeper")
    def remove_selected_list(self, item):
        global batsman_count, bowler_count, allrounder_count, wk_count, total_points, used_points
        self.salected_list.takeItem(self.salected_list.row(item))
        for i in dt.players_stats:
            if i[1] == item.text() and i[3] == "BAT":
                dt.batsman.append(item.text())
                dt.final_team_list.remove(item.text())
                batsman_count -= 1
                total_points = total_points + dt.name_value[item.text()]
                used_points = used_points - dt.name_value[item.text()]
                self.maintain_points()
                if self.bat_button.isChecked() == True:
                    self.player_list.addItem(item.text())
            if i[1] == item.text() and i[3] == "BWL":
                dt.bowlers.append(item.text())
                dt.final_team_list.remove(item.text())
                bowler_count-=1
                total_points = total_points + dt.name_value[item.text()]
                used_points = used_points - dt.name_value[item.text()]
                self.maintain_points()
                if self.bow_button.isChecked() == True:
                    self.player_list.addItem((item.text()))
            if i[1] == item.text() and i[3] == "AR":
                dt.all_rounder.append(item.text())
                dt.final_team_list.remove(item.text())
                allrounder_count-=1
                total_points = total_points + dt.name_value[item.text()]
                used_points = used_points - dt.name_value[item.text()]
                self.maintain_points()
                if self.ar_button.isChecked() == True:
                    self.player_list.addItem((item.text()))
            if i[1] == item.text() and i[3] == "WK":
                dt.wicket_keeper.append(item.text())
                dt.final_team_list.remove(item.text())
                wk_count-=1
                total_points = total_points + dt.name_value[item.text()]
                used_points = used_points - dt.name_value[item.text()]
                self.maintain_points()
                if self.wk_button.isChecked() == True:
                    self.player_list.addItem((item.text()))

    def new_team(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_newteam_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        res = Dialog.exec_()

        if res == QtWidgets.QDialog.Accepted:
            if ui.team():
                self.lineEdit.setText(ui.team())
                self.maintain_points()
                self.refresh_points()
            else:
                if res == QtWidgets.QDialog.Accepted:
                    self.error_msg("Please Enter Team Name!!!!")
    def maintain_points(self):
        self.bat_label.setText(str(batsman_count))
        self.now_label.setText(str(bowler_count))
        self.ar_label.setText(str(allrounder_count))
        self.wk_label.setText(str(wk_count))
        self.point_available_lable.setText(str(total_points))
        self.points_used_label.setText(str(used_points))

    def alert_message(self, no, type):
        bat_elert = QMessageBox()
        bat_elert.setWindowTitle("Error")
        bat_elert.setText(f"You Can't Select More Than {no} {type}")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        bat_elert.setFont(font)
        bat_elert.exec_()
    def save_message(self,msg):
        save_msg = QMessageBox()
        save_msg.setWindowTitle("Fantasy Cricket")
        save_msg.setText(msg)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        save_msg.setFont(font)
        save_msg.exec_()

    def open_team(self, team_total_points=0):
        name = dt.get_team_names()
        if not name:
            self.error_msg("No Previous Teams !!!!")
        else:
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.get_name_team()
            response = Dialog.exec_()
            if response == QtWidgets.QDialog.Accepted:
                self.salected_list.clear()
                team_name = ui.team_name()
                dt.get_selected_team(team_name)
                self.lineEdit.setText(team_name)
                self.refresh_points()
                self.maintain_points()
                self.bat_label.setText("4")
                self.now_label.setText("3")
                self.ar_label.setText("3")
                self.wk_label.setText("1")
                for i in dt.open_team_players:
                    team_total_points += i[1]
                    self.salected_list.addItem(str(i[0]))
                    if i[0] in dt.batsman:
                        dt.batsman.remove(str(i[0]))
                    if i[0] in dt.bowlers:
                        dt.bowlers.remove(str(i[0]))
                    if i[0] in dt.all_rounder:
                        dt.all_rounder.remove(str(i[0]))
                    if i[0] in dt.wicket_keeper:
                        dt.wicket_keeper.remove(str(i[0]))
                self.points_used_label.setText(str(team_total_points))
                remaining_points = 1000 - team_total_points
                self.point_available_lable.setText(str(remaining_points))
                self.save_message("You Can't Update Opened Team!!!!")


    def save_team(self):
        total_players = batsman_count + bowler_count + allrounder_count + wk_count

        team_name = self.lineEdit.text()
        if total_players == 11 and len(team_name) != 0:
            self.save_message("Team Saved Successfully!!!")
            dt.add_team_database(str(team_name))
        else:
            if len(team_name) == 0:
                self.error_msg("Please Enter Team Name!!!!")
            else:
                self.error_msg("Insufficient Players !!!!")
    def error_msg(self,msg):
        less_points = QMessageBox()
        less_points.setWindowTitle("Error")
        less_points.setText(msg)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        less_points.setFont(font)
        less_points.exec_()

    def refresh_points(self):
        global batsman_count, bowler_count, allrounder_count, wk_count, total_points, used_points
        batsman_count = 0
        bowler_count = 0
        allrounder_count = 0
        wk_count = 0
        total_points = 1000
        used_points = 0
        self.player_list.clear()
        self.salected_list.clear()
        dt.refresh_category_list()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fantasy_app_window = QtWidgets.QMainWindow()
    ui = Ui_Fantasy_app_window()
    ui.setupUi(Fantasy_app_window)
    Fantasy_app_window.show()
    sys.exit(app.exec_())
