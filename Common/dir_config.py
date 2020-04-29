import os


base_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcases_dir = os.path.join(base_dir,"TestCases")

htmlreport_dir = os.path.join(base_dir,"Outputs/reports")

logs_dir = os.path.join(base_dir,"Outputs/logs")

#config_dir = os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")