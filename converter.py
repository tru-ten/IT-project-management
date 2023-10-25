class NumberToWordsConverter:
    def __init__(self):
        self.units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        self.tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def convert_to_words(self, number):
        if 0 <= number < 10:
            return self.units[number]
        elif 10 <= number < 20:
            return self.teens[number - 10]
        elif 20 <= number < 100:
            return self.tens[number // 10] + (" " + self.units[number % 10] if number % 10 > 0 else "")
