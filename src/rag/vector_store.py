from pymilvus import MilvusClient, DataType
from dotenv import load_dotenv
import os

load_dotenv()

client = MilvusClient(
    uri=os.getenv("CLUSTER_ENDPOINT"),
    token=os.getenv("MILVUS_TOKEN")
)

schema = MilvusClient.create_schema(
    auto_id = True,
    enable_dynamic_field = True,
)

schema.add_field(field_name="my_vector", datatype=DataType.FLOAT_VECTOR, dim=768)

index_params = client.prepare_index_params()

index_params.add_index(field_name="my_id")
index_params.add_index(
    field_name="my_vector",
    index_type="IVF_FLAT",
    metric_type="COSINE",
)

client.create_collection(
    collection_name="my_collection",
    schema=schema,
    index_params=index_params
)