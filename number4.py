from_unit  = input("Convert from? ")
to_unit    = input("Convert to? ")
value_unit      = float(input("Value? "))

def gal_to_ml(gal):
    result = value_unit * 3785.41
    print(result,'ml')


if from_unit == "gal" and to_unit == "ml":
    gal_to_ml(from_unit)

elif from_unit == "gal" and to_unit == "km":
    print("Incompatible conversion")

else:
    print("Invalid unit entered!!")
