import paho.mqtt.client as mqtt
import json
import argparse
import time
# from cloud.process.RBI import DM_CAL

# This is the Publisher
# d = DM_CAL.DM_CAL(HighlyEffectDeadleg=True, ContainsDeadlegs=False, OnlineMonitoring="Sulfuric acid (H2S/H2) corrosion high velocity - Key process parameters")
# print(d.DF_THIN(5.08))

def send_data_1(Chromium=False, materialExposedFluid=False, EnvironmentCost=0, Op3=0, RiskAnalystPeriod=36,
                PressurisationControlled=False, MaterialHTHA=True, NorminalThickness=19.05, HTHAMaterialGrade="1Cr-0.5Mo",
                CorrectiveAction="None", EquOper=False, CriticalTemp=80,PTAMaterialGrade="321 Stainless Stee",
                PipeCondition="Broken gussets or gussets welded directly to pipe", ThermalHistory="Solution Annealed",
                EquipmentVolumn=100,InternalLinerCondition="Poor", MinDesignTemp=17, System="Vapor", minOP=200, NaOHConcentration=12, hydrogen=False,
                CorrosionAllowance=3.17, PresenceCracks=False, VASD=True, PresenceofSulphides=False, MaterialPTA=True,
                PTAMaterialCode="321 Stainless Stee", maxOT=100,CarbonAlloySteel=False, InterfaceSoilWater=False,
                ToxicPercent=0,componentid=1):
    data={}
    data["Chromium"] = Chromium
    data["materialExposedFluid"] = materialExposedFluid
    data["EnvironmentCost"] = EnvironmentCost
    data["Op3"] = Op3
    data["RiskAnalystPeriod"] = RiskAnalystPeriod
    data["PressurisationControlled"] = PressurisationControlled
    data["MaterialHTHA"] = MaterialHTHA
    data["NorminalThickness"] = NorminalThickness
    data["HTHAMaterialGrade"] = HTHAMaterialGrade
    data["CorrectiveAction"] = CorrectiveAction
    data["EquOper"] = EquOper
    data["CriticalTemp"] = CriticalTemp
    data["PipeCondition"] = PipeCondition
    data["ThermalHistory"] = ThermalHistory
    data["EquipmentVolumn"] = EquipmentVolumn
    data["InternalLinerCondition"]=InternalLinerCondition
    data["MinDesignTemp"]=MinDesignTemp
    data["System"]=System
    data["minOP"]=minOP
    data["NaOHConcentration"]=NaOHConcentration
    data["hydrogen"]=hydrogen
    data["CorrosionAllowance"]=CorrosionAllowance
    data["PresenceCracks"]=PresenceCracks
    data["VASD"]=VASD
    data["PresenceofSulphides"]=PresenceofSulphides
    data["MaterialPTA"]=MaterialPTA
    data["PTAMaterialCode"]=PTAMaterialCode
    data["maxOT"]=maxOT
    data["CarbonAlloySteel"]=CarbonAlloySteel
    data["InterfaceSoilWater"]=InterfaceSoilWater
    data["ToxicPercent"]=ToxicPercent
    data["componentid"]=componentid
    data["PTAMaterialGrade"]=PTAMaterialGrade
    return data

