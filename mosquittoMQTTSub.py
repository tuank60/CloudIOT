import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'RbiCloud.settings'
application = get_wsgi_application()

from cloud import models
import paho.mqtt.client as mqtt
import json
from datetime import datetime
from cloud.process.RBI import fastCalulate as ReCalculate
from django.shortcuts import render, redirect
import argparse

# This is the Subscriber

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'xv3Cb1rLYSwqLq0qakUJ'

def on_connect(client, userdata, rc, *extra_params):
    print("Connected with result code "+str(rc))
    sensor_data = {"Chromium": 0, "materialExposedFluid": 0, "EnvironmentCost": 0, "Op3": 0, "RiskAnalystPeriod": 0,
                   "PressurisationControlled": 0, "MaterialHTHA": 0, "NorminalThickness": 0, "HTHAMaterialGrade": 0,
                   "CorrectiveAction": 0, "EquOper": 0, "CriticalTemp": 0, "PipeCondition": 0, "ThermalHistory": 0,
                   "EquipmentVolumn": 0, "InternalLinerCondition": 0, "MinDesignTemp": 0, "System": 0, "minOP": 0,
                   "NaOHConcentration": 0, "hydrogen": 0, "CorrosionAllowance": 0, "PresenceCracks": 0, "VASD": 0,
                   "PresenceofSulphides": 0, "MaterialPTA": 0, "PTAMaterialCode": 0, "maxOT": 0, "CarbonAlloySteel": 0,
                   "InterfaceSoilWater": 0, "ToxicPercent": 0,"Op4": 0, "tempRef": 0, "AminSolution": 0, "ExternalCoatingDate": 0,
                   "OpHydrogenPressure": 0, "EnvCaustic": 0, "Op9": 0, "Op6": 0, "ExposureAmine": 0, "MassInventory": 0, "DeltaFATT": 0, "minOT": 0, "CO3": 0,
                   "PresenceCyanides": 0, "Op7": 0, "APIFluid": 0, "NumberPipeFittings": 0,"InternalCladding": 0, "DFDI": 0, "ExternalCoatingQuality": 0,
                   "HydrogenFluoric": 0, "ToxicConstituents": 0, "H2SInWater": 0, "NickelAlloy": 0,
                   "Downtime": 0, "CostFactor": 0, "exposureAcid": 0, "HFICI": 0, "InternalLining": 0,
                   "Op5": 0, "ExternalCoating": 0, "CylicLoad": 0,"ProductionCost": 0, "PresenceofSulphidesShutdown": 0, "EnvCH2S": 0,
                   "OnlineMonitoring": 0, "InsulationType": 0, "MinReqThickness": 0,"SusceptibleTemper": 0, "AusteniticSteel": 0,
                   "PreviousFailures": 0,"allowStress": 0, "BranchDiameter": 0,
                   "MaxBrinell": 0, "CylicOper": 0, "PHWater": 0, "ExposedSulfur": 0,
                   "AdminControlUpset": 0, "CladdingCorrosionRate": 0,
                   "ExternalInsulationType": 0, "Op10": 0, "Op2": 0, "ChlorideIon": 0,
                   "PersonDensity": 0, "SulphurContent": 0, "HeatTraced": 0,
                   "complex": 0, "InsulationCholride": 0, "Material": 0, "MaxDesignTemp": 0,
                   "NorminalDiameter": 0, "ExternalInsulation": 0, "minTemp": 0, "CurrentCorrosionRate": 0,
                   "InsulationCondition": 0,"SteamedOut": 0, "EquipmentCost": 0, "CurrentThickness": 0, "LOM": 0, "Op8": 0,
                   "InternalCoating": 0, "AqueShutdown": 0, "InjureCost": 0, "MFTF": 0,
                   "MassComponent": 0, "InternalLinerType": 0, "ReleasePercentToxic": 0, "Op1": 0,
                   "BranchJointType": 0, "supportMaterial": 0, "AqueOp": 0, "BrittleFacture": 0,
                   "PWHT": 0, "ReleaseDuration": 0, "ExternalEnvironment": 0,
                   "ContainsDeadlegs": 0, "Highly": 0, "maxOP": 0, "timeShakingPipe": 0,
                   "ChemicalInjection": 0, "MitigationSystem": 0,"DetectionType": 0, "ShakingAmount": 0, "heatTreatment": 0,
                   "SigmaPhase": 0, "TrampElements": 0, "DesignPressure": 0, "SulfurContent": 0,"componentid":0,"proposalname":0}
    client.subscribe('v1/devices/me/attributes/response/+')
    client.publish('v1/devices/me/attributes/request/1', json.dumps(sensor_data))
