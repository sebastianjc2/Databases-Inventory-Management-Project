# Team Name: SQLytes

## Team Members

- Eithan Capella: eithan.capella@upr.edu
- Pedro Pagán: pedro.pagan6@upr.edu
- Sebastian Caballero: sebastian.caballero@upr.edu
- Sebastián Estrada: sebastian.estrada@upr.edu
- Yariel Mercado: yariel.mercado1@upr.edu

## Setting up a working environment 
1. Create your own virtual environment folder in the workspace where the program is going to reside. 
   This allows the project to localize the packages and versions instead of applying system-wide changes. 
   Use this as a general guide, as the setup varies based on OS. This is targeted towards macOS users.
      1. Run the following command: `python -m venv <.venv>`
         - `.venv` can be named anything.
         - The creation of your venv was successful if a `<.venv>` folder appears in your workspace and if `(<.venv>)` 
           appears at the beginning of your directory. Example: `(<.venv>) <username> <ProjectWorkspace>`
      2. Change your Python environment to the location of where your created venv resides.
      3. Run the following command to activate your venv `source <venv_name>/bin/activate`.
2. Install the libraries used in this project by running the following command inside your venv: 
   `pip install -r requirements.txt`
3. The required Python version for this is `Python 3.10.2` or newer. If your system-wide version of Python is older, 
   the venv can be configured to handle independent versions of Python.

If you're running this on PyCharm, it's worth knowing that PyCharm automatically sets this up for you and can also
auto-activate your venv each time the IDE is fired up. More info on how to configure this can be easily found online.

## Workflow Rules
1. **ALWAYS** make a new branch for your new changes. Never make changes on the main/master branch since this can 
   lead to trouble and result in the project being broken for everyone.
2. Write tests for every feature you are going to implement. 
3. Commit and push in small steps. If a change is working as expected, commit and push it to the current branch you are 
   working on. Do not make commits, push, or merge in where no more than 2 features or working changes have been 
   implemented. This allows us to easily traceback where the code broke starting from the last working commit or push.
4. Merge with main once all your changes in the branch you are making have been tested and are working.
5. Remember to update `requirements.txt` as new libraries are introduced.
6. Separate frontend and backend work into their own folders/workspaces. 
7. **ALWAYS** work in your venv so that if something goes wrong, your general packages aren't affected.
8. Follow Python best practices :snake:!
9. Remember to **set your line length to 120 characters** so that the source code can be consistently formatted, 
   regardless of screen size. 
10. Ensure that any IDE, venv, or compilation specific artifacts are listed under `.gitignore`.
