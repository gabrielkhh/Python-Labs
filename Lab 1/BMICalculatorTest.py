import sys

try:
    unit = sys.argv[1]
    height = float(sys.argv[2])
    weight = float(sys.argv[3])

    if height > 0 and weight > 0:
        height_square = height * height
        BMI = None
        FinalBMI = None
        Description = None

        if unit == "metric":
            BMI = weight / height_square
        elif unit == "imperial":
            BMI = 703 * weight / height_square
        else:
            raise Exception()

        if BMI < 16:
            Description = "Severe Thinness"
        elif 16 <= BMI < 17:
            Description = "Moderate Thinness"
        elif 17 <= BMI < 18.5:
            Description = "Mild Thinness"
        elif 18.5 <= BMI < 25:
            Description = "Normal"
        elif 25 <= BMI < 30:
            Description = "Overweight"
        elif 30 <= BMI < 35:
            Description = "Obese Class I"
        elif 35 <= BMI <= 40:
            Description = "Obese Class II"
        elif BMI > 40:
            Description = "Obese Class III"

        print('%0.2f\t%s' % (BMI, str(Description)))
    else:
        raise Exception()



except:
    print('Your input is invalid!')
