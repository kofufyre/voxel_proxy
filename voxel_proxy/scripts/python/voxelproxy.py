'''
Docstring for scripts.python.post_proc
'''



import maya.cmds as cmd
import maya.api.OpenMaya as om


def mesh_process(mesh:str):

    if not cmd.objExists(mesh):
        return False
    

    try:
        blast = cmd.polySeparate(mesh, ch=1)
    except: return False #mesh cant be blasted on parts (shells)



    buffer = list() #buffer to store mesh shells polycount

    for mesh in blast:
        
        MSelection = om.MGlobal.getSelectionListByName(mesh)
        
        try:
            DagPath = om.MSelectionList(MSelection).getDagPath(0)
            MFnMesh = om.MFnMesh(DagPath)
            buffer.append(MFnMesh.numPolygons)
        except: continue


    shell = blast[buffer.index(max(buffer))] #pointer to shell we need to save

    blast.pop(buffer.index(max(buffer))) #remove highest polycount shell from blast buffer
    cmd.delete(blast) #remove all garbage shells


    #hierarchy cleaning
    shell_parent = cmd.listRelatives(shell, p=1)[0]
    cmd.parent(shell, w=1)

    if shell_parent:
        tmp = cmd.rename(shell_parent, f'{shell_parent}_qwerty')
        cmd.delete(tmp)

    
    output = cmd.rename(shell, mesh)
    
    return output





def mesh_polycount(mesh:str):

    if not cmd.objExists(mesh):
        return False
    

    MSelection = om.MGlobal.getSelectionListByName(mesh)

    try:
        DagPath = om.MSelectionList(MSelection).getDagPath(0)
        MFnMesh = om.MFnMesh(DagPath)
        return MFnMesh.numPolygons #return polycount
    
    except: return False #failed to construct mesh class and get polygons; return 0




