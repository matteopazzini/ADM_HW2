from collections import Counter
import datetime
import pandas as pd

start_time = datetime.datetime.now()

data_list = pd.read_json('/home/matt/ADM_HM2/list.json',lines=True,chunksize=200)
total_data_list = pd.DataFrame()
for chunk in data_list:  #drop columns that are not useful or that are redundant
    PARTIAL_DATA = chunk["tags"]
    total_data_list = pd.concat([total_data_list,PARTIAL_DATA])


new_counter = total_data_list.dropna()

list_counter = []
for element in new_counter[0]:
    list_counter.extend(element)
    
print(*Counter(list_counter).most_common(5),sep="\n")    

end_time = datetime.datetime.now()

time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000
print("Milliseconds elapsed for LOCAL_MACHINE:",round(execution_time,2),"ms")