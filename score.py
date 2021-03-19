# Returns: Dict of applicant's scores
# Parmaeters: Applicant's data
# Description: Calculates weighted sum of applicant's attributes based on how highly the company values the attribute
def calculateApplicantScore(applicants_data, company_attributes_data) :
    # Calculate the applicants score by averaging all their attributes weighted by company importance
    temp = {}
    scores = []
    for a in applicants_data :
        weighted_score = 0
        c_attr_sum = 0
        for a_attr in a['attributes'] :
            # Calculate weighted sum of all applicant's attributes
            weighted_score += (a['attributes'][a_attr] / 10) * (company_attributes_data[a_attr] / 10)
            c_attr_sum += company_attributes_data[a_attr] / 10
        # Average weighted attribute to find applicant score 
        weighted_score = weighted_score / c_attr_sum
        # Format scores into dict
        temp[a['name']] = round(weighted_score, 2)
        scores.append(temp)
        temp = {}

    return scores
