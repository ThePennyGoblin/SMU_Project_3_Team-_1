# SMU_Project_3_Team-_1

# Production-Line Butcher - Quality Control

## Project Overview
- As the quality control team for an industrial butcher, we are tasked with determining:
    - Where our product lines are above 95% compliant to customer's specifications. 
    - Remove obvious errors in the data before serving to the client.
    - Use our tool to determine where outliers or offspec items might be explained by manual errors, camera-read errors, or non-production/operational issues
    - Provide suggestions where we should further clean data, add additional slicers for a dashboard, etc for better data-driven decision-making. 
    - Future proof the tool
    - Serve this live using AWS sources-- database AWS, and EDB.  

- These goals are met by: 
    - Interactive visualizations dashboard
        - Actions Page : provides a dynamic list of out of compliant products so stakeholders can focus on correction.
        - Overview Page : provides a dynamic table of each relevant metric, with action items (non-compliant) staged at the to for easy review. 
        - Products Page : provides side-by-side view of each metric, called dynamically by product in the left nav-bar. Vital statistics are called to further describe data.
  
    - Libraries and Tools not covered in class
        - plotly.express
        - plotly.io
        - flask_sqlalchemy
        - sqlalchemy.exc
        - https://bootswatch.com/5/slate/bootstrap.min.css
        - https://cdn.plot.ly/plotly-latest.min.js
        - AWS EBS
   
    - Data stored and extracted from database
        - Tools: 
            - AWS RDB
            - postgres
            - DBeaver
        - Files:
            -data_processing.py
            -data_cleaning.py
            -data_load.py
            -db_model.py
    - Group Presentation 


## Team Members
Abigail Parsley
Caite Green
Josh Still
Kevin Khan

## Tools and Technologies

- Excel (CSV)
- QuickDBD
- Pandas
- DBeaver
- Matplotlib
- Flask (API)
- OTHER PENDING

ools - CSV, PostgresSQL, Python(various libraries)
        - Stripped spaces and semi-colons, any N/A and errors.
        - Removed non-relevant data, like 
            -"test blocks"
            -Suspected water on the line -- lower outliers that didn't make sense for thickness (dropped entire rows)
            -Suspected manual entry errors (no decimal points) on weight that populated >50 lbs (multiplied by .01 to reset decimals)
            -
## Project Steps
1. Data Ingestion - Python pandas, CSV, Excel, postgresql, csv, dotenv
    - Function to take in CSV.
    - Function to clean & transform and add ID columns.

2. Data Loading - AWS RDB, DBeaver, postgresql, Python pandas, sqlalchemy, csv, dotenv
    - Function to create a new DB in our RDS DB.
    - Create a function to read our table script query to create the tables.
    - Function to load into the DB (test env is Dbeaver, production is AWS RDB)

3. Data Transformation - Python pandas, numpy, plotly.graphobjects, matplotlib, CSV, Excel
    - Initial testing direct from CSV, so that we can work independently from the database ingestion team. 
    - Data analysis -- understand data to create punch list to transform, used Excel as a test env, as well as Python. 
    - Create multiple plot models, use as a tool to further refine cleaning and data story. 
    - Added vertical mean, and upper/lower spec lines.  

4. Outlier and Error Handling -- Python pandas, numpy
    - Excluding all weights over 50 by multiplying by .01-- clear decimal placement error. These are likely just human error-- forgot decimals.  
    - Removing all rows with thickness < .05in. These are likely water on the line. 

5. User Experience -- Python pandas, flask, numpy, csv, plotly.js
    - Files : vital_stats.py, plot.py, db_operations.py
    - Functions to query the data from database
    - Functions to transform based on the above
     - Function to make a describe chart. 
        - weight
        - thickness
    
6. Data Serving : Python flask_sqlalchemy, pandas, numpy, csv
    Flask - app.py
        - Create end points to serve html files & data as APIs for client to read.
        - Integrate internal modules to transform the data.

7. Client Processing : flask_sqlalchemy, sqlalchemy, pandas, JavaScript, Bootstrap
    -HTML Files
        -Source bootstrap and place all elements as needed.
    -JS Files
        -Minimal JavaScript- used to fetch API endpoints and append to html

8. Debugging & Cleaning Up
    - Ensure everything works as intended. 
    - Clean up unneccessary files/folders comments, fix any code, typo, refactor variables etc. 

9. Deployment AWS EBS, GitHub CICD

## Conclusion and Ethical Considerations 
This tool is designed with internal stakeholders in mind.  It catches issues, serves those issue succintly, and provides the quality control team visibilty into what lines they need to review.

External stakeholders should not be served this view.  They should be provided a second data-cleaning step that normalizes more complex issues.  An example of these errors, is a finding where it looks like 12 oz steaks were accidentally coded as 6-oz. Unless the customer then had those packed in 12-oz boxes, these are not relevant to the quality of the product. 

The project discusses the real-world problem of determining what data is and is not relevant. It further explores who the audience is, what story the data tells, and how cleaning and transforming and visualizing that data skews what insights are served.  


## Future Work
Based on client requests and stakeholder.  

User Experience:
- The overall architecture works, so all we'd need to do is redefine Python functions and find places in the html.  
- Date/Time slicer
- Quarterly view, monthly, view, weekly, daily ingestion and view
- Outliers lists by product and date
- Interactive callout from the action page to the product page product (or plots within the action page)
- Password protect the website-- landing main page
- Different users could have different views (call different data)
- Transform data differently based on who the stakeholder is.  

Data + Reports:
- Send livelinks or emails when data is uploaded to the database
- Embed radio buttons to call/ download csv reports from the website based on data and product

## Learning Notes
Kevin Khan : Bootswatch makes life so much easier. Gives us a CSS format out of the box. 
Caite Green : There are a lot of team members with impressive skills.  Hire them. Look at this app. Also, learned a number of future-proofing and trouble-shooting methods like function-wrapping and creating safe errors so VSCode offers up suggestions. 
Abigail Presley : 
Saad Nasir : 
Josh Still : 

## Resources
    - Anonymized Dataset - original data sourced from industrial butcher production-line camera reader.  
    - Bootstrap https://bootswatch.com/5/slate/bootstrap.min.css
    - Plotly.js https://cdn.plot.ly/plotly-latest.min.js
    - And the intern... (ChatGPT 4.0)

