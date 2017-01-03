from ij import IJ, ImagePlus, ImageStack, Prefs
from ij.io import FileSaver
from ij.plugin import ChannelSplitter

imp1 = IJ.openImage('/home/mohit/Downloads/ChanA_0001_0001_0001_0001.tif')
#print imp1
#IJ.run("Enhance Contrast", "saturated=0.35"); 
imp1.show()
IJ.run("Enhance Contrast", "Auto")
IJ.run("Green")
title1 = imp1.getTitle()



imp2 = IJ.openImage('/home/mohit/Downloads/ChanB_0001_0001_0001_0001.tif')
print imp2

imp2.show()
IJ.run("Enhance Contrast", "Auto");
IJ.run("Red")
title2 = imp2.getTitle()
IJ.run("Merge Channels...","c2=["+title1+"] c1=["+title2+"]keep ignore")
imp3 = IJ.getImage()
folder = '/home/mohit/Downloads/'
filepath= folder+"/"+"final.tiff"
fs= FileSaver(imp3)
fs.saveAsTiff(filepath)