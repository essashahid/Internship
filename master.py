import os

'''
Refer to readme.txt for the way to enter the path.
'''


class WeatherReport:

    def __init__(self, year):
        self.year = year
        self.max_temp = None
        self.min_temp = None
        self.max_humidity = None
        self.min_humidity = None
        self.hottest_day = None

    def process_data_line(self, line):
        line = line.split(',')
        if len(line) >= 3:
            date = line[0]
            max_temp = int(line[1])
            min_temp = int(line[3])
            max_humidity = int(line[7])
            min_humidity = int(line[9])

            if not self.max_temp or max_temp > self.max_temp:
                self.max_temp = max_temp
                self.hottest_day = date

            if not self.min_temp or min_temp < self.min_temp:
                self.min_temp = min_temp

            if not self.max_humidity or max_humidity > self.max_humidity:
                self.max_humidity = max_humidity

            if not self.min_humidity or min_humidity < self.min_humidity:
                self.min_humidity = min_humidity

    def print_annual_report(self):

        if self.max_temp is not None and self.min_temp is not None and self.max_humidity is not None and self.min_humidity is not None:
            print(
                f"{self.year}\t\t{self.max_temp}\t\t{self.min_temp}\t\t{self.max_humidity}\t\t{self.min_humidity}")

    def print_hottest_day_report(self):

        if self.hottest_day is not None and self.max_temp is not None:
            print(f"{self.year}\t\t{self.hottest_day}\t\t{self.max_temp}")

    def print_format_annual(self):

        print("Year\t\tMAX Temp\tMIN Temp\tMAX Humidity\tMIN Humidity")
        print("--------------------------------------------------------------------------")

    def print_format_hottest_day(self):

        print("Year\t\tDate\t\tTemp")
        print("------------------------------------------")


def main():
    user_input = input("Enter weather data directory: ")
    if not os.path.exists(user_input):
        print("Invalid Path")
        return

    report_number = input(
        "Enter Report Number (1 for Annual Max/Min Temp, 2 for Hottest day of each year): ")

    reports = {}

    with open(user_input, 'r') as file:
        for line in file:
            if line.startswith("PKT"):
                continue
            year = line.split(',')[0].split('-')[0]
            if year not in reports:
                reports[year] = WeatherReport(year)
            reports[year].process_data_line(line)

    if report_number == '1':
        WeatherReport.print_format_annual(WeatherReport)
        [report.print_annual_report() for report in reports.values()]
    elif report_number == '2':
        WeatherReport.print_format_hottest_day(WeatherReport)
        [report.print_hottest_day_report() for report in reports.values()]
    else:
        print("Invalid Report Number")
        return


if __name__ == '__main__':
    main()
