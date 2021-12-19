

from PyQt5 import QtCore, QtGui, QtWidgets
import data as dt
strike_rate_points = 0
economy_rate_points = 0
total_team_score = 0
class Ui_Evaluate_team(object):
    def setupUi(self, Evaluate_team):
        Evaluate_team.setObjectName("Evaluate_team")
        Evaluate_team.resize(657, 647)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        Evaluate_team.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Evaluate_team)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 41, 561, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(46, -1, 38, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose_team = QtWidgets.QLabel(self.layoutWidget)
        self.choose_team.setObjectName("choose_team")
        self.horizontalLayout.addWidget(self.choose_team)
        self.comboBox_team = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_team.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_team.setObjectName("comboBox_team")
        self.horizontalLayout.addWidget(self.comboBox_team)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.choose_match = QtWidgets.QLabel(self.layoutWidget)
        self.choose_match.setObjectName("choose_match")
        self.horizontalLayout.addWidget(self.choose_match)
        self.comboBox_match = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_match.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_match.setObjectName("comboBox_match")
        self.horizontalLayout.addWidget(self.comboBox_match)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horinzon_labels = QtWidgets.QHBoxLayout()
        self.horinzon_labels.setContentsMargins(85, -1, 111, -1)
        self.horinzon_labels.setObjectName("horinzon_labels")
        self.players = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.players.setFont(font)
        self.players.setObjectName("players")
        self.horinzon_labels.addWidget(self.players)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horinzon_labels.addItem(spacerItem2)
        self.score = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.horinzon_labels.addWidget(self.score)
        self.verticalLayout.addLayout(self.horinzon_labels)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.player_list = QtWidgets.QListWidget(self.layoutWidget)
        self.player_list.setObjectName("player_list")
        self.horizontalLayout_3.addWidget(self.player_list)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.score_list = QtWidgets.QListWidget(self.layoutWidget)
        self.score_list.setObjectName("score_list")
        self.horizontalLayout_3.addWidget(self.score_list)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(82, -1, 80, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.calculate = QtWidgets.QPushButton(self.layoutWidget)
        self.calculate.setObjectName("calculate")
        self.horizontalLayout_2.addWidget(self.calculate)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 25)
        self.verticalLayout.setStretch(4, 2)
        self.frame = QtWidgets.QFrame(Evaluate_team)
        self.frame.setGeometry(QtCore.QRect(30, 20, 601, 601))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:#f0efef;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 601, 81))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:#ddeedd;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.frame.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(Evaluate_team)
        self.calculate.clicked.connect(self.display_team)
    def retranslateUi(self, Evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        Evaluate_team.setWindowTitle(_translate("Evaluate_team", "Evalute Team"))
        self.choose_team.setText(_translate("Evaluate_team", "Choose Team"))
        self.choose_match.setText(_translate("Evaluate_team", "Choose Match"))
        self.players.setText(_translate("Evaluate_team", "Players"))
        self.score.setText(_translate("Evaluate_team", "Score"))
        self.calculate.setText(_translate("Evaluate_team", "Calculate"))
        self.label.setText(_translate("Evaluate_team", "                  "))

    def team_list(self):
        names = dt.get_team_names()
        self.comboBox_team.addItems(names)

    def match_list(self):
        dt.get_match_list()
        self.comboBox_match.addItems(dt.match_list)

    def display_team(self):
        global total_team_score
        dt.final_team_with_points.clear()
        self.player_list.clear()
        self.score_list.clear()
        dt.selected_player_data.clear()
        dt.get_selected_team(str(self.comboBox_team.currentText()))
        for i in dt.open_team_players:
            if i[0] in dt.current_match_data:
                dt.selected_player_data[i[0]] = dt.current_match_data[i[0]]
        self.calculate_points()
        for i in dt.final_team_with_points:
            self.player_list.addItem(i)
            self.score_list.addItem(str(dt.final_team_with_points[i]))
        self.label.setText(str(total_team_score))
        total_team_score=0

    def calculate_points(self):
        global strike_rate_points, economy_rate_points, total_team_score
        for i in dt.selected_player_data:
            ## Scored runs points
            self.refresh_points()
            runs_points = dt.selected_player_data[i]["Scored"]//2
            if dt.selected_player_data[i]["Scored"]%50:
                runs_points+=5
            if dt.selected_player_data[i]["Scored"]%100:
                runs_points+=10

            #
            # ## strike rate points

            if dt.selected_player_data[i]["Scored"]>0:
                strike_rate = dt.selected_player_data[i]["Scored"]/dt.selected_player_data[i]["Faced"] * 100
                if strike_rate>=80 and strike_rate<=100:
                    strike_rate_points += 2
                if strike_rate >= 100:
                    strike_rate_points += 6

            ##fours points
            fours_point = dt.selected_player_data[i]["Fours"]

            ##six points
            six_point = dt.selected_player_data[i]["Sixes"] *2

            ##wicket points
            wicket_points = dt.selected_player_data[i]["Wkts"]*10
            if dt.selected_player_data[i]["Wkts"] >= 3:
                wicket_points += 5
            if dt.selected_player_data[i]["Wkts"] >= 5:
                wicket_points+=15

            # economy rate points
            over = dt.selected_player_data[i]["Bowled"]/6
            if over > 0:
                economy_rate = dt.selected_player_data[i]["Given"]/over
                if economy_rate>3.5 and economy_rate<=4.5:
                    economy_rate_points += 4
                if economy_rate>2 and economy_rate<=3.5:
                    economy_rate_points += 7
                if economy_rate <=2:
                    economy_rate_points += 10


            #stumping points
            stumping_points = dt.selected_player_data[i]["Stumping"]*10

            #runout points
            runout_points = dt.selected_player_data[i]["RO"] * 10

            #catching points
            catching_points = dt.selected_player_data[i]["Catches"] * 10
            total_points = runs_points + strike_rate_points + fours_point + six_point + wicket_points + economy_rate_points + stumping_points + runout_points + catching_points
            dt.final_team_with_points[f"{i}"] = total_points
            total_team_score += total_points

    def refresh_points(self):
        global strike_rate_points,economy_rate_points, total_team_score
        strike_rate_points = 0
        economy_rate_points = 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaluate_team = QtWidgets.QDialog()
    ui = Ui_Evaluate_team()
    ui.setupUi(Evaluate_team)
    ui.team_list()
    ui.match_list()
    Evaluate_team.show()
    sys.exit(app.exec_())
