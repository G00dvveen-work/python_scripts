from .. import dragonfly as df


log_dir = '../files/logs/CALL'
output_dir = '../files/output'

calls = df.parse_call(log_dir, output_dir)