def send_data_2(Op4=0, tempRef=21, AminSolution="Diglycolamine DGA", ExternalCoatingDate="2018-09-26",
                OpHydrogenPressure=10000, EnvCaustic=False, Op9=0, Op6=0, ExposureAmine="Low Lean Amine", MassInventory=12400,
                DeltaFATT=0.5, minOT=20, CO3=0, PresenceCyanides=False, Op7=100, APIFluid="C1-C2", NumberPipeFittings="More than 10",
                InternalCladding=True, DFDI=False, ExternalCoatingQuality="Please select coat quality..", HydrogenFluoric=False,
                ToxicConstituents=True, H2SInWater=1000, NickelAlloy=False, Downtime=False,CostFactor=1.2, exposureAcid=False,
                HFICI=False, InternalLining=True, Op5=0, ExternalCoating=False,
                CylicLoad="Valve with high pressure drop", ProductionCost=50000, PresenceofSulphidesShutdown=False, EnvCH2S=False):
    data={}
    data["Op4"] = Op4
    data["tempRef"] = tempRef
    data["AminSolution"] = AminSolution
    data["ExternalCoatingDate"]=ExternalCoatingDate
    data["OpHydrogenPressure"]=OpHydrogenPressure
    data["EnvCaustic"]=EnvCaustic
    data["Op9"]=Op9
    data["Op6"]=Op6
    data["ExposureAmine"]=ExposureAmine
    data["MassInventory"]=MassInventory
    data["DeltaFATT"]=DeltaFATT
    data["minOT"]=minOT
    data["CO3"]=CO3
    data["PresenceCyanides"]=PresenceCyanides
    data["Op7"]=Op7
    data["APIFluid"]=APIFluid
    data["NumberPipeFittings"]=NumberPipeFittings
    data["InternalCladding"]=InternalCladding
    data["DFDI"]=DFDI
    data["ExternalCoatingQuality"]=ExternalCoatingQuality
    data["HydrogenFluoric"]=HydrogenFluoric
    data["ToxicConstituents"]=ToxicConstituents
    data["H2SInWater"]=H2SInWater
    data["NickelAlloy"]=NickelAlloy
    data["Downtime"]=Downtime
    data["CostFactor"]=CostFactor
    data["exposureAcid"]=exposureAcid
    data["HFICI"]=HFICI
    data["InternalLining"]=InternalLining
    data["Op5"]=Op5
    data["ExternalCoating"]=ExternalCoating
    data["CylicLoad"]=CylicLoad
    data["ProductionCost"]=ProductionCost
    data["PresenceofSulphidesShutdown"]=PresenceofSulphidesShutdown
    data["EnvCH2S"]=EnvCH2S
    return data

def send_data_3(OnlineMonitoring="aking", InsulationType='C',
                MinReqThickness=16.68, SusceptibleTemper=False, AusteniticSteel=False, PreviousFailures="Greater than one",
                allowStress=240, BranchDiameter="Any branch less than or equal to 2\" Nominal OD", MaxBrinell="Below 200",
                CylicOper=True, PHWater=5, ExposedSulfur=False, AdminControlUpset=True, CladdingCorrosionRate=0.29,
                ExternalInsulationType="Calcium Silicate", Op10=0, Op2=0, ChlorideIon=1000, PersonDensity=0.005,
                SulphurContent="High > 0.01%", HeatTraced=False, complex="Above Average", InsulationCholride=True,
                Material="plastic", MaxDesignTemp=1000, NorminalDiameter=97.62, ExternalInsulation=1, minTemp=45,
                CurrentCorrosionRate=0.29, InsulationCondition="Above average", MaterialCostFactor=1):
    data={}
    data["OnlineMonitoring"]=OnlineMonitoring
    data["InsulationType"]=InsulationType
    data["MinReqThickness"]=MinReqThickness
    data["SusceptibleTemper"]=SusceptibleTemper
    data["AusteniticSteel"]=AusteniticSteel
    data["PreviousFailures"]=PreviousFailures
    data["allowStress"]=allowStress
    data["BranchDiameter"]=BranchDiameter
    data["MaxBrinell"]=MaxBrinell
    data["CylicOper"]=CylicOper
    data["PHWater"]=PHWater
    data["ExposedSulfur"]=ExposedSulfur
    data["AdminControlUpset"]=AdminControlUpset
    data["CladdingCorrosionRate"]=CladdingCorrosionRate
    data["ExternalInsulationType"]=ExternalInsulationType
    data["Op10"]=Op10
    data["Op2"]=Op2
    data["ChlorideIon"]=ChlorideIon
    data["PersonDensity"]=PersonDensity
    data["SulphurContent"]=SulphurContent
    data["HeatTraced"]=HeatTraced
    data["complex"]=complex
    data["InsulationCholride"]=InsulationCholride
    data["Material"]=Material
    data["MaxDesignTemp"]=MaxDesignTemp
    data["NorminalDiameter"]=NorminalDiameter
    data["ExternalInsulation"]=ExternalInsulation
    data["minTemp"]=minTemp
    data["CurrentCorrosionRate"]=CurrentCorrosionRate
    data["InsulationCondition"]=InsulationCondition
    data["MaterialCostFactor"]=MaterialCostFactor
    return data

