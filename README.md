# Team Name: SQLytes

## Team Members

- Eithan Capella: eithan.capella@upr.edu
- Pedro Pagán: pedro.pagan6@upr.edu
- Sebastian Caballero: sebastian.caballero@upr.edu
- Sebastián Estrada: sebastian.estrada@upr.edu
- Yariel Mercado: yariel.mercado1@upr.edu

## How to run the program (To be updated as progress is achieved...)

1. Create your own virtual environment folder in the workspace where the program is going to reside. This is so that the project runs independently in your machine and it does not depend on the current libraries found locally in your machine and so that the libraries found in this project are not installed directly in your computer.
   - Before starting, make sure you are in the directory in which you are going to run the program. To create a virtual environment (venv) in your computer, do the following:
      1. Run the following command: `python -m venv .venv`
         - `.venv` can be any name you wish.
      2. If in VSCode, follow this step and stop. Else follow step 3:
         - Click the option that says if you want to use the newly created venv as your python interpreter. If you missed this, you can easily change this via the Python Interpreter selector in the Command Palette.
         - Reset or Create a new terminal after running the command above. The creation of your venv was successful if a `.venv` folder appears in your workspace and if `(.venv)` appears at the beginning of your directory. Example: `(.venv) username ProjectWorkspace`
      3. Change your Python Environment to the location of where your created venv resides.
        - Run the following command to acticate your venv`source venv_name/bin/activate`
      4. Now you are done with the creation of a venv.
2. Install the libraries used in this project by running the following command inside your venv: `pip install -r requirements.txt` 
3. Now you have all dependencies and libraries to run the program.

## Rules to make changes to the project and implement new features.
1. **ALWAYS** make a new branch for your new changes. Never do changes in the main/master branch since this can lead to trouble and result in the project being broken for everyone.
2. Make tests and test every feature you are going to implement before pushing and merging to main. This is so that the main branch is healthy and has the latest working changes.
3. Commit and push in small steps. If a change is working as expected, commit and push it to the current branch you are working on. Do not make commits, push or merge in where no more than 2 features or working changes have been implemented. This is so that we can save time when something breaks and we can easily traceback where the code broke starting from the last working commit or push.
4. Merge with main once all your changes in the branch you are making have been tested and are working.
5. Remember to update `requierements.txt` as new libraries are introduced to the program.
6. Separate frontend and backend work into their own folders/workspaces. This is to have better organization in the general workspace.
7. **ALWAYS** work in your venv so that if something goes wrong, your general packages in the computer do not get affected.
8. Follow best python and development practices :)

Feel Free to add more rules here for the team to follow :D
Remember that the important thing is have fun and learn (in addition to making a working project ofc).




