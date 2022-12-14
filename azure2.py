#creation of workspace 
from azureml.core import Workspace
ws = Workspace.create(name=" ",
subscription_id='',
resource_group='',
create_resource_group = True,
location=''  )


#connectiong the workspace (this method is used when we download a json file from azure ml workspace so that we can metion file name)
from azureml.core import workspace
ws = workspace.from_config()

# generally preferd configuration file is by get method 
from azureml.core import workspace
ws = workspace.get(
    name = "",
    subscription_id = "",
    resource_group = ""
)

#usage of compute targets for running experment
for compute_name in  ws.compute_targets:
    compute  = ws.compute_targets['target-name']
    print(compute.name," : ",compute.type)




#creation of experiment
from azureml.core import Experiment 
experiment = Experiment(workspace='',name='')
#running the experiment
run = experiment.start_logging()
 
 #experiment code is written here
  

# completion of the experiment
run.complete()

# logging functions for experiments
# 1. log("records single name value")
# 2.log_list("records names list of values")
# 3.log_row("records row with multiple columns")
# 4.log_table("recors dictonary as a table")
# 5.log_image("records image file ")


# running a code which says the number of observations or length of rows in an experiment
from azureml.core import Experiment 
experiment = Experiment(workspace='',name='')
#running the experiment
run = experiment.start_logging()

# loading the data set and counting the no.of rows
data = pd.read_csv('data.csv')
row_count = (len(data))

#logging the output
run.log('observations',row_count)

#ending the file 
run.complete()

#to upload the output in the separate folder

run.upload_file(name = " ",path_or_stream = " ")


# Importing all libraries needed
 
import azureml.core 
import Run
import pandas as pd 
import matplotlib.pyplot as plt
import os 

# to access the experiment run context
run = Run.get_context()