def send_data_4(SteamedOut=False, EquipmentCost=2000, CurrentThickness=19.05, LOM=False, Op8=0, InternalCoating=True,
                AqueShutdown=False, InjureCost=5000000, MFTF=False, MassComponent=24000, InternalLinerType="Acid Brick",
                ReleasePercentToxic=1, Op1=0, BranchJointType=None, supportMaterial=True, AqueOp=False, BrittleFacture=1,
                PWHT=False, ReleaseDuration="", ExternalEnvironment="Arid/dry", ContainsDeadlegs=False, Highly=True, maxOP=1000,
                timeShakingPipe="13 to 52 weeks",ChemicalInjection=False, MitigationSystem="Fire water deluge system and monitors",
                DetectionType='C', ShakingAmount="Moderate", heatTreatment="Normalised Temper", SigmaPhase=1,TrampElements=False,
                DesignPressure=12000, SulfurContent=0,proposalname="thingsboard"):
    data={}
    data["SteamedOut"]=SteamedOut
    data["EquipmentCost"]=EquipmentCost
    data["CurrentThickness"]=CurrentThickness
    data["LOM"]=LOM
    data["Op8"]=Op8
    data["InternalCoating"]=InternalCoating
    data["AqueShutdown"]=AqueShutdown
    data["InjureCost"]=InjureCost
    data["MFTF"]=MFTF
    data["MassComponent"]=MassComponent
    data["InternalLinerType"]=InternalLinerType
    data["ReleasePercentToxic"]=ReleasePercentToxic
    data["Op1"]=Op1
    data["BranchJointType"]=BranchJointType
    data["supportMaterial"]=supportMaterial
    data["AqueOp"]=AqueOp
    data["BrittleFacture"]=BrittleFacture
    data["PWHT"]=PWHT
    data["ReleaseDuration"]=ReleaseDuration
    data["ExternalEnvironment"]=ExternalEnvironment
    data["ContainsDeadlegs"]=ContainsDeadlegs
    data["Highly"]=Highly
    data["maxOP"]=maxOP
    data["timeShakingPipe"]=timeShakingPipe
    data["ChemicalInjection"]=ChemicalInjection
    data["MitigationSystem"]=MitigationSystem
    data["DetectionType"]=DetectionType
    data["ShakingAmount"]=ShakingAmount
    data["heatTreatment"]=heatTreatment
    data["SigmaPhase"]=SigmaPhase
    data["TrampElements"]=TrampElements
    data["DesignPressure"]=DesignPressure
    data["SulfurContent"]=SulfurContent
    data["proposalname"]=proposalname
    return data

# def send_data_5():

