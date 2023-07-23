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
        returnString = self.commuteName + '\n'
        returnString += 'Total hours per week: {0:.2f} '.format(self.totalTimePerWeekHours) + '\n'
        returnString += 'Total Cost per day: ${0:.2f} '.format(self.totalCostPerWeek/7) + '\n'
        returnString +='Total Cost per month: ${0:.2f} '.format(self.totalCostPerWeek*4) + '\n'
        return returnString



#   Main function
def main():

    # Fuel economies of different cars
    carFunFuelEconomy = 22
    carEfficientFuelEconomy = 34

    # Cost of gas
    costOfRegular = 3.75
    costOfPremium = 4.00

    #   Create the commute scenarios
    baseLine = Commute(commuteName= 'Baseline Close Commute', 
                    oneWayTripMiles= 20, 
                    oneWayTripTimeMinutes= 21, 
                    carFuelEconomyMPG= carFunFuelEconomy, 
                    gasCostPerGallon= costOfPremium, 
                    tripsPerWeek= 1)

    print(baseLine)

    farCommuteFastCar_3Days = Commute(commuteName= 'Far - Fast Car - 3 Days', 
                                        oneWayTripMiles= 44, 
                                        oneWayTripTimeMinutes= 45, 
                                        carFuelEconomyMPG= carFunFuelEconomy, 
                                        gasCostPerGallon= costOfPremium, 
                                        tripsPerWeek= 3)

    print(farCommuteFastCar_3Days)

    far_EfficientCar_3Days = Commute(commuteName= 'Far - Hybrid - 3 Days', 
                                                oneWayTripMiles= 44, 
                                                oneWayTripTimeMinutes= 45, 
                                                carFuelEconomyMPG= carEfficientFuelEconomy, 
                                                gasCostPerGallon= costOfRegular, 
                                                tripsPerWeek= 3)
    
    print(far_EfficientCar_3Days)



if (__name__ == "__main__"):
    main()


