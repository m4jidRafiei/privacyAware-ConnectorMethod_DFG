'''
@author: majid
'''

from p_connector_dfg.privacyPreserving import privacyPreserving

ela_path = ".\intermediate_results\ela_connector.xml"
ela_method = "Connector Method"
ela_desired_analyses = ['directly follows graph', 'process discovery']

activity_activity_matrix_path = r".\intermediate_results\test.csv"

dfg_path = "./DFG.svg"
freq_threshold = 0.0
# show_final_result = False

#Connector structure parameters--------------
relation_depth = True #if you want to have relation depth in the connector structure
trace_length = True # if you want to have trace length in the connector structure
trace_id = True # if you want to have a fake trace id in the connector structure

event_log = "sample_log.xes"
key = 'DEFPASSWORD12!!!'

pp = privacyPreserving(event_log)
pp.apply_privacyPreserving(key, ela_path, ela_method, ela_desired_analyses, event_log, relation_depth = relation_depth, trace_length = trace_length, trace_id = trace_id)

#directly call result maker---------------
# activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"
# pp.result_maker(True, True, True, False, 0.0, connector_dataStructure_path = connector_dataStructure_path, activity_activity_matrix_path = activity_activity_matrix_path, key = 'M4J!DPASSWORD!!!')

#directly call result maker using ela (Process Mining Abstraction)---------------
# activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"

pp.result_maker_ela(ela_path, True,True, True, freq_threshold, dfg_path, activity_activity_matrix_path = activity_activity_matrix_path,key = key)
