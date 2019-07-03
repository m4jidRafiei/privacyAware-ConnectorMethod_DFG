'''
Created on Jul 1, 2019

@author: majid
'''

from PP.Utilities import Utilities
import pandas as pd


connector_dataStructure_path = ".\intermediate_results\ConnectorStructure_Activity.csv"
activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"
export_ActActMatrix = True
visualizeResult = True
encryptedResult = False
frequencyThreshold = 0.2


snBasic_DF = pd.read_csv(connector_dataStructure_path)
snBasic_DF = snBasic_DF.iloc[:,1:]


ActActMatrix, activityList = Utilities.makeDFG_connector(snBasic_DF, frequencyThreshold, encryption=encryptedResult, visualization=visualizeResult)

ActActMatrix_pd = pd.DataFrame(ActActMatrix, index=activityList, columns=activityList)

if(export_ActActMatrix):
    ActActMatrix_pd.to_csv(activity_activity_matrix_path, sep=',', encoding='utf-8')