# Returns: Dict of the average attributes across employees
# Parmaeters: Team member's data
# Description: Predicts how a company will value attributes based on people currently employed 
def predictCompanyAttributes(team_members_data) :
    # Initialize dict to store company attribute ratings based on current employees 
    team_totals = {}
    for t in team_members_data :
        for t_attr in t['attributes'] :
            team_totals[t_attr] = 0

    # Calculate company attribute ratings based on current employees
    for t in team_members_data :
        for attr in t['attributes'] :
            team_totals[attr] += t['attributes'][attr]  

    print("This is how your company values certain applicant attributes on a 1-10 scale")

    for x in team_totals:
        team_totals[x] = round( (team_totals[x] / len(team_members_data)), 1)
        print(x + ": " + str(team_totals[x]))    
    
    return team_totals


# Returns: Dict of how the company values applicant attibutes
# Parmaeters: Team member's data and Dict of the average attributes across employees
# Description: Will prompt user to chose between using the predicted company values or ones the user inputs
def setCompanyAttributes(team_members_data, team_totals) :
    # Initialize dict to store company attributes
    company_attributes = {}
    for c in team_members_data :
        for attr in c['attributes'] :
            company_attributes[attr] = -1

    # Prompt user for valid input
    answ = input("Do you agree? (y:yes, n:no) ")
    while not (answ == 'y' or answ == 'n') :
        print("Invalid Input: Please resound with 'y' or 'n'")
        answ = input("Are the ratings accurate to your company? (y:yes, n:no)")

    if answ == 'n' :
        # Prompt user to rate the importance of each attribute on a scale fom 1-10
        print("Please rate the importance of the following attriubutes to your company on a scale from 0-10 ")
        print("0: not relevant at all  10: crucial to this position")

        # Obtain user input for each attribute 
        for c_attr in company_attributes :
            while company_attributes[c_attr] < 0 or company_attributes[c_attr] > 10 :
                company_attributes[c_attr] = float(input(c_attr + ": "))
                if company_attributes[c_attr] < 0 or company_attributes[c_attr] > 10 :
                    print('Invalid Input: Please input a number between 0-10')

    elif answ == 'y' :
        for c_attr in company_attributes :
            company_attributes[c_attr] = team_totals[c_attr]
    
    return company_attributes