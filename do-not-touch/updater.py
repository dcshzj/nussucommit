#!/usr/bin/python
# Script for updating the operating hours based on a list of pre-defined dates
# Triggered automatically everyday at 16:00 UTC by GitHub Actions

import datetime
import os

class Updater(object):
    def __init__(self):
        # This is because we are running at 16:00 UTC, which would be a new day
        self.dateToCheck = datetime.datetime.today() + datetime.timedelta(days=1)
        self.dateString = self.dateToCheck.strftime('%Y-%m-%d')
        self.pathToFile = "updater.csv"
        self.pathToConfig = os.environ["GITHUB_WORKSPACE"] + "/_config.yml"

    def compareDate(self, first, second):
        if (first == second):
            return True
        else:
            return False

    def updateHours(self, text):
        original = open(self.pathToConfig, "rt").read().splitlines()

        for i in range(0, len(original)):
            if (original[i].startswith("operating-type: ")):
                original[i] = "operating-type: " + text
                break

        newFile = open(self.pathToConfig, "wt").write("\n".join(original) + "\n")

    def main(self):
        listOfDates = open(self.pathToFile).read().splitlines()
        counter = 0

        for line in listOfDates:
            counter += 1
            if (counter == 1):
                continue

            lineArray = line.split(',')

            if not self.compareDate(self.dateString, lineArray[0]):
                continue

            self.updateHours(lineArray[1])

if __name__ == "__main__":
    Updater = Updater()
    Updater.main()
