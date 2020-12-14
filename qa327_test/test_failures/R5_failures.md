# R5 Requirement Failures
These are the failures found and fixed on a specific branch for the R@ requirement.

Branch: **52_test**
- Issue with return statements from /update post function, it does not render the html correctly, resulting in server error
  - Fixed by rendering html correctly through passing all required arguments
- Issue with backend function to update a ticket, the code runs unnecessary db.session.update function
  - Fixed by removing that line of code so it'll update a ticket without error.