One day hopefully I will need to use a cap table

I used Streamlit because it's so calm for front-end work. (Fake) equity data is handled with names, share classes, and ownership percentages Pandas and stored in memory using st.session_state. 

The Dashboard provides a high-level overview of the cap table, displaying equity data in a table and visualizing ownership distribution with a pie chart. You can add new stakeholders by specifying details like share class and shares issued. The Simulate Funding Round page models the impact of issuing new shares on the cap table. Perhaps the most intricate feature is that it recalculates ownership percentages to account for dilution.

Didn't forget about Convertible Notes or SAFEs, which has it's own section on the sidebar if you want to try it out. The Employee Equity page manages employee stock grants with support for vesting schedules.

As good practice, there's a Timeline page that logs all equity-related events chronologically. Finally, the Export Cap Table page provides functionality to download the cap table as a CSV file for external use.

I got to learn a nice intro to VC by understanding the effects of funding rounds, tracking convertible notes and SAFEs, and understanding how dilution impacts stakeholders. 





