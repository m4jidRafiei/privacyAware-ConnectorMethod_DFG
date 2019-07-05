'''
@author: majid
'''

from PP.Utilities import Utilities
from pm4py.objects.log.importer.xes import factory as xes_importer_factory
from PP.privacyPreserving import privacyPreserving
import pandas as pd


connector_dataStructure_path = ".\intermediate_results\ConnectorStructure_Activity.csv"
show_final_result = True


#Connector structure parameters
relation_depth = True #if you want to have relation depth in the connector structure
trace_length = True # if you want to have trace length in the connector structure
trace_id = True # if you want to have a fake trace id in the connector structure


event_log = "sample_log.xes"

pp = privacyPreserving(event_log)

pp.apply_privacyPreserving(connector_dataStructure_path, show_final_result, relation_depth = relation_depth, trace_length = trace_length, trace_id = trace_id)


#directly call result maker---------------
# activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"
# pp.result_maker(True, True, True, False, 0.0, connector_dataStructure_path = connector_dataStructure_path, activity_activity_matrix_path = activity_activity_matrix_path)



