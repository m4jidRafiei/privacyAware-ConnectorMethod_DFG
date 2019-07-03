'''
Created on Jul 3, 2019

@author: majid
'''

from PP.Utilities import Utilities
from pm4py.objects.log.importer.xes import factory as xes_importer_factory
import pandas as pd

class privacyPreserving(object):
    '''
    Applying privacy preserving technique and/or see the reults
    '''


    def __init__(self, log):
        '''
        Constructor
        '''
        self.log = log
    
    def apply_privacyPreserving(self, connector_dataStructure_path, show_final_result, **keyword_param):
        
        log = xes_importer_factory.apply("sample_log.xes")
        utils = Utilities(log)
        connectorBasic_DF, activityList = utils.create_basic_matrix_connector_activity(relation_depth = keyword_param['relation_depth'], trace_length = keyword_param['trace_length'], trace_id = keyword_param['trace_id'])   
        connectorBasic_DF.to_csv(connector_dataStructure_path, sep=',', encoding='utf-8')
        
    
        if(show_final_result):
            read_external_connector_ds = False
            connector_dataStructure_path = ".\intermediate_results\ConnectorStructure_Activity.csv"
            activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"
            export_ActActMatrix = True
            visualizeResult = True
            encryptedResult = False
            frequencyThreshold = 0.0
            
            self.result_maker(read_external_connector_ds, export_ActActMatrix, visualizeResult, encryptedResult, frequencyThreshold, 
                                                    connector_dataStructure_path = connector_dataStructure_path, activity_activity_matrix_path =activity_activity_matrix_path,
                                                    connector_ds = connectorBasic_DF)
            
            
            
    
    def result_maker(self, read_external_connector_ds, export_ActActMatrix, visualizeResult, encryptedResult, frequencyThreshold, **keyword_param):
        
        if(read_external_connector_ds):
            connector_dataStructure = keyword_param['connector_dataStructure_path']
            snBasic_DF = pd.read_csv(connector_dataStructure)
            snBasic_DF = snBasic_DF.iloc[:,1:]
        else:
            snBasic_DF = keyword_param['connector_ds']
        
       


        ActActMatrix, activityList = Utilities.makeDFG_connector(snBasic_DF, frequencyThreshold, encryption=encryptedResult, visualization=visualizeResult)

        ActActMatrix_pd = pd.DataFrame(ActActMatrix, index=activityList, columns=activityList)

        if(export_ActActMatrix):
            ActActMatrix_pd.to_csv(keyword_param['activity_activity_matrix_path'], sep=',', encoding='utf-8')  
            
            
            
            