# def on_subcribe(client, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
# def on_log(client, obj, level, string):
#     print(string)
def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload)
    payload = msg.payload.decode()
    data_sensor = json.loads(payload)
    print(data_sensor['client'])
    data = data_sensor['client']
    comp = models.ComponentMaster.objects.get(componentid= int(data["componentid"]))
    facility_id = models.EquipmentMaster.objects.get(equipmentid=comp.equipmentid_id).facilityid_id
    target = models.FacilityRiskTarget.objects.get(facilityid=facility_id)
    faci = models.Facility.objects.get(facilityid=facility_id)
    data["APIComponentTypeID"] = models.ApiComponentType.objects.get(apicomponenttypeid=comp.apicomponenttypeid).apicomponenttypename
    data['equipmentType'] = models.EquipmentType.objects.get(equipmenttypeid=models.EquipmentMaster.objects.get(equipmentid=comp.equipmentid_id).equipmenttypeid_id).equipmenttypename
    data['AssessmentDate'] = datetime.now()
    rw_assessment = models.RwAssessment(equipmentid_id=comp.equipmentid_id, componentid_id=comp.componentid, 
        assessmentdate=data['AssessmentDate'], riskanalysisperiod=data['RiskAnalystPeriod'], 
        isequipmentlinked= comp.isequipmentlinked, proposalname=data["proposalname"])
    rw_assessment.save()
    print("1")
    rw_equipment = models.RwEquipment(id=rw_assessment, commissiondate=models.EquipmentMaster.objects.get(equipmentid= comp.equipmentid_id).commissiondate,
        adminupsetmanagement=data["AdminControlUpset"], containsdeadlegs=data["ContainsDeadlegs"],
        cyclicoperation=data["CylicOper"], highlydeadleginsp=data["Highly"],
        downtimeprotectionused=data["Downtime"], externalenvironment=data['ExternalEnvironment'],
        heattraced=data["HeatTraced"], interfacesoilwater=data["InterfaceSoilWater"],
        lineronlinemonitoring=data["LOM"], materialexposedtoclext=data["MFTF"],
        minreqtemperaturepressurisation=data["minTemp"],
        onlinemonitoring=data['OnlineMonitoring'], presencesulphideso2=data["PresenceofSulphides"],
        presencesulphideso2shutdown=data["PresenceofSulphidesShutdown"],
        pressurisationcontrolled=data["PressurisationControlled"], pwht=data["PWHT"], steamoutwaterflush=data["SteamedOut"],
        managementfactor= faci.managementfactor, thermalhistory=data['ThermalHistory'],
        yearlowestexptemp=data["EquOper"], volume=data["EquipmentVolumn"])
    rw_equipment.save()
    print("2")
    rwcomponent = models.RwComponent(id=rw_assessment, nominaldiameter=data["NorminalDiameter"],
        nominalthickness=data['NorminalThickness'], currentthickness=data['CurrentThickness'],
        minreqthickness=data['MinReqThickness'], currentcorrosionrate=data['CurrentCorrosionRate'],
        branchdiameter=data['BranchDiameter'], branchjointtype=data['BranchJointType'],
        brinnelhardness=data['MaxBrinell']
        , deltafatt=data['DeltaFATT'], chemicalinjection=data["ChemicalInjection"],
        highlyinjectioninsp=data["HFICI"], complexityprotrusion=data['complex'],
        correctiveaction=data['CorrectiveAction'], crackspresent=data["PresenceCracks"],
        cyclicloadingwitin15_25m=data['CylicLoad'],
        damagefoundinspection=data["DFDI"], numberpipefittings=data['NumberPipeFittings'],
        pipecondition=data['PipeCondition'],
        previousfailures=data['PreviousFailures'], shakingamount=data['ShakingAmount'],
        shakingdetected=data["VASD"], shakingtime=data['timeShakingPipe'],
        trampelements=data["TrampElements"])
    rwcomponent.save()
    print("3")
    rwstream = models.RwStream(id=rw_assessment, aminesolution=data['AminSolution'], aqueousoperation=data["AqueOp"],
        aqueousshutdown=data["AqueShutdown"], toxicconstituent=data["ToxicConstituents"],
        caustic=data["EnvCaustic"],
        chloride=data['ChlorideIon'], co3concentration=data['CO3'], cyanide=data["PresenceCyanides"],
        exposedtogasamine=data["exposureAcid"], exposedtosulphur=data["ExposedSulfur"],
        exposuretoamine=data['ExposureAmine'],
        h2s=data["EnvCH2S"], h2sinwater=data["H2SInWater"], hydrogen=data["hydrogen"],
        hydrofluoric=data["HydrogenFluoric"], materialexposedtoclint=data["materialExposedFluid"],
        maxoperatingpressure=data['maxOP'],
        maxoperatingtemperature=float(data['maxOT']), minoperatingpressure=float(data['minOP']),
        minoperatingtemperature=data['minOT'], criticalexposuretemperature=data['CriticalTemp'],
        naohconcentration=data['NaOHConcentration'],
        releasefluidpercenttoxic=float(data['ReleasePercentToxic']),
        waterph=float(data['PHWater']), h2spartialpressure=float(data['OpHydrogenPressure']))
    rwstream.save()
    print("4")
    rwexcor = models.RwExtcorTemperature(id=rw_assessment, minus12tominus8=data['Op1'], 
        minus8toplus6=data['Op2'], plus6toplus32=data['Op3'], plus32toplus71=data['Op4'],
        plus71toplus107=data['Op5'], plus107toplus121=data['Op6'], plus121toplus135=data['Op7'],
        plus135toplus162=data['Op8'], plus162toplus176=data['Op9'], morethanplus176=data['Op10'])
    rwexcor.save()
    print("5")
    rwcoat = models.RwCoating(id=rw_assessment, externalcoating=data["ExternalCoating"], 
        externalinsulation=data["ExternalInsulation"],
        internalcladding=data["InternalCladding"], internalcoating=data["InternalCoating"],
        internallining=data["InternalLining"], externalcoatingdate=data["ExternalCoatingDate"],
        externalcoatingquality=data['ExternalCoatingQuality'], externalinsulationtype=data["ExternalInsulationType"],
        insulationcondition=data['InsulationCondition'], insulationcontainschloride=data["InsulationCholride"],
        internallinercondition=data['InternalLinerCondition'], internallinertype=data['InternalLinerType'],
        claddingcorrosionrate=data["CladdingCorrosionRate"], supportconfignotallowcoatingmaint=data["supportMaterial"])
    rwcoat.save()
    print("6")
    # rwmaterial = models.RwMaterial(id=rw_assessment, corrosionallowance=data["CorrosionAllowance"], materialname=data['Material'],
    #     designpressure=data['DesignPressure'], designtemperature=data['MaxDesignTemp'], ishtha=data["MaterialHTHA"],
    #     mindesigntemperature=data['MinDesignTemp'], brittlefracturethickness=data['BrittleFacture'],
    #     sigmaphase=data['SigmaPhase'], sulfurcontent=data["SulfurContent"], heattreatment=data['heatTreatment'],
    #     referencetemperature=data["tempRef"], ptamaterialcode=data['PTAMaterialGrade'],
    #     hthamaterialcode=data['HTHAMaterialGrade'], ispta=data["MaterialPTA"], austenitic=data["AusteniticSteel"],
    #     temper=data["SusceptibleTemper"], carbonlowalloy=data["CarbonAlloySteel"], nickelbased=data["NickelAlloy"],
    #     chromemoreequal12=data["Chromium"], allowablestress=data['allowStress'], costfactor=data['MaterialCostFactor'])
    # rwmaterial.save()
    print(data["CorrosionAllowance"])
    print(data['Material'])
    print(data['DesignPressure'])
    print(data['MaxDesignTemp'])
    print(data['MinDesignTemp'])
    print(data['BrittleFacture'])
    print(data['SigmaPhase'])
    print(data["SulfurContent"])
    print(data['heatTreatment'])
    print(data["tempRef"])
    print(data['PTAMaterialGrade'])
    print(data['HTHAMaterialGrade'])
    print(data["MaterialPTA"])
    print(data["MaterialHTHA"])
    print(data["AusteniticSteel"])
    print(data["SusceptibleTemper"])
    print(data["CarbonAlloySteel"])
    print(data["NickelAlloy"])
    print(data["Chromium"])
    print(data['allowStress'])
    print(data['MaterialCostFactor'])
    rwmaterial = models.RwMaterial(id=rw_assessment, corrosionallowance=data["CorrosionAllowance"], materialname=data['Material'],
                                   designpressure=data['DesignPressure'], designtemperature=data['MaxDesignTemp'],
                                   mindesigntemperature=data['MinDesignTemp'],
                                   brittlefracturethickness=data['BrittleFacture'], sigmaphase=data['SigmaPhase'],
                                   sulfurcontent=data["SulfurContent"], heattreatment=data['heatTreatment'],
                                   referencetemperature=data["tempRef"],
                                   ptamaterialcode=data['PTAMaterialGrade'],
                                   hthamaterialcode=data['HTHAMaterialGrade'], ispta=data["MaterialPTA"], ishtha=data["MaterialHTHA"],
                                   austenitic=data["AusteniticSteel"], temper=data["SusceptibleTemper"], carbonlowalloy=data["CarbonAlloySteel"],
                                   nickelbased=data["NickelAlloy"], chromemoreequal12=data["Chromium"],
                                   allowablestress=data['allowStress'], costfactor=data['MaterialCostFactor'])
    rwmaterial.save()
    print("7")
    rwinputca = models.RwInputCaLevel1(id=rw_assessment, api_fluid=data['APIFluid'], system=data['System'],
        release_duration=data['ReleaseDuration'], detection_type=data['DetectionType'],
        isulation_type=data['InsulationType'],
        mitigation_system=data['MitigationSystem'],
        equipment_cost=data['EquipmentCost'], injure_cost=data['InjureCost'],
        evironment_cost=data['EnvironmentCost'], toxic_percent=data['ToxicPercent'],
        personal_density=data['PersonDensity'],
        material_cost=data['MaterialCostFactor'],
        production_cost=data['ProductionCost'], mass_inventory=data['MassInventory'],
        mass_component=data['MassComponent'],
        stored_pressure=float(data['minOP']) * 6.895, stored_temp=data['minOT'])
    rwinputca.save()
    print("Calculating...")
    ReCalculate.ReCalculate(rw_assessment.id)
    print(rw_assessment.id)
    print("okok")
    # return redirect('damgeFactor', proposalID=rwassessment.id)

    print("Finished!")
    # client.disconnect()

def main():
    client = mqtt.Client()
    client.username_pw_set("xv3Cb1rLYSwqLq0qakUJ")
    client.connect("demo.thingsboard.io", 1883)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


if __name__ == "__main__":
    main()