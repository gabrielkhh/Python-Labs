import sys

try:
    hours = float(sys.argv[1])
    normalRate = float(sys.argv[2])
    overtimeRate = float(sys.argv[3])

    normalSalary = None
    extraSalary = None
    totalSalary = None

    # Make sure that the rate is not of an unrealistic value
    if normalRate > 0 and overtimeRate >= 0:
        # Check if overtime has been hit
        if 0 <= hours <= 40:
            # Not overtime
            normalSalary = normalRate * hours
            extraSalary = 0.00
            totalSalary = normalSalary
        elif 40 < hours <= 168:
            # Overtime
            normalSalary = normalRate * 40
            extraSalary = (hours - 40) * overtimeRate
            totalSalary = normalSalary + extraSalary
        else:
            raise Exception()
    else:
        raise Exception()

    print('Normal Salary:%0.2f, Extra Salary:%0.2f, Total Salary:%0.2f' % (normalSalary, extraSalary, totalSalary))

except:
    print('Your input is invalid!')