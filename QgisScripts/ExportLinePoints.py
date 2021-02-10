outputfile = open("C:/Users/user/Documents/SummerProject/ExtractedCairns/roads.csv",'w')
layer = iface.activeLayer()
for l in layer.getFeatures():
    geom=l.geometry()
    for f in geom.asPolyline():
        string = f"{f.x()} {f.y()}"
        outputfile.write(string)
        outputfile.write(",")
    outputfile.write("\n")
        
outputfile.close()