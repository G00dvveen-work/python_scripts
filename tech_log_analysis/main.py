import event_parser as ep
import pandas as pd


call_log_dir = './files/logs/call'
excp_log_dir = './files/logs/excp'
output_dir = './files/output'

#calls = pd.read_csv(ep.parse_call(call_log_dir, output_dir))

exceptions = pd.read_csv(ep.parse_excp(excp_log_dir, output_dir))


#print(calls.head())
print(exceptions['context'].value_counts())