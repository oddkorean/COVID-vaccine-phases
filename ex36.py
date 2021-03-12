from sys import exit
import webbrowser

def designate(phase):

    if phase == "":
        print("Based on the information provided, you are currently not eligible for a high priority phase.\n")

    else:
        print(f"Based on the information provided, you are designated as part of {phase}.\n")

def eligible(phase):
    if "1A" in phase:
        print("Phase 1A has the highest priority so you will be contacted shortly to schedule your vaccination. Please be at the vaccination site at least 10 minutes earlier.")

    elif "1B" in phase:
        print("Phase 1B has the second highest priority so you will be contacted after Phase 1A has been vaccinated. Please be at the vaccination site at least 10 minutes earlier.")

    elif "1C" in phase:
        print("Phase 1C has priority after Phase 1B so you will be contacted after Phase 1B has been vaccinated. Please be at the vaccination site at least 10 minutes earlier.")

    else:
        print("At this time there are not enough vaccines to designate your phase for vaccination. We will contact you when higher priority phases are all vaccinated.")



#second path about age
def age():
    phase = ""
    age = ""

    while type(age) != int: # need to compare type with type
        print("How old are you?")
        age = input(">")

        if age.isnumeric() is True:
            age = int(age)

            #print(f"age is {age} and {isinstance(age, int)}") #need to compare type with type. I thought I was comparing variable value with type.

        else:
            print("Please enter a valid number.")

    if age > 100:
        print("Congratulations on living so long.")
        age = int(age)
        phase = "Phase 1B"

    elif 75 >= age >= 65:
        phase = "Phase 1C"

    elif 64 >= age >= 16:
        print("Do you have any underlying medical conditions that would designate you at high-risk for COVID? Ex. Obesity, Morbid obesity, DM II, COPD, CAD, CKD, ICH, sickle cell, smoking, etc.")
        risk = ""
        phase = risk_path(risk) #need to change global variable by returning new value in function and equalling that value to global variable

    elif age > 75:
        phase = "Phase 1B"

    elif age < 13:
        print("Congratulations for being alive on this world up until now! You have had at most a 0.01% chance of being unalive at this point. ")

    else:
        phase = ""

    #print(f"this is the phase: {phase}")
    designate(phase)
    eligible(phase)

#pathway asking about underlying medical conditions contributing to risk
def risk_path(risk):
    risk = input(">")
    if "yes" in risk:
        phase = "Phase 1C"
        #print(f'this is the phase inside the risk path: {phase}')
        return phase

    elif "no" in risk:
        phase = ""
        #print(f"this is the phase inside the 'NO' path: {phase}")
        return phase

    else:
        print("Please enter a valid answer.")
        return risk_path(risk)


#start of the path
def healthcare():
    print("Are you a healthcare worker? Ex. nurse, physician, EMT, etc.")
    healthcare_status = input(">")

    if "yes" in healthcare_status:
        phase = "Phase 1A"
        designate(phase)
        eligible(phase)

    elif "no" in healthcare_status:
        age()

    else:
        print("Please refer to the CDC website to determine your occupational status and restart the form.")
        webbrowser.open("https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/hcp.html")


healthcare()

