#reading in unstructured data like pdfs
import os
from llama_index.core import (
    StorageContext,
    SimpleDirectoryReader,
    VectorStoreIndex,
    download_loader,
    RAKEKeywordTableIndex,
    load_index_from_storage
)

#not useful now but maybe useful for later...
def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir = index_name)
    else: 
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))
    
    return index



files = ["EFGTA", "eogt", "GameFamily", "thesis"]
paths = []
for i in range(4):
    pdf_name = os.path.join("data", files[i]+".pdf")
    paths.append(pdf_name)
    
reader = SimpleDirectoryReader(input_files=paths)
data = reader.load_data()
index = VectorStoreIndex.from_documents(data)
pdf_query_engine = index.as_query_engine()




