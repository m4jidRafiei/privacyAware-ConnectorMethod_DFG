'''
Created on Jul 2, 2019

@author: majid
'''

from PP.Utilities import Utilities
from pm4py.objects.log.importer.xes import factory as xes_importer_factory

connector_dataStructure_path = ".\intermediate_results\ConnectorStructure_Activity.csv"
export_intermediate_results = True #if you want to export the log with the perturbed activities

log = xes_importer_factory.apply("sample_log.xes")
    
utils = Utilities(log)
    
connectorBasic_DF, activityList = utils.create_basic_matrix_connector_activity(relation_depth = True, trace_length = True, trace_id = False)   

if(export_intermediate_results):
    connectorBasic_DF.to_csv(connector_dataStructure_path, sep=',', encoding='utf-8')
