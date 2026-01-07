# feature/indexed list
#git add adds file to be staged
#git commit commits file to repository
# git diff shows changes before stage
#git diff --staged shows change in file after git add 
#git log --oneline --decorate: shows commit history,--oneline: shows everything in one line, -- decorate: shows which branch /ref point
#git branch : shows list of branches
#git checkout -b "branch_name": creates a new branch named "branch_name"
#git checkout master: goes to original branch
#git merge "branch_name": merges branch to master
#if you make a change to a file and save it and want to go back to the previous version: git restore day22.py
#if you do git add file to be staged by accident use: git restore --staged day22.py
#git remote -v: confirms origin is set correctly, -u sets upstream so future gut push works w/o extra args
#git remote add origin <git_url>: adds files to github repsository from remote source called origin
#git push -u origin master pushes remote source to master branch
# feature/indexed list

class JobApp:
    def __init__(self, company: str, role: str, date: str, status: str = "applied", notes: str = ""):
        self.company = company
        self.role = role
        self.date = date
        self.status = status
        self.notes = notes
    
    def update_status(self, new_status) -> bool:
        self.status = new_status
        return True

    def to_line(self):
        return self.company + "|" + self.role + "|"+ self.date + "|" + self.status + "|" + self.notes
    def __str__(self):
        return f"Applied to {self.company}, for the position: {self.role}, earliest start date: {self.date}, status = {self.status}, any additional notes: {self.notes}"

def main():
    apps = []
        
    while True:
        
        print("1) Add application")
        print("2) List applications")
        print("3) Update status")
        print("4) Save")
        print("5) Load")
        print("6) Quit\n")

        print("Enter choice: \n")
        try:
            choice = int(input())
        except ValueError:
            print("Please enter a number from 1-6")
            continue

        if choice == 1:
            print("Adding new job application")

            company = input("What company did you apply to ?").strip()
            role = input("What role was hiring at the company ?").strip()
            date = input("What's the earliest date you can start?").strip()
            notes = input("Anything you want to mention?").strip()

            apps.append(JobApp(company, role, date, notes=notes))
        elif choice == 2:
            count = 1
            for app in apps:

                print(f"{count}) {app}")
        elif choice == 3:
            if not apps:
                print("You need to add a job application before updating status\n")
                continue

            # print("What job would you like to update status for?")
            update = input("Please enter the company name: ")


            for app in apps:
                if update.lower() == app.company.lower():
                    while True:
                        print("What would you like to change the status to?")
                        status = input().strip().lower()
                        if status in ["applied", "denied", "interview", "offer"]:
                            app.status = status
                            print(f"Changed status to {app.status}")
                            break
                        else:
                            print("Not a valid status")
                            continue
                        
        elif choice ==4:
            output = input("Where would you like to save the job applications to?")
            count = 0
            with open(output, "w") as f:
                for app in apps:
                    f.write(f"{app.to_line()}\n")
                    count +=1
            print(f"Saved {count} apps")
        elif choice == 5:
            input_path = input("from where do you want to load your file ?")
            apps.clear()
            with open(input_path, "r") as f:
                for line in f:
                    if len(row) != 5:
                        continue
                    row = line.split("|")
                    company = row[0].strip()
                    role = row[1].strip()
                    date = row[2].strip()
                    status = row[3].strip()
                    notes = row[4].strip()

                    apps.append(JobApp(company, role, date, status, notes))
        elif choice == 6:
            print("See you next time")
            break



 


if __name__ == "__main__":
    main()

        