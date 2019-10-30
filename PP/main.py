'''
@author: majid
'''

from PP.privacyPreserving import privacyPreserving

pma_path = ".\intermediate_results\pma_connector.xml"
# show_final_result = False

#Connector structure parameters--------------
relation_depth = True #if you want to have relation depth in the connector structure
trace_length = True # if you want to have trace length in the connector structure
trace_id = True # if you want to have a fake trace id in the connector structure

event_log = "sample_log.xes"

pp = privacyPreserving(event_log)
pp.apply_privacyPreserving(pma_path, event_log, relation_depth = relation_depth, trace_length = trace_length, trace_id = trace_id)

#directly call result maker---------------
# activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"
# pp.result_maker(True, True, True, False, 0.0, connector_dataStructure_path = connector_dataStructure_path, activity_activity_matrix_path = activity_activity_matrix_path)

#directly call result maker using PMA (Process Mining Abstraction)---------------
activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"
pp.result_maker_pma(pma_path, False,True, True, 0.0, activity_activity_matrix_path = activity_activity_matrix_path)
