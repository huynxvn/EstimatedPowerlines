outputfile = open("C:/Users/user/Documents/SummerProject/ExtractedCairns/t2.csv",'w')
layer = iface.activeLayer()
for l in layer.getFeatures():
    geom=l.geometry()
    string = f"{geom.asPoint().x()},{geom.asPoint().y()}\n"
    outputfile.write(string)
outputfile.close()
    
