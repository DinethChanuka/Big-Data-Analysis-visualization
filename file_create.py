import os
#Directories Creation and write content of files 

project_folder = "/content/data_pipeline_lab"
project_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_pipeline_lab")

requirements_path = project_folder + "/requirements.txt"

requirements = """
prefect
pandas
requests
pandera
pyarrow
"""
pipeline_path = project_folder + "/pipeline.py"
os.makedirs(project_folder, exist_ok=True)
os.makedirs(project_folder + "/data", exist_ok=True)
with open(requirements_path, "w") as f:
    f.write(requirements)
with open(pipeline_path, "w") as f:
    f.write("# This is the main pipeline file\n")

# Create the project folder and subfolders

if os.path.exists(project_folder):
    os.makedirs(project_folder + "/data", exist_ok=True)
    print("Project Folder Created Sucessfully")
else:
    print("Project Folder Creation Failed")

#requirements.txt file creation



if os.path.exists(requirements_path):
    with open(requirements_path, "w") as f:
        f.write(requirements)
    print("Requirements File Created Sucessfully")
else:
    print("Requirements File Creation Failed")

#pipeline.py file creation



if os.path.exists(pipeline_path):
    with open(pipeline_path, "w") as f:
         f.write("# This is the main pipeline file\n")
    print("Pipeline File Created Sucessfully")
else:
    print("Pipeline File Creation Failed")

# Check the created files and directories

for root ,dirs, files in os.walk(project_folder):
    level = root.replace(project_folder, '').count(os.sep)

    indent = " " * level

    for filr in files:
        print(indent+"---"+filr)