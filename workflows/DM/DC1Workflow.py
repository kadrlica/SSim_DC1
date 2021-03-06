from java.util import HashMap

def setupFilters():
   filters = ['u','g','r','i','z','y']	
   vars = HashMap()
   i = 0
   for filter in filters:
     vars.put("FILTER",filter)
     visits = []
     f = open(SLAC_SCRIPT_LOCATION+"/"+VISIT_FILE)
     for line in f.readlines():
        dir,visit,f,flags = line.split()
        if filter==f and "s" not in flags:
           visits.append(visit)  
     if visits:
        visitsFile = pipeline.createFile("filter-"+filter+"-visits.txt")
        visitsFile.addLine("--selectId visit="+"^".join(visits))
        pipeline.writeFile(visitsFile)
        pipeline.createSubstream("processFilter",i,vars)
        i += 1

def setupVisits():
   vars = HashMap()
   for visit in VISITS.split("^"):
      vars.put("VISIT",visit)
      pipeline.createSubstream("processVisit",int(visit),vars)

def setupEimageVisits():
   vars = HashMap()
   f = open(SLAC_SCRIPT_LOCATION+"/"+VISIT_FILE)
   for line in f.readlines():
      visit,filter,raft,flags = line.split()
      if "e" not in flags and "s" not in flags:
         vars.put("VISIT",visit)
         vars.put("FILTER",filter)
         vars.put("RAFT",raft)
         vars.put("FLAGS",flags)
         pipeline.createSubstream("processVisit",int(visit)*100+int(raft),vars)

def setupForcedPhotometryVisits():
   vars = HashMap()
   f = open(SLAC_SCRIPT_LOCATION+"/"+VISIT_FILE)
   for line in f.readlines():
      dir,visit,filter,flags = line.split()
      if "s" not in flags:
          vars.put("FILTER",filter)
          vars.put("VISIT",visit)
          pipeline.createSubstream("processForcedPhotometry",int(visit),vars)

def report():
   return
