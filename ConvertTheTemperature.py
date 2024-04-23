class Solution(object):
    def convertTemperature(self, celsius):
        array=[]
        kelvin=celsius + 273.15
        fahrenheit = celsius *1.80 + 32.00
        array.append(kelvin)
        array.append(fahrenheit)
        return array
