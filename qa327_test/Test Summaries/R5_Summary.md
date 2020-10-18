| Specification                                                                                                            | Test case ID | Purpose                                                  |
|--------------------------------------------------------------------------------------------------------------------------|--------------|----------------------------------------------------------|
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. | R5.1.1       | Check failure for invalid name                           |
| The name of the ticket is no longer than 60 characters                                                                   | R5.2.1       | Check failure for ticket name greater than 60 characters |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                                        | R5.3.1       | Check failure for quantity of 0                          |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                                        | R5.3.2       | Check failure for quantity of 101                        |
| Price has to be of range [10, 100]                                                                                       | R5.4.1       | Check failure for range < 10                             |
| Price has to be of range [10, 100]                                                                                       | R5.4.2       | Check failure for range > 100                            |
| Date must be given in the format YYYYMMDD (e.g. 20200901)                                                                | R5.5.1       | Check failure for date in a different format             |
| Date must be given in the format YYYYMMDD (e.g. 20200901)                                                                | R5.5.2       | Check Success for date in correct format                 |
| The ticket of the given name must exist                                                                                  | R5.6.1       | Check failure for ticket name doesn't exist              |
| For any errors, redirect back to / and show an error message                                                             | R5.7.1       | This has been checked with tests R5.1.1-R5.6.1           |
