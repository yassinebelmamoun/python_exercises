import re

class Converter(object):
    # The pattern to valide the string input
    # HH:MM:SS(am, AM, pm or PM)
    pattern = "([0-1][0-2]|0[1-9]|[1-9]):([0-5][0-9]):([0-5][0-9])(am|pm|AM|PM)"

    def __init__(self, string_time):
        # Check if the input is correct by calling the static method: validate
        self.string_time_input = Converter.validate(self.pattern, string_time)

        # If no validation error is raised, get Hour, Minute, Second and period (AM or PM)
        self.hour = re.match(self.pattern, string_time).group(1) 
        self.minute = re.match(self.pattern, string_time).group(2)
        self.second = re.match(self.pattern, string_time).group(3)
        self.period = re.match(self.pattern, string_time).group(4)

    @staticmethod
    def validate(pattern, string_time):    
        if isinstance(string_time, str):
            if re.match(pattern, string_time):
                return string_time
            else:
                raise ValueError("The input doesn't follow the pattern")
        else:
            raise TypeError("The input must be a String")

    def get_military_time(self):
        print("The Time (Input) is : ", self.string_time_input)
        string_time_output = self.compile_military_time()
        print("The Military Time is :", string_time_output)

    def compile_military_time(self):
        # Special case : MIDNIGHT
        if self.string_time_input == '12:00:00AM':
            return '00:00:00'
        # Special case : NOON
        elif self.string_time_input == '12:00:00PM':
            return '12:00:00'
        # AM period case
        elif self.period == 'AM':
            return self.hour + ':' + self.minute + ':' + self.second
        # PM period case
        else:
            return str(12 + int(self.hour)) + ':' + self.minute + ':' + self.second


if __name__ == '__main__':
    # Create the instance
    converter_object = Converter(string_time = "11:59:59pm")
    # Call the method "get_military_time" for the instance created
    converter_object.get_military_time()
