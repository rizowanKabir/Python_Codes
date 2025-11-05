import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QMessageBox, QHBoxLayout, QRadioButton, QButtonGroup
)
from PyQt5.QtGui import QFont
import json


class VotingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Election Voting System")
        self.setGeometry(200, 100, 500, 400)

        # Candidate data
        self.candidates = {"Alice": 0, "Bob": 0, "Charlie": 0}
        self.voters = set()  # to track who already voted

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("🗳 Welcome to Voting System")
        title.setFont(QFont("Arial", 16))
        layout.addWidget(title)

        # Voter name input
        self.voter_input = QLineEdit()
        self.voter_input.setPlaceholderText("Enter your voter name")
        layout.addWidget(self.voter_input)

        # Candidate selection
        self.radio_group = QButtonGroup(self)
        self.radio_buttons = []
        for name in self.candidates.keys():
            rb = QRadioButton(name)
            self.radio_group.addButton(rb)
            layout.addWidget(rb)
            self.radio_buttons.append(rb)

        # Vote button
        vote_btn = QPushButton("Vote ✅")
        vote_btn.clicked.connect(self.cast_vote)
        layout.addWidget(vote_btn)

        # Result button
        result_btn = QPushButton("Show Results 📊")
        result_btn.clicked.connect(self.show_results)
        layout.addWidget(result_btn)

        self.setLayout(layout)

    def cast_vote(self):
        voter_name = self.voter_input.text().strip()

        if not voter_name:
            QMessageBox.warning(self, "Error", "Please enter your name!")
            return

        if voter_name in self.voters:
            QMessageBox.warning(self, "Error", "You already voted!")
            return

        selected = None
        for rb in self.radio_buttons:
            if rb.isChecked():
                selected = rb.text()
                break

        if not selected:
            QMessageBox.warning(self, "Error", "Please select a candidate!")
            return

        # Record vote
        self.candidates[selected] += 1
        self.voters.add(voter_name)

        # Save data to file (persistence)
        with open("votes.json", "w") as f:
            json.dump(self.candidates, f)

        QMessageBox.information(self, "Success", f"Thank you {voter_name}, your vote for {selected} is recorded!")

    def show_results(self):
        results = "\n".join([f"{c}: {v} votes" for c, v in self.candidates.items()])
        winner = max(self.candidates, key=self.candidates.get)
        QMessageBox.information(self, "Results", f"📊 Voting Results:\n\n{results}\n\n🏆 Winner: {winner}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec_())