def main():
    CLOUD_URL = "demo.thingsboard.io"
    ACCESS_TOKEN1 = "xv3Cb1rLYSwqLq0qakUJ"
    PORT = 1883
    client = mqtt.Client()
    client.username_pw_set(ACCESS_TOKEN1)
    client.connect(CLOUD_URL, PORT)
    client.loop_start()

    data1 = send_data_1(Chromium=False, materialExposedFluid=False, EnvironmentCost=0, Op3=0, RiskAnalystPeriod=36,
                        PressurisationControlled=False, MaterialHTHA=True, NorminalThickness=19.05, HTHAMaterialGrade="1Cr-0.5Mo",
                        CorrectiveAction="None", EquOper=False, CriticalTemp=80,PTAMaterialGrade="321 Stainless Stee",
                        PipeCondition="Broken gussets or gussets welded directly to pipe", ThermalHistory="Solution Annealed",
                        EquipmentVolumn=100,InternalLinerCondition="Poor", MinDesignTemp=17, System="Vapor", minOP=200, NaOHConcentration=12, hydrogen=False,
                        CorrosionAllowance = 3.17, PresenceCracks = False, VASD = True, PresenceofSulphides = False, MaterialPTA = True, PTAMaterialCode = "321 Stainless Stee",
                        maxOT = 100,CarbonAlloySteel=False, InterfaceSoilWater=False,ToxicPercent=0,componentid=1)
    send_data = json.dumps(data1)
    print(send_data)
    client.publish('v1/devices/me/attributes', send_data)
    time.sleep(5)

    data2 = send_data_2(Op4=0, tempRef=21, AminSolution="Diglycolamine DGA", ExternalCoatingDate="2018-09-26",
                        OpHydrogenPressure=10000, EnvCaustic=False, Op9=0, Op6=0, ExposureAmine="Low Lean Amine",
                        MassInventory=12400,DeltaFATT=0.5, minOT=20, CO3=0, PresenceCyanides=False, Op7=100, APIFluid="C1-C2",
                        NumberPipeFittings="More than 10",InternalCladding=True, DFDI=False, ExternalCoatingQuality="Please select coat quality..",
                        HydrogenFluoric=False,ToxicConstituents=True, H2SInWater=1000, NickelAlloy=False, Downtime=False,
                        CostFactor=1.2, exposureAcid=False, HFICI=False, InternalLining=True, Op5=0,
                        ExternalCoating=False,CylicLoad="Valve with high pressure drop", ProductionCost=50000, PresenceofSulphidesShutdown=False, EnvCH2S=False
                        )
    send_data = json.dumps(data2)
    print(send_data)
    client.publish('v1/devices/me/attributes', send_data)
    time.sleep(5)

    data3 = send_data_3(OnlineMonitoring="aking", InsulationType='C',
                        MinReqThickness=16.68, SusceptibleTemper=False, AusteniticSteel=False,
                        PreviousFailures="Greater than one",
                        allowStress=240, BranchDiameter="Any branch less than or equal to 2\" Nominal OD",
                        MaxBrinell="Below 200",
                        CylicOper=True, PHWater=5, ExposedSulfur=False, AdminControlUpset=True,
                        CladdingCorrosionRate=0.29,
                        ExternalInsulationType="Calcium Silicate", Op10=0, Op2=0, ChlorideIon=1000, PersonDensity=0.005,
                        SulphurContent="High > 0.01%", HeatTraced=False, complex="Above Average",
                        InsulationCholride=True,Material="plastic", MaxDesignTemp=1000, NorminalDiameter=97.62, ExternalInsulation=1, minTemp=45,
                        CurrentCorrosionRate=0.29, InsulationCondition="Above average",MaterialCostFactor=1)
    send_data = json.dumps(data3)
    print(send_data)
    client.publish('v1/devices/me/attributes', send_data)
    time.sleep(5)

    data4 = send_data_4(SteamedOut=False, EquipmentCost=2000, CurrentThickness=19.05, LOM=False, Op8=0,
                        InternalCoating=True,
                        AqueShutdown=False, InjureCost=5000000, MFTF=False, MassComponent=24000,
                        InternalLinerType="Acid Brick",
                        ReleasePercentToxic=1, Op1=0, BranchJointType="None", supportMaterial=True, AqueOp=False,
                        BrittleFacture=1,
                        PWHT=False, ReleaseDuration="time", ExternalEnvironment="Arid/dry", ContainsDeadlegs=False,
                        Highly=True, maxOP=1000,
                        timeShakingPipe="13 to 52 weeks",ChemicalInjection=False, MitigationSystem="Fire water deluge system and monitors",
                        DetectionType='C', ShakingAmount="Moderate", heatTreatment="Normalised Temper", SigmaPhase=1,
                        TrampElements=False, DesignPressure=12000, SulfurContent=0,proposalname="thingsboard")
    send_data = json.dumps(data4)
    print(send_data)
    client.publish('v1/devices/me/attributes', send_data)
    time.sleep(5)
    client.loop_stop()
    client.disconnect()



if __name__ == "__main__":
    main()


