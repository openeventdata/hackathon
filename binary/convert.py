
import gdelt_pb2
import sys 


f = open("gdelt2003.pbf","wb")



eg = gdelt_pb2.EventGroup()

def u(a):
    return unicode(a, 'utf8')

c = 0 
for line in open("/Users/user/project/gdelt/backfiles/2003.csv","r"):
    # 
    #print line 

    v = line.replace("\n","").split("\t")
    e = eg.events.add()
    #e = gdelt_pb2.Event()
    #e = gdelt_pb2.Event()
    e.GLOBALEVENTID = long(v[0]) 
    e.SQLDATE = u(v[1]) 
    e.MonthYear = u(v[2])
    e.Year = u(v[3])
    e.FractionDate = u(v[4])
    e.Actor1Code = u(v[5])
    e.Actor1Name = u(v[6])
    e.Actor1CountryCode = u(v[7]) 
    e.Actor1KnownGroupCode = u(v[8])
    e.Actor1EthnicCode = u(v[9])
    e.Actor1Religion1Code = u(v[10])
    e.Actor1Religion2Code = u(v[11])
    e.Actor1Type1Code = u(v[12])
    e.Actor1Type2Code = u(v[13])
    e.Actor1Type3Code = u(v[14])
    e.Actor2Code = u(v[15])
    e.Actor2Name = u(v[16])
    e.Actor2CountryCode = u(v[17])
    e.Actor2KnownGroupCode = u(v[18])
    e.Actor2EthnicCode = u(v[19])
    e.Actor2Religion1Code = u(v[20])
    e.Actor2Religion2Code = u(v[21])
    e.Actor2Type1Code = u(v[22])
    e.Actor2Type2Code = u(v[23])
    e.Actor2Type3Code = u(v[24])
    e.IsRootEvent = u(v[25])
    e.EventCode = u(v[26])
    e.EventBaseCode = u(v[27])
    e.EventRootCode = u(v[28])
    if v[29] != "": e.QuadClass = int(v[29])
    if v[30] != "": e.GoldsteinScale = float(v[30]) # maybe losing precision...
    if v[31] != "": e.NumMentions = int(v[31])
    if v[32] != "": e.NumSources = int(v[32])
    if v[33] != "": e.NumArticles = int(v[33])
    if v[34] != "": e.AvgTone = float(v[34])   # maybe losing precision...
    if v[35] != "": e.Actor1Geo_Type = int(v[35])
    e.Actor1Geo_FullName = u(v[36])
    e.Actor1Geo_CountryCode = u(v[37])
    e.Actor1Geo_ADM1Code = u(v[38])
    if v[39] != "": e.Actor1Geo_Lat = float(v[39])
    if v[40] != "": e.Actor1Geo_Long = float(v[40])
    if v[41] != "": e.Actor1Geo_FeatureID = int(v[41])
    if v[42] != "": e.Actor2Geo_Type = int(v[42])
    e.Actor2Geo_FullName = u(v[43])
    e.Actor2Geo_CountryCode = u(v[44])
    e.Actor2Geo_ADM1Code = u(v[45])
    if v[46] != "": e.Actor2Geo_Lat = float(v[46])
    if v[47] != "": e.Actor2Geo_Long = float(v[47])
    if v[48] != "": e.Actor2Geo_FeatureID = int(v[48])
    if v[49] != "": e.ActionGeo_Type = int(v[49])
    e.ActionGeo_FullName = u(v[50])
    e.ActionGeo_CountryCode = u(v[51])
    e.ActionGeo_ADM1Code = u(v[52])
    if v[53] != "": e.ActionGeo_Lat = float(v[53])
    if v[54] != "": e.ActionGeo_Long = float(v[54])
    if v[55] != "": e.ActionGeo_FeatureID = int(v[55])
    if v[56] != "": e.DATEADDED = int(v[56])
    #e.SOURCEURL = v[57]
    
    #eg.events.append(e)

    c += 1 
    if c > 8000:
        sys.exit()    
 
print(eg.SerializeToString())

f.write(eg.SerializeToString())
f.close()
