import dotenv
import os
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase
import datetime
import pandas as pd

# Load .env file
dotenv.load_dotenv(".env")

# Setup Dune Python client
dune = DuneClient.from_env()

query_id = 4607670 # full version
# query_id = 4591805 # short version

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# Query the query (execute and get latest result)
query = QueryBase(
    query_id=query_id
    # Uncomment and change the parameter values if needed
    # params=[
    #     QueryParameter.text_type(name="contract", value="0x6B175474E89094C44Da98b954EedeAC495271d0F"),  # default is DAI
    #     QueryParameter.text_type(name="owner", value="owner"),  # default using vitalik.eth's wallet
    # ],
)

query_result = dune.run_query_dataframe(
    query=query,
    # ping_frequency = 10 # Uncomment to change the seconds between checking execution status, default is 1 second
    # performance = "large" # Uncomment to change query run performance level, default is medium
    # batch_size = 5000 # Uncomment to change the maximum number of rows to retrieve per batch of results, default is 32,000
)

# Note: To get the result in CSV format, call run_query_csv()
# print(query_result)

query_result.to_csv(f'dune-query-result-{query_id}-{timestamp}.csv')
