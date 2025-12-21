## DIGEST BUNDLE


As of writing this README.md, databricks asset bundles do not support variable substitution for the workspace.host field. 
Therefore, this field is ommitted as instead provided through the environment variable $DATABRICKS_HOST.
Hence, providing it using th var=<value> to the cli does not work.

## Deployment using databricks-cli

Make sure the $DATABRICKS_HOST environmental variable is set as stated in the previous section.
databricks auth login --host <workspace-url>

## Validate

databricks bundle validate --var="storage_account_name=<value>" --var="container=<value>" --var="path_to_monitor=<value>" --var="existing_cluster_id=<value>"--var="catalog=<value>"
--var="schema=<value>"

## Deploy the bundle to a target 

databricks bundle deploy --var="storage_account_name=<value>" --var="container=<value>" --var="path_to_monitor=<value>" --var="existing_cluster_id=<value>"--var="catalog=<value>"
--var="schema=<value>" --target dev