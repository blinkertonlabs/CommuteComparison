#   Blinkerton Labs
#   The intent of this Python script is to learn about classes
#   and complete a what-if analysis that compares different commutes
#   based on a number of different factors.  This is really just an
#   excuse to learn more Python with a particular goal in mind.





class Commute:
    def __init__(self, 
           commuteName,
           oneWayTripMiles,
           oneWayTripTimeMinutes,
           carFuelEconomyMPG,
           gasCostPerGallon,
           tripsPerWeek):
        self.commuteName = commuteName
        self.oneWayTripMiles = oneWayTripMiles
        self.oneWatTripTimeMinutes = oneWayTripTimeMinutes
        self.carFuelEconomyMPG = carFuelEconomyMPG
        self.gasCostPerGallon = gasCostPerGallon
        self.tripsPerWeek = tripsPerWeek
    
        #   Other parameters that are calculated automatically
        self.costPerTrip = ((self.oneWayTripMiles * 2) / self.carFuelEconomyMPG) * self.gasCostPerGallon
        
        #   Weekly totals
        self.totalCostPerWeek = self.costPerTrip * self.tripsPerWeek
        self.totalMilesPerWeek = (self.oneWayTripMiles * 2) * self.tripsPerWeek
        self.totalTimePerWeekHours = ((self.oneWatTripTimeMinutes * 2) / 60) * self.tripsPerWeek

        #   Annual Totals
        self.totalCostPerYear = 52 * self.totalCostPerWeek
        self.totalMilesPerYear = 52 * self.totalMilesPerWeek
        self.totalTimePerYearDays = (52 * self.totalTimePerWeekHours) / 24

    def __str__(self):
        return 'Total Cost per week: ' + str(self.totalCostPerWeek)



#   Main function
def main():

    #   Create the commute scenarios

    baseLine = Commute(commuteName= 'Baseline Eaton Commute', 
                    oneWayTripMiles= 20, 
                    oneWayTripTimeMinutes= 21, 
                    carFuelEconomyMPG= 22, 
                    gasCostPerGallon= 4.00, 
                    tripsPerWeek= 1)

    print(baseLine)



if (__name__ == "__main__"):
    main()


