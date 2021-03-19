# Returns: Dict of applicant's scores
# Parmaeters: Applicant's data
# Description: Calculates weighted average of applicant's attributes based on how highly the company values the attribute
def calculateApplicantScore(applicants_data, company_attributes_data) :
    # Calculate the applicants score by averaging all their attributes weighted by company importance
    temp = {}
    scores = []
    for a in applicants_data :
        avg = 0
        i = 0
        for a_attr in a['attributes'] :
            # Calculate weighted sum of all applicant's attributes
            avg += (a['attributes'][a_attr] / 10) * (company_attributes_data[a_attr] / 10)
            # Don't factor in an attribute the comapny rates as 0
            if company_attributes_data[a_attr] > 0 :
                i += 1
        # Average weighted attribute to find applicant score 
        avg = avg / i
        # Format scores into dict
        temp[a['name']] = round(avg, 2)
        scores.append(temp)
        temp = {}

    return scores
