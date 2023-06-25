#Sensor fault detection of a vehicle that uses compressed air to provide pressure to the break
### Problem Statement
```The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.
```
### Benifits : 
Correct prediction reduce the cost of unnecessary repair cost
### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### install pymongo
```
pip install pymongo
```
```
pip install pymongo[srv]
```


## Git commands

If you are starting a project and you want to use git in your project
```
git init
```
Note: This is going to initalize git in your source code.


OR

You can clone exiting github repo
```
git clone <github_url>
```
Note: Clone/ Downlaod github  repo in your system


Add your changes made in file to git stagging are
```
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to staging are


Create commits
```
git commit -m "message"
```

```
git push origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name 

To push your changes forcefully.
```
git push origin main -f
```


To pull  changes from github repo
```
git pull origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name

### Create .env file for urls
```
MONGO_DB_URL = ""
```

## github - connect to your repository
```
git init    # initialise git to your project
git remote add origin <githublink>
cd .git/
cd logs/
ls
cat HEAD/
cd remotes/
ls
cd origin
ls
cat main
cd.. # back to main dir
```
## git push command
```
git add .              # add for all files to staging area
git add <file_name>    # add a specific file 
git status             # To check the staging files 
git commit -m "comment about your commit"
git push origin main   # push files to origin main
git push origin main -f  #  push files forcefully to origin main 

```
### check which repository connected 
```
git remote -ve
git remote remote origin
git log    # history of commits
```
