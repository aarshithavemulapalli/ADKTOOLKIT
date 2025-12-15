from google.adk.tools.openapi_tool import OpenAPIToolset, RestApiTool
import yaml
from pathlib import Path

# Load OpenAPI spec
spec_path = Path(__file__).parent.parent / "openapi" / "petstore.yaml"

with spec_path.open() as f:
    openapi_doc = yaml.safe_load(f)

# Create the toolset
toolset = OpenAPIToolset(spec_dict=openapi_doc)

# Since get_tools() is async, we'll create a function that returns the toolset
# and let the agent handle it, OR we can return the toolset itself
def get_petstore_tools():
    """Returns the OpenAPIToolset for lazy tool access."""
    return toolset

# For direct tool access, we'll need to process at agent runtime
petstore_toolset = toolset