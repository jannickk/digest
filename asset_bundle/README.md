## DIGEST BUNDLE


As of writing this README.md, databricks asset bundles do not support variable substitution for the workspace.host field. 
Therefore, this field is ommitted as instead provided through the environment variable $DATABRICKS_HOST.
Hence, providing it using th var=<value> to the cli does not work.

## Deployment using databricks-cli

Make sure the $DATABRICKS_HOST environmental variable is set as stated in the previous section.
databricks auth login --host <workspace-url>

## Validate

databricks bundle validate --var="container=data" --var="path_to_monitor=folder" --var="existing_cluster_id=0129-072203-9ov97njk" --var="storage_account_name=senjkdtbxloader" --var="catalog=jk_libraries" --var="schema=dev_bundle"

## Deploy the bundle to a target 

databricks bundle deploy --var="storage_account_name=<value>" --var="container=<value>" --var="path_to_monitor=<value>" --var="existing_cluster_id=<value>" --var="storage_account_name=<value>" --var="catalog=<value>"
--var="schema=<value>" --config databricks-imperative.yml --target dev