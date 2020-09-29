from functools import partial

#Window
cmds.window("Cake Stand", sizeable=True, resizeToFitChildren=True) 
cmds.columnLayout( adjustableColumn=True )                                             

#Text
cmds.separator(h=20)
cmds.text("Adjust Parameters of the Cake Stand")
cmds.separator(h=20)

#Stem Funcations
def adjustBaseHeight(sliderHeight, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the stem radius value
        
    Adjusts the stem radius of the stem based on the slider value
    """
    
    valHeight = cmds.floatSliderGrp(sliderRadius, q=True, value=True)
    basels = cmds.ls('base*', long=True)
    baseName = basels[len(basels)-1][1:5]
    baseNumber= basels[len(basels)-1][4]
    cmds.select(baseName, r=True)
    cmds.setAttr('polySphere' + baseNumber+ '.radius', valHeight, **kwargs)   

baseHeightSlider = cmds.floatSliderGrp(label='Base Height', columnAlign= (1,'right'), field=True, min=1, max=5, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(baseHeightSlider,  e=True, dc = partial(adjustBaseHeight, baseHeightSlider))

#Butto'
cmds.button(l = 'Create Cake Stand',  c = 'base()')
cmds.separator(h=20)
cmds.showWindow()

    
def base():
    baseSides = 5
    baseHieght = cmds.floatSliderGrp(baseHeightSlider, q=True, value=True)
    baseSub = 3
    baseRadius = 4
    #baseShape = Circle
   # finalCap = cmds.polySphere(n='cap#', r=3, sx=3, sy=3, ch=True)
    finalStem = cmds.polyDisc(poly='disk#', radius=1, s=4, sd=3)
