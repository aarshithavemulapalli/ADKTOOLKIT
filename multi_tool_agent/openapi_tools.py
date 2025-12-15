from google.adk.tools.openapi_toolset import OpenAPIToolset

petstore_toolset = OpenAPIToolset.from_openapi_spec(
    spec_path="openapi/petstore.yaml"
)
