import json
from company import predictCompanyAttributes, setCompanyAttributes
from score import calculateApplicantScore

# Open data.json file
f = open('data.json')
# Load data.json
data = json.load(f)

# Split up team member and applicant data
team_members = data['team']             
applicants = data['applicants']         

team_totals = predictCompanyAttributes(team_members)

company_attributes = setCompanyAttributes(team_members, team_totals)
    
scores = calculateApplicantScore(applicants, company_attributes)

# Finalize output dict with applicant's scores
scored_applicants = {}
scored_applicants['scoredApplicants'] = scores

# Create and write to output.json file
with open('output.json', 'w') as outfile:
    json.dump(scored_applicants, outfile)

print("Thanks for the input! Your applicants have been scored and can be found in output.js")
