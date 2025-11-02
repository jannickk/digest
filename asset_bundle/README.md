# main_bundle

As of writing this README.md, databricks asset bundles do not support variable substitution for the workspace.host field.
Therefore, this field is ommitted as instead provided through the environment variable $DATABRICKS_HOST



# Deployment using databricks-cli

Make sure the $DATABRICKS_HOST environmental variable is set as stated in the previous section.

# Validate

databricks bundle validate --var="storage_account_name==<THE STORAGE ACCOUNT NAME>" --var="container=<THE CONTAINER IN THE STORAGE ACCOUNT WHERE NEW FILES WILL BE DEPOSITED>" --var="path_to_monitor=<THE PATH INSIDE THE CONTAINER TO MONITORING FOR NEW FILES>" --var="existing_cluster_id=<YOUR EXISTING CLUSTER ID>"



