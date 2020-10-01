from functools import partial

#Window
cmds.window("Quad Cylinder", sizeable=True, resizeToFitChildren=True) 
cmds.columnLayout( adjustableColumn=True )                                             

#Text
cmds.separator(h=20)
cmds.text("Adjust Parameters of the Quad Cylinder")
cmds.separator(h=20)

#Stem Funcations
def adjustHeight(sliderHeight, sliderNumPlates, sliderDistance, slidehieghtPlate, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the cylinder height value
        
    Adjusts the cylinder height based on the slider value
    """
    
    valHeight = cmds.floatSliderGrp(sliderHeight, q=True, value=True)
    valHeightPlates = cmds.floatSliderGrp(slidehieghtPlate, q=True, value=True)
    valDistance = cmds.floatSliderGrp(sliderDistance, q=True, value=True)
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    quadcylinderName = nameObject('base')
    quadcylinderNumber = int(numberObject('base'))
    
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    cmds.setAttr('polybase' + str(quadcylinderNumber)+ '.height', valHeight, **kwargs) 
    cmds.move(0,valHeight/2,0, quadcylinderName)
    for i in range(0, valNumPlates):
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.move(0,valHeight+2*i+(valHeightPlates/2.0) +(valDistance*i),0,nameplate)
    
    poleNumber = int(numberObject('pole'))
    poleName = nameObject('pole')
    heightPole = valHeight+2*(valNumPlates-1)+(valHeightPlates/2.0) +(valDistance*(valNumPlates-1))
    cmds.setAttr('polypole' + str(poleNumber) + '.height', heightPole, **kwargs) 
    cmds.move(0,heightPole/2,0, poleName)
    
def adjustRadiusBase(sliderRadius, sliderNumPlates, *args, **kwargs):
    """
    sliderRadius: floatSliderGrp object holding the cylinder radius value
        
    Adjusts the cylinder radius based on the slider value
    """
    
    valRadius = cmds.floatSliderGrp(sliderRadius, q=True, value=True)
    quadcylinderName = nameObject('base')
    quadcylinderNumber = int(numberObject('base'))
    cmds.setAttr('polybase' + str(quadcylinderNumber) + '.radius', valRadius, **kwargs) 
    
def adjustRadiusPole(sliderRadius, *args, **kwargs):
    """
    sliderRadius: floatSliderGrp object holding the cylinder radius value
        
    Adjusts the cylinder radius based on the slider value
    """
    
    valRadius = cmds.floatSliderGrp(sliderRadius, q=True, value=True)
    poleName = nameObject('pole')
    poleNumber = int(numberObject('pole'))
    cmds.setAttr('polypole' + str(poleNumber) + '.radius', valRadius, **kwargs) 
    
def adjustSubH(sliderSubH, sliderNumPlates, *args, **kwargs):
    """
    sliderSubH: floatSliderGrp object holding the cylinder subdivision height value
        
    Adjusts the cylinder subdivision height based on the slider value
    """
    quadcylinderName = nameObject('base')
    cmds.delete(quadcylinderName)
    base()
    
    poleName = nameObject('pole')
    cmds.delete(poleName)
    pole()
    
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(0, valNumPlates):
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.delete(nameplate)
    plates()
      
def adjustCap(sliderCap,sliderNumPlates, *args, **kwargs):
    """
    sliderCap: floatSliderGrp object holding the cylinder subdivision cap value
        
    Adjusts the cylinder subdivision cap based on the slider value
    """
    quadcylinderName = nameObject('base')
    cmds.delete(quadcylinderName)
    base()
         
    poleName = nameObject('pole')
    cmds.delete(poleName)
    pole()
    
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(0, valNumPlates):
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.delete(nameplate)
    plates()
    
def adjustSubAx(sliderSubAx,sliderNumPlates, *args, **kwargs):
    """
    sliderSubAx: floatSliderGrp object holding the cylinder subdivision axis value
        
    Adjusts the cylinder subdivision axis based on the slider value
    """
    quadcylinderName = nameObject('base')
    cmds.delete(quadcylinderName)
    base() 
    
    poleName = nameObject('pole')
    cmds.delete(poleName)
    pole()
    
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(0, valNumPlates):
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.delete(nameplate)
    plates()
    
def adjustDistance(sliderDistance, sliderNumPlates, sliderHeight, sliderPlateHeight, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the cylinder height value
        
    Adjusts the cylinder height based on the slider value
    """
    valHeight = cmds.floatSliderGrp(sliderHeight, q=True, value=True)
    valDistance = cmds.floatSliderGrp(sliderDistance, q=True, value=True)
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    valHeightPlates= cmds.floatSliderGrp(sliderPlateHeight, q=True, value=True)
    
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(1, valNumPlates):
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.move(0,valHeight+2*i+(valHeightPlates/2.0)+(valDistance*i),0,nameplate)
    
    poleNumber = int(numberObject('pole'))
    poleName = nameObject('pole')
    heightPole = valHeight+2*(valNumPlates-1)+(valHeightPlates/2.0)+(valDistance*(valNumPlates-1))
    cmds.setAttr('polypole' + str(poleNumber) + '.height', heightPole, **kwargs) 
    cmds.move(0,heightPole/2,0, poleName)
       
def adjustNumPlates(sliderNumPlates, sliderDistance, sliderHeight, sliderRadiusPlate, sliderNumTaper, sliderPlateHeight, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the cylinder height value
        
    Adjusts the cylinder height based on the slider value
    """
    valHeight = cmds.floatSliderGrp(sliderHeight, q=True, value=True)
    valDistance = cmds.floatSliderGrp(sliderDistance, q=True, value=True)
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    valRadius = cmds.floatSliderGrp(sliderRadiusPlate, q=True, value=True)
    valTaper = cmds.floatSliderGrp(sliderNumTaper, q=True, value=True)
    valHeightPlates= cmds.floatSliderGrp(sliderPlateHeight, q=True, value=True)
    
    plates() 
    
    poleNumber = int(numberObject('pole'))
    poleName = nameObject('pole')
    heightPole = valHeight+2*(valNumPlates-1)+(valHeightPlates/2.0)+(valDistance*(valNumPlates-1))
    cmds.setAttr('polypole' + str(poleNumber) + '.height', heightPole, **kwargs) 
    cmds.move(0,heightPole/2,0, poleName)
    
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    
    
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(0, valNumPlates):
       taperRadius = valRadius - (valTaper*(float(i)/float(valNumPlates))*valRadius)
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.setAttr('poly' + nameplate + '.radius', taperRadius, **kwargs) 

def adjustRadiusPlate(sliderRadiusPlate, sliderNumPlates,sliderNumTaper, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the cylinder height value
        
    Adjusts the cylinder height based on the slider value
    """
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    valRadius = cmds.floatSliderGrp(sliderRadiusPlate, q=True, value=True)
    valTaper = cmds.floatSliderGrp(sliderNumTaper, q=True, value=True)
    
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    
    
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(0, valNumPlates):
       taperRadius = valRadius - (valTaper*(float(i)/float(valNumPlates))*valRadius)
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.setAttr('poly' + nameplate + '.radius', taperRadius, **kwargs) 

def adjustRadiusTaperPlate(sliderRadiusPlate, sliderNumPlates, sliderNumTaper, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the cylinder height value
        
    Adjusts the cylinder height based on the slider value
    """
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    valRadius = cmds.floatSliderGrp(sliderRadiusPlate, q=True, value=True)
    valTaper = cmds.floatSliderGrp(sliderNumTaper, q=True, value=True)
    
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    
    
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(0, valNumPlates):
       taperRadius = valRadius - (valTaper*(float(i)/float(valNumPlates))*valRadius)
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.setAttr('poly' + nameplate + '.radius', taperRadius, **kwargs) 
       
def adjustHeightPlate(sliderHeight, sliderNumPlates, sliderDistance, slidehieghtPlate, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the cylinder height value
        
    Adjusts the cylinder height based on the slider value
    """
    
    valHeight = cmds.floatSliderGrp(sliderHeight, q=True, value=True)
    valDistance = cmds.floatSliderGrp(sliderDistance, q=True, value=True)
    valNumPlates = cmds.intSliderGrp(sliderNumPlates, q=True, value=True)
    valHeightPlates = cmds.floatSliderGrp(slidehieghtPlate, q=True, value=True)
    quadcylinderName = nameObject('base')
    quadcylinderNumber = int(numberObject('base'))
    
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    
    plateName = nameObject(name)
    plateNumber = int(numberObject(name))
    for i in range(0, valNumPlates):
       nameplate = name + str((plateNumber - (valNumPlates-i))+1)
       cmds.setAttr('poly' + nameplate + '.height', valHeightPlates, **kwargs) 
       cmds.move(0,valHeight+2*i+(valHeightPlates/2.0) +(valDistance*i),0,nameplate)
    
    poleNumber = int(numberObject('pole'))
    poleName = nameObject('pole')
    heightPole = valHeight+2*(valNumPlates-1)+(valHeightPlates/2.0)+(valDistance*(valNumPlates-1))
    cmds.setAttr('polypole' + str(poleNumber) + '.height', heightPole, **kwargs) 
    cmds.move(0,heightPole/2,0, poleName)
    
def nameObject(name):
    nameStar = name+'*'
    quadcylinderls = cmds.ls(nameStar, long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = name + quadcylinderNumber
    return quadcylinderName
    
def numberObject(name):
    nameStar = name+'*'
    quadcylinderls = cmds.ls(nameStar, long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    return quadcylinderNumber
    

def nameGroup(name):
    nameStar = name+'*'
    quadcylinderls = cmds.ls(nameStar, long=True)
    quadcylinderNumber= str(len(quadcylinderls))
    quadcylinderName = name + quadcylinderNumber
    return quadcylinderName
 
def numberGroup(name):
    nameStar = name+'*'
    quadcylinderls = cmds.ls(nameStar, long=True)
    quadcylinderNumber= str(len(quadcylinderls))
    return quadcylinderNumber
    

HeightSlider = cmds.floatSliderGrp(label='Height', columnAlign= (1,'right'), field=True, min=1, max=20, value=0, step=0.1, dc = 'empty')
HeightPlateSlider = cmds.floatSliderGrp(label='Height Plate', columnAlign= (1,'right'), field=True, min=0.5, max=4, value=0, step=0.1, dc = 'empty')
DistanceSlider = cmds.floatSliderGrp(label='Plate Distance', columnAlign= (1,'right'), field=True, min=1, max=20, value=0, step=0.1, dc = 'empty')
NumPlateSlider = cmds.intSliderGrp(label='Number Plates', columnAlign= (1,'right'), field=True, min=1, max=20, value=0, step=0.1, dc = 'empty')
RadiusPlateSlider = cmds.floatSliderGrp(label='Radius Plate', columnAlign= (1,'right'), field=True, min=5, max=20, value=0, step=0.1, dc = 'empty')
RadiusPlateTaper = cmds.floatSliderGrp(label='Radius Plate Taper', columnAlign= (1,'right'), field=True, min=0, max=1, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(RadiusPlateTaper, e=True, dc = partial(adjustRadiusTaperPlate, RadiusPlateSlider, NumPlateSlider, RadiusPlateTaper))
cmds.floatSliderGrp(RadiusPlateSlider, e=True, dc = partial(adjustRadiusPlate, RadiusPlateSlider, NumPlateSlider, RadiusPlateTaper))
cmds.intSliderGrp(NumPlateSlider, e=True, dc = partial(adjustNumPlates, NumPlateSlider, DistanceSlider, HeightSlider, RadiusPlateSlider, RadiusPlateTaper, HeightPlateSlider))

cmds.floatSliderGrp(HeightSlider, e=True, dc = partial(adjustHeight, HeightSlider, NumPlateSlider, DistanceSlider, HeightPlateSlider))

cmds.floatSliderGrp(HeightPlateSlider, e=True, dc = partial(adjustHeightPlate, HeightSlider, NumPlateSlider, DistanceSlider, HeightPlateSlider))

RadiusSlider = cmds.floatSliderGrp(label='Radius Base', columnAlign= (1,'right'), field=True, min=5, max=20, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(RadiusSlider,  e=True, dc = partial(adjustRadiusBase, RadiusSlider, NumPlateSlider))

RadiusPoleSlider = cmds.floatSliderGrp(label='Radius Pole', columnAlign= (1,'right'), field=True, min=0.5, max=4, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(RadiusPoleSlider,  e=True, dc = partial(adjustRadiusPole, RadiusPoleSlider))


SubHSlider = cmds.intSliderGrp(label='Subdivision Height', columnAlign= (1,'right'), field=True, min=1, max=20, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(SubHSlider,  e=True, dc = partial(adjustSubH, SubHSlider, NumPlateSlider))

CapSlider = cmds.intSliderGrp(label='Subdivision Cap', columnAlign= (1,'right'), field=True, min=2, max=20, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(CapSlider,  e=True, dc = partial(adjustCap, CapSlider, NumPlateSlider))

SubAxSlider = cmds.intSliderGrp(label='Subdivision Axis', columnAlign= (1,'right'), field=True, min=6, max=20, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(SubAxSlider,  e=True, dc = partial(adjustSubAx, SubAxSlider, NumPlateSlider))
cmds.floatSliderGrp(DistanceSlider,  e=True, dc = partial(adjustDistance, DistanceSlider, NumPlateSlider, HeightSlider, HeightPlateSlider))


#Button
cmds.button(l = 'Create Quad Cylinder',  c = 'cakestand()')
cmds.separator(h=20)
cmds.showWindow()

def cakestand():
    cakestand = cmds.group(empty=True, name='cakeStand#')
    height = cmds.floatSliderGrp(HeightSlider, q=True, value=True) 
    distance = cmds.floatSliderGrp(DistanceSlider, q=True, value=True) 
    base()
    plates()
    pole()

def plates():
    numPlate = cmds.intSliderGrp(NumPlateSlider, q=True, value=True) 
    valDistance = cmds.floatSliderGrp(DistanceSlider, q=True, value=True)
    valHeight = cmds.floatSliderGrp(HeightSlider, q=True, value=True)
    radius= cmds.floatSliderGrp(RadiusPlateSlider, q=True, value=True)
    radiusTaper = cmds.floatSliderGrp(RadiusPlateTaper, q=True, value=True)
    height = cmds.floatSliderGrp(HeightPlateSlider, q=True, value=True)
    subax = cmds.intSliderGrp(SubAxSlider, q=True, value=True)
    subheight = cmds.intSliderGrp(SubHSlider, q=True, value=True)
    subcap = cmds.intSliderGrp(CapSlider, q=True, value=True)
    numBase = int(numberObject('base'))
    extraP = ''
    for i in range(0,numBase):
        extraP+= 'p'
    name = extraP + 'lates'
    plateNumber = int(numberObject(name))
    if (plateNumber == 0):
        plateCyl = quadCylinder(name, radius, height, subax, subheight, subcap)
        plateName = nameObject(name)
        cmds.move(0,valHeight+(height/2.0),0,plateName)
        newname = 'poly'+ plateName
        cmds.rename('polyCylinder1', newname)
        cmds.parent(plateName, nameGroup('cakeStand'))
        cmds.select(nameGroup('cakeStand'),add=True)
    plateNumber = int(numberObject(name))
    differenceNumPlates = numPlate - plateNumber
    if (differenceNumPlates<0):
        for i in range(0, differenceNumPlates, -1):
            numberPlatetoDelete = plateNumber + i
            namePlatetoDelete = name + str(numberPlatetoDelete)
            cmds.delete(namePlatetoDelete)
    
    if (differenceNumPlates>0):
        for i in range(plateNumber,numPlate):
            taperRadius = radius - (radiusTaper*(float(i)/float(numPlate))*radius)
            plateCyl = quadCylinder(name, taperRadius, height, subax, subheight, subcap)
            plateName = nameObject(name)
            cmds.move(0,valHeight+2*i+(height/2) +(valDistance*i),0,plateName)
            
            newname = 'poly'+ plateName
            cmds.rename('polyCylinder1', newname)
            cmds.parent(plateName, nameGroup('cakeStand'))
            cmds.select(nameGroup('cakeStand'),add=True)

def base():
    radius= cmds.floatSliderGrp(RadiusSlider, q=True, value=True)
    height = cmds.floatSliderGrp(HeightSlider, q=True, value=True)
    subax = cmds.intSliderGrp(SubAxSlider, q=True, value=True)
    subheight = cmds.intSliderGrp(SubHSlider, q=True, value=True)
    subcap = cmds.intSliderGrp(CapSlider, q=True, value=True)
    name = 'base'
    baseCyl = quadCylinder(name, radius, height, subax, subheight, subcap)
    baseName = nameObject(name)
    baseNum = numberObject(name)
    newname = 'poly'+ baseName
    cmds.rename('polyCylinder1', newname)
    cmds.move(0,height/2,0,baseName)
    cmds.parent(baseName, nameGroup('cakeStand'))
    cmds.select(nameGroup('cakeStand'),add=True)
    


def pole():
    radius= cmds.floatSliderGrp(RadiusPoleSlider, q=True, value=True)
    subax = cmds.intSliderGrp(SubAxSlider, q=True, value=True)
    subheight = cmds.intSliderGrp(SubHSlider, q=True, value=True)
    subcap = cmds.intSliderGrp(CapSlider, q=True, value=True)
    valDistance = cmds.floatSliderGrp(DistanceSlider, q=True, value=True)
    valHeight = cmds.floatSliderGrp(HeightSlider, q=True, value=True)
    valHeightPlate = cmds.floatSliderGrp(HeightPlateSlider, q=True, value=True)
    numPlate = cmds.intSliderGrp(NumPlateSlider, q=True, value=True) 
    heightPole = valHeight+2*(numPlate-1)+(valHeightPlate/2)+(valDistance*(numPlate-1))
    name = 'pole'
    baseCyl = quadCylinder(name, radius, heightPole, subax, subheight, subcap)
    baseName = nameObject(name)
    newname = 'poly'+ baseName
    cmds.rename('polyCylinder1', newname)
    cmds.move(0,heightPole/2,0,baseName)
    cmds.parent(baseName, nameGroup('cakeStand'))
    cmds.select(nameGroup('cakeStand'),add=True)

def quadCylinder(name, radius, height, subax, subheight, subcap):
    #quaded cylinders can only have an even subdivision axis number, so this ensures that it will only be set to an even number
    if (subax%2 == 1):
        subax+=1
    totaledges = ((subcap*4)+((subheight*2)-1))*subax
    startEdgeToDelete = totaledges - subax*2
    nameHash = name+'#'
    nameStar = name+'*'
    
    cylinder = cmds.polyCylinder(n=nameHash, r=radius, h=height, sx=subax, sy=subheight, sc=subcap)
    quadcylinderls = cmds.ls(nameStar, long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    nameobj = nameObject(name)
    #deleting every other edge in the inner most circle of the cylinder to turn the inner triangles into quads
    listtodel = []
    for i in range (startEdgeToDelete,totaledges,2):
        listtodel.append(name + str(quadcylinderNumber) + '.e[' + str(i) + ']')
    cmds.delete(listtodel)
    #cmds.move(0,-height/2.0,0, nameobj+ ".scalePivot",nameobj+".rotatePivot", absolute=True)

