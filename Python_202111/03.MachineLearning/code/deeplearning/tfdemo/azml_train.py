#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'demo'))
	print(os.getcwd())
except:
	pass

#%%
import azureml.core
print(azureml.core.VERSION)


#%%
import azureml.core
from azureml.core import Workspace, Datastore

ws = Workspace.from_config()


#%%
ds = ws.get_default_datastore()


#%%
datastores = ws.datastores
for name, ds in datastores.items():
    print(name, ds.datastore_type)


#%%
import azureml.data
from azureml.data.azure_storage_datastore import AzureFileDatastore, AzureBlobDatastore

ds.upload(src_dir='./resized_dataset',
          target_path='resized_dataset',
          overwrite=True,
          show_progress=True)


#%%
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

cpu_cluster_name = "cpucluster"

# Verify that cluster does not exist already
try:
    cpu_cluster = ComputeTarget(workspace=ws, name=cpu_cluster_name)
    print('Found existing cluster, use it.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2',
                                                           max_nodes=4)
    cpu_cluster = ComputeTarget.create(ws, cpu_cluster_name, compute_config)

cpu_cluster.wait_for_completion(show_output=True)


#%%
from azureml.core import Experiment
experiment_name = 'demo_experiment'

exp = Experiment(workspace=ws, name=experiment_name)


#%%
from azureml.train.estimator import Estimator

script_params = {
    '--data-folder': ds.as_mount()
}

keras_est = Estimator(source_directory='./',
                   script_params=script_params,
                   compute_target='cpucluster',
                   entry_script='train.py',
                   conda_packages=['keras','tensorflow','matplotlib','scikit-learn','pillow'])


#%%
run = exp.submit(keras_est)
print(run.get_portal_url())

run.wait_for_completion(show_output = True)


#%%
from azureml.widgets import RunDetails
RunDetails(run).show()


#%%
print(run.get_file_names())


#%%
model = run.register_model(model_name='starwar_model', model_path='starwar_model.h5')
print(model.name, model.id, model.version, sep = '\t')


#%%



