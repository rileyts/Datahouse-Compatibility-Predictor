# Datahouse-Compatibility-Predictor

## Language 
<p> This was written in Python 3. </p>

## How is Compatability Generated?
<p>The software takes input data by parsing through the file data.json.</p>

<p>An applicant’s compatibility score is a weighted average of all of their attributes. The weights are determined based on how much the company values these attributes. These numbers are divided by 10 to be on the range [0, 1].</p>

***Score = (attribute1 * weight1 + … + attributeN * weightN) / (weight1 +...+ weightN)***

<p>By averaging the attributes across all current team members, the software calculates a number between 1-10 representing how much the company values said attribute. These numbers are presented to the user and asks if the predicted numbers are an accurate representation of the candidates their company is looking to hire.</p>

<p>If they agree, the applicant’s score is calculated with the predicted values as the weights.</p>

<p>If they disagree, they are prompted to rate each attribute on a scale of 1-10. Their input is then used for scoring.</p>

<p>The results are written to the file output.JSON.</p>

## Instructions for use
<p> Once downloaded and unzipped, double clicking 'main.py' will run the software in the Python terminal</p>
<p> For better view of UI, run in Python IDLE </p>
