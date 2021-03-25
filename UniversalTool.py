####################################
#                                            #
#            MAYA LIP SYNC TOOLS             #
#           written by Corey Gohm            #
#                                            #
####################################

import maya.cmds as cmds
cmds.window( title='Tool Generator',sizeable=False )

cmds.rowColumnLayout(nc=1, columnWidth=[(1,375)])
name = cmds.textField(pht="Name Space")
rig = cmds.textField(pht="Rig Name")


def createTools(a):
    name1 = cmds.textField(name, q=True, text=True)
    rig1 = cmds.textField(rig, q=True, text=True)
    if rig1 == "Sam":
        def resetMouth(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", 0)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", 0)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")
           
        def AHH(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.765)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", 0.034)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", 0.033)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", 0.063)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", 0.067)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", -1.437)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")
          
        def OHH(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.506)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 1.4)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", -0.8)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 3.1)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", -0.853)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", -0.619)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", 0)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", 6.076)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")
          
        def UUU(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.553)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 2.3)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", 2.6)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 5.1)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 4.5)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", -1)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", -1)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", -0.397)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", -0.477)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", -1.404)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")
         
        def IEE(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.597)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 0.9)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", 0.306)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0.319)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", 0.186)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0.358)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", -0.241)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", 0.013)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", -4.32)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")
            
        def EHH(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.597)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 0.9)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", 0.162)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0.319)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", -0.005)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0.358)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", -0.241)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", 0.013)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          cmds.setAttr(name1+ "FKJaw_M.rx", -4.32)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", 3.526)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")

        def FFF(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 1.2)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", -12.4)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 1.6)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 4.8)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 4.8)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", 0.013)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", -0.241)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", 3.526)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")
            
        def LLL(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.637)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 0.9)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0.256)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0.256)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", -0.241)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", 0.013)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", -4.32)
         
          cmds.setAttr(name1+ "FKTongue2_M.rz", 29.198)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 19.245)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")
            
        def TTH(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.73)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", 0.9)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_L", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", -0.276)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0.319)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", -0.461)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0.358)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", -0.241)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", 0.013)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", -4.32)
         
          cmds.setAttr(name1+ "FKTongue2_M.rz", 10.115)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 10.071)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")

        def MBP(a):
          cmds.setAttr(name1+ "ctrlMouth_M.tx", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.ty", -0.14)
          cmds.setAttr(name1+ "ctrlMouth_M.upperRoll", -1)
          cmds.setAttr(name1+ "ctrlMouth_M.lowerRoll", -5.3)
          cmds.setAttr(name1+ "ctrlMouth_M.stickyLips", 0)
          cmds.setAttr(name1+ "ctrlMouth_M.zipLips_R", 0)
          
          cmds.setAttr(name1+ "ctrlMouthCorner_L.tx", -0.804)
          cmds.setAttr(name1+ "ctrlMouthCorner_L.ty", 0)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.tx", -0.667)
          cmds.setAttr(name1+ "ctrlMouthCorner_R.ty", 0)
          
          cmds.setAttr(name1+ "ctrlCheek_R.tx", -0.728)
          cmds.setAttr(name1+ "ctrlCheek_R.ty", 0)
          cmds.setAttr(name1+ "ctrlCheek_L.tx", -0.502)
          cmds.setAttr(name1+ "ctrlCheek_L.ty", 0)
          
          cmds.setAttr(name1+ "FKJaw_M.rx", -2.395)
          
          cmds.setAttr(name1+ "FKTongue2_M.rz", 0)
          cmds.setAttr(name1+ "FKTongue3_M.rz", 0)
          
          cmds.setKeyframe(name1+ "ctrlMouth_M",name1+ "ctrlMouthCorner_L",name1+ "ctrlMouthCorner_R",name1+ "ctrlCheek_R",name1+ "ctrlCheek_L", name1+ "FKJaw_M.rx",name1+ "FKTongue2_M",name1+ "FKTongue3_M")

        ####   PLay Back ####
        
        def play(a):
            cmds.play(forward=True)
        def stop(a):
            cmds.play(state=False)
            

        ###### Window Commands #########

        cmds.window( widthHeight=(308, 210),title="Sam Custom Tools", sizeable=True )
        form = cmds.formLayout()
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

        ### Lipsync Tab ###
        child1 = cmds.rowColumnLayout(numberOfColumns=3,columnWidth=[(1, 100), (2, 100), (3, 100)], rs = (10,10),cs = (10,10))
        cmds.button( label='AHH', c = AHH)
        cmds.button( label='OHH', c = OHH)
        cmds.button( label='EHH', c = EHH)
        cmds.button( label='UUU', c = UUU)
        cmds.button( label='IEE', c = IEE)
        cmds.button( label='FFF', c = FFF)
        cmds.button( label='LLL', c = LLL)
        cmds.button( label='TTH', c = TTH)
        cmds.button( label='MBP', c = MBP)
        cmds.button( label='RESET MOUTH',width=300, c=resetMouth)
        cmds.button( label='RESET MOuth',m=False)
        cmds.button( label='RESET MOuth',m=False)
        cmds.button( label='play', c=play)
        cmds.button( label='stop', c=stop)
        cmds.setParent( '..' )

        child2 = cmds.rowColumnLayout(nc=2, columnWidth=[(1,375),(2,375),(8,750), (9,750)])
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=400, label = "Right Blink")
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_L.blink", width=400, label = "Left Blink")
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_L.blink", width=1,m = False )
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.squint", width=400, label="Right Squint")
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.squint", width=1, m=False)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_L.squint", width=400, label="Left Squint")
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.squint", width=1, m=False)

        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=400, label="Right Brow Inner")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.ty", width=400, label="Right Brow outer")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.squeeze", width=400, label="Right Brow Squeeze")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=1, m=False)

        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.tx", width=400, label="Left Brow Inner")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.ty", width=400, label="Left Brow outer")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.squeeze", width=400, label="Left Brow Squeeze")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.tx", width=1, m=False)
        cmds.setParent( '..' )
        cmds.showWindow()
    elif rig1 == "Nadia" or rig1=="Penelopy" or rig1=="Brooke":
        def resetMouth(a):
            cmds.setAttr(name1+ "ctrlPhonemes_M.aaa",0)
            cmds.setAttr(name1+"ctrlPhonemes_M.eh",0)
            cmds.setAttr(name1+"ctrlPhonemes_M.ohh",0)
            cmds.setAttr(name1+"ctrlPhonemes_M.uuu",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.iee",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.rrr",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.www",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.sss",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.fff",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.tth",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.mbp",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.ssh",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.schwa",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.gk",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.lntd",0)
            cmds.setAttr(name1+ "ctrlPhonemes_M.ahh",0)
            
        def resetEyes(a):
            cmds.setAttr(name1+ "ctrlEye_R.blink", 0)
            cmds.setAttr(name1+ "ctrlEye_L.blink", 0)
            
        def resetEmotions(a):
            cmds.setAttr(name1+ "ctrlEmotions_M.happy",0)
            cmds.setAttr(name1+ "ctrlEmotions_M.angry",0)
            cmds.setAttr(name1+ "ctrlEmotions_M.sad",0)
            cmds.setAttr(name1+ "ctrlEmotions_M.surprise",0)
            cmds.setAttr(name1+ "ctrlEmotions_M.fear",0)
            cmds.setAttr(name1+ "ctrlEmotions_M.disgust",0)
            cmds.setAttr(name1+ "ctrlEmotions_M.contempt",0)
            
        def keyMouth(a):
            cmds.setKeyframe(name1+ "ctrlPhonemes_M.aaa",name1+ "ctrlPhonemes_M.eh",name1+ "ctrlPhonemes_M.ohh",name1+ "ctrlPhonemes_M.uuu")
            cmds.setKeyframe(name1+ "ctrlPhonemes_M.iee",name1+ "ctrlPhonemes_M.rrr",name1+ "ctrlPhonemes_M.www",name1+ "ctrlPhonemes_M.sss")
            cmds.setKeyframe(name1+ "ctrlPhonemes_M.fff",name1+ "ctrlPhonemes_M.tth",name1+ "ctrlPhonemes_M.mbp",name1+ "ctrlPhonemes_M.ssh")
            cmds.setKeyframe(name1+ "ctrlPhonemes_M.schwa",name1+ "ctrlPhonemes_M.gk",name1+ "ctrlPhonemes_M.lntd",name1+ "ctrlPhonemes_M.ahh")
            
        def keyEyes(a):
            cmds.setKeyframe(name1+ "ctrlEye_R.blink",name1+ "ctrlEye_L.blink")
            cmds.setKeyframe(name1+ "ctrlBrow_R.tx",name1+ "ctrlBrow_R.ty",name1+ "ctrlBrow_R.squeeze")
            cmds.setKeyframe(name1+ "ctrlBrow_L.tx",name1+ "ctrlBrow_L.ty",name1+ "ctrlBrow_L.squeeze")
            
        def keyEmotions(a):
            cmds.setKeyframe(name1+ "ctrlEmotions_M.happy",name1+ "ctrlEmotions_M.angry",name1+ "ctrlEmotions_M.sad",name1+ "ctrlEmotions_M.surprise",name1+ "ctrlEmotions_M.fear",name1+ "ctrlEmotions_M.disgust",name1+ "ctrlEmotions_M.contempt")
            
        if rig1 == "Nadia":
           cmds.window( widthHeight=(308, 210),title="Nadia Custom Tools", sizeable=True ) 
        elif rig1== "Penelopy":
            cmds.window( widthHeight=(308, 210),title="Penelopy Custom Tools", sizeable=True )
        elif rig1 =="Brooke":
            cmds.window( widthHeight=(308, 210),title="Brooke Custom Tools", sizeable=True )
  
        
        form = cmds.formLayout()
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

        child1 = cmds.rowColumnLayout(nc=2, columnWidth=[(1,375),(2,375),(8,750), (9,750)])
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.aaa", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.eh", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.ahh", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.ohh", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.uuu", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.iee", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.rrr", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.www", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.sss", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.fff", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.tth", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.mbp", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.ssh", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.schwa", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.gk", width=375)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlPhonemes_M.lntd", width=375)
        if rig1=="Brooke":
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )

        
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEmotions_M.happy", width=375, label = "Happy")
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEmotions_M.angry", width=375, label = "Angry")
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEmotions_M.sad", width=375, label = "Sad")
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEmotions_M.surprise", width=375, label = "Surprise")
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEmotions_M.disgust", width=375, label = "Disgust")
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEmotions_M.fear", width=375, label = "Fear")
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEmotions_M.contempt", width=375, label = "contempt")
            
            cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )
            
        
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )

        

        cmds.button(label="Reset Mouth", c=resetMouth)
        cmds.button(label="Key Mouth", c=keyMouth)

        cmds.button(label="Reset Emotions", c=resetEmotions)
        cmds.button(label="Key Emotions", c=keyEmotions)
        cmds.setParent('..')


        child2 = cmds.rowColumnLayout(nc=2, columnWidth=[(1,375),(2,375),(8,750), (9,750)])
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=750, label = "Right Blink")
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_L.blink", width=750, label = "Left Blink")
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10, pre=2, at=name1+ "ctrlEye_R.blink", width=1,m = False )

        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=400, label="Right Brow Inner")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.ty", width=400, label="Right Brow outer")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10.0, pre=2, at=name1+ "ctrlBrow_R.squeeze", width=750, label="Right Brow Squeeze")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_R.tx", width=1, m=False)

        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.tx", width=400, label="Left Brow Inner")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+"ctrlBrow_L.ty", width=400, label="Left Brow outer")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+"ctrlBrow_L.tx", width=1, m=False)
        cmds.attrFieldSliderGrp( min=0, max=10.0, fmn=0, fmx=10.0, pre=2, at=name1+ "ctrlBrow_L.squeeze", width=750, label="Left Brow Squeeze")
        cmds.attrFieldSliderGrp( min=-1.0, max=1.0, fmn=-1, fmx=1, pre=2, at=name1+ "ctrlBrow_L.tx", width=1, m=False)

        cmds.button(label="Reset Eyes", c=resetEyes)
        cmds.button(label="Key Eyes", c=keyEyes)
        cmds.setParent('..')

        cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Mouth Buttons'),(child2, 'Eye Sliders')) )
    elif rig1 == "Ruby" or rig1=="Link" or rig1 =="Zelda":
        def resetMouth(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", 0)
            cmds.setAttr("CN_Bip001_Sync.ty", 0)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0)
            cmds.setAttr("CN_Bip001_Emote.ty", 0)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)

            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)
            
        def AHH(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", 0)
            cmds.setAttr("CN_Bip001_Sync.ty", -1)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0)
            cmds.setAttr("CN_Bip001_Emote.ty", 0)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)
            
            
            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)
              
        def OHH(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", -0.812)
            cmds.setAttr("CN_Bip001_Sync.ty", -0.587)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", -0.503)
            cmds.setAttr("CN_Bip001_Emote.ty", -0.503)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)
            
            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0.279)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", -0.16)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", -0.287)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0.119)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", -0.0117)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", -0.401)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", -0.055)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", -0.06)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", -0.144)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", 0.385)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", -0.004)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", -0.124)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0.178)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", -0.075)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0.002)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", -0.414)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", -0.016)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", -0.287)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", -0.124)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", -0.113)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", -0.545)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", -0.005)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", -0.06)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", -0.144)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", -0.421)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", -0.003)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", -0.06)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", -0.265)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0.005)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", -0.002)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", -0.062)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0.033)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0.001)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0.259)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)
             
        def UUU(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", -1)
            cmds.setAttr("CN_Bip001_Sync.ty", -0.428)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0)
            cmds.setAttr("CN_Bip001_Emote.ty", 0)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)

            
            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0.463)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", -0.16)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", -0.287)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0.309)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", -0.01)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", -0.073)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0.091)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", -0.063)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", -0.144)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", 0.385)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", -0.004)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", -0.124)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0.178)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", -0.075)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0.002)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", -0.661)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", -0.016)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", -0.287)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", -0.374)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", -0.021)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", -0.213)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", -0.161)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", -0.063)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", -0.144)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", -0.421)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", -0.003)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", -0.06)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", -0.265)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0.005)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", -0.002)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", -0.062)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0.033)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0.001)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0.259)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)
         
        def EHH(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", -0.118)
            cmds.setAttr("CN_Bip001_Sync.ty", -0.512)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0.379)
            cmds.setAttr("CN_Bip001_Emote.ty", 0.379)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0.208)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0.208)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)

            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", -0.03)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0.16)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", -0.01)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", -0.011)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0.162)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", -0.17)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0.122)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", -0.012)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0.03)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0.16)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", -0.01)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0.011)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0.162)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", -0.017)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0.122)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", -0.012)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)
            
        def IEE(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", 0.213)
            cmds.setAttr("CN_Bip001_Sync.ty", -0.37)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0.255)
            cmds.setAttr("CN_Bip001_Emote.ty", 0.255)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0.384)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0.384)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)

            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)

        def FFF(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", 0.064)
            cmds.setAttr("CN_Bip001_Sync.ty", 0.347)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0.099)
            cmds.setAttr("CN_Bip001_Emote.ty", 0.099)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0.276)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0.276)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 1.646)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)

            
            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", -3.564)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", -3.564)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0.161)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", -0.099)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", -6.36)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", -16.697)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)
            
        def LLL(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", 0.189)
            cmds.setAttr("CN_Bip001_Sync.ty", -0.419)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0)
            cmds.setAttr("CN_Bip001_Emote.ty", 0)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 51.063)

            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", -0.03)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0.16)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", -0.01)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", -0.011)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0.162)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", -0.17)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0.122)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", -0.012)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0.03)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0.16)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", -0.01)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0.011)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0.162)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", -0.017)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0.122)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", -0.012)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)
            
        def TTH(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", 0.189)
            cmds.setAttr("CN_Bip001_Sync.ty", -0.315)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0.211)
            cmds.setAttr("CN_Bip001_Emote.ty", 0.211)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0.257)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0.257)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 0)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0.707)
            cmds.setAttr("CN_Bip001_Tongue2.ty", -0.125)
            cmds.setAttr("CN_Bip001_Tongue2.tz", -0.181)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 29.387)

            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)

        def MBP(a):
            #set the Mouth Sync atributes
            cmds.setAttr("CN_Bip001_Sync.tx", -0.209)
            cmds.setAttr("CN_Bip001_Sync.ty", 1)
            
            #set the Emote atributes
            cmds.setAttr("CN_Bip001_Emote.tx", 0.076)
            cmds.setAttr("CN_Bip001_Emote.ty", 0.076)
            
            #set the Sneer atibutes
            cmds.setAttr("CN_Bip001_Sneer.tx", 0)
            cmds.setAttr("CN_Bip001_Sneer.ty", 0)
            
            #Set the FV atributes
            cmds.setAttr("CN_Bip001_FV.tx", 1.468)
            
            #Toung Control
            cmds.setAttr("CN_Bip001_Tongue2.tx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ty", 0)
            cmds.setAttr("CN_Bip001_Tongue2.tz", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rx", 0)
            cmds.setAttr("CN_Bip001_Tongue2.ry", 0)
            cmds.setAttr("CN_Bip001_Tongue2.rz", 0)

            #Mouth Details
            cmds.setAttr("CN_Bip001_LipCorner_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_R.tx", -0.012)
            cmds.setAttr("CN_Bip001_LipLower2_R.ty", 0.217)
            cmds.setAttr("CN_Bip001_LipLower2_R.tz", 0.057)
            cmds.setAttr("CN_Bip001_LipLower2_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_R.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ty", 0.205)
            cmds.setAttr("CN_Bip001_LipLower1_R.tz", 0.092)
            cmds.setAttr("CN_Bip001_LipLower1_R.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_R.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipCorner_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipCorner_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper2_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper2_L.rz", 0)
           
            cmds.setAttr("CN_Bip001_LipUpper1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower2_L.tx", 0.012)
            cmds.setAttr("CN_Bip001_LipLower2_L.ty", 0.217)
            cmds.setAttr("CN_Bip001_LipLower2_L.tz", 0.059)
            cmds.setAttr("CN_Bip001_LipLower2_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower2_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower1_L.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ty", 0.205)
            cmds.setAttr("CN_Bip001_LipLower1_L.tz", 0.092)
            cmds.setAttr("CN_Bip001_LipLower1_L.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower1_L.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipUpper_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ty", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.tz", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipUpper_C.rz", 0)
            
            cmds.setAttr("CN_Bip001_LipLower_C.tx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ty", 0.205)
            cmds.setAttr("CN_Bip001_LipLower_C.tz", 0.093)
            cmds.setAttr("CN_Bip001_LipLower_C.rx", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.ry", 0)
            cmds.setAttr("CN_Bip001_LipLower_C.rz", 0)

        def resetEyes(a):
            cmds.setAttr("CN_Bip001_Eyes.blinkR", 0)
            cmds.setAttr("CN_Bip001_Eyes.blinkL", 0)
            
        def resetBrows(a):
            cmds.setAttr("CN_Bip001_BrowUpDownR.tx", 0)
            cmds.setAttr("CN_Bip001_BrowUpDownL.tx", 0)
            

        if rig1 == "Ruby":
           cmds.window( widthHeight=(308, 210),title="Ruby Custom Tools", sizeable=True ) 
        elif rig1== "Link":
            cmds.window( widthHeight=(308, 210),title="Link Custom Tools", sizeable=True )
        elif rig1 =="Zelda":
            cmds.window( widthHeight=(308, 210),title="Zelda Custom Tools", sizeable=True )
            
        form = cmds.formLayout()
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

        child1 = cmds.rowColumnLayout(numberOfColumns=3,columnWidth=[(1, 100), (2, 100), (3, 100)], rs = (10,10),cs = (10,10))
        cmds.button( label='AHH', c = AHH)
        cmds.button( label='OHH', c = OHH)
        cmds.button( label='EHH', c = EHH)
        cmds.button( label='UUU', c = UUU)
        cmds.button( label='IEE', c = IEE)
        cmds.button( label='FFF', c = FFF)
        cmds.button( label='LLL', c = LLL)
        cmds.button( label='TTH', c = TTH)
        cmds.button( label='MBP', c = MBP)

        cmds.button( label='RESET MOUTH',width=300, c=resetMouth)
        cmds.button( label='RESET MOuth',m=False)
        cmds.button( label='RESET MOuth',m=False)

        cmds.setParent( '..' )

        child2 = cmds.rowColumnLayout(numberOfColumns=1, rs = (10,10))
        cmds.attrFieldSliderGrp( min=-1, max=1, fmn=-1, fmx=1, pre=2, at="CN_Bip001_Eyes.blinkR", width=300)
        cmds.attrFieldSliderGrp( min=-1, max=1, fmn=-1, fmx=1, pre=2, at="CN_Bip001_Eyes.blinkL", width=300)
        cmds.attrFieldSliderGrp( min=-1, max=1, fmn=-1, fmx=1, pre=2, at="CN_Bip001_BrowUpDownR.tx", width=300, label="Right Brow Up Down")
        cmds.attrFieldSliderGrp( min=-1, max=1, fmn=-1, fmx=1, pre=2, at="CN_Bip001_BrowUpDownL.tx", width=300, label="Left Brow Up Down")
        cmds.button( label='RESET EYES',width=300, c=resetEyes)
        cmds.button( label='RESET EYE BROWS',width=300, c=resetBrows)



        cmds.setParent( '..' )

        cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Buttons'), (child2, 'Sliders')) )
    else:
        print("No Rig in Database with the name " +rig1)
    cmds.showWindow()
def display(A):
    name1= cmds.textField(name, q=True, text=True)
    print(name1)
   
cmds.button(label="generate tool", c=createTools)
cmds.button(label="generate tool",m=False)
cmds.text("------------------------------------------------------------------------------------------------------------------------------------")
cmds.text("RIG NAMES",fn="boldLabelFont")
cmds.text("Sam")
cmds.text("Nadia")
cmds.text("Penelopy")
cmds.text("Brooke")
cmds.text("Ruby")
cmds.text("Link")
cmds.text("Zelda")
cmds.text("------------------------------------------------------------------------------------------------------------------------------------")
cmds.button(label="generate tool",m=False) 
 




cmds.showWindow()
