<img width="1192" height="364" alt="voxel_proxy_header" src="https://github.com/user-attachments/assets/2a9912b3-419a-4aa2-af91-9baab7291a7b" /> <br>
*Currently in development.
# Description

**Voxel Proxy** provides a simple and fast way to generate volume proxy meshes. Originally intended as a rigging tool to generate a proxy mesh for skinning purpose to represent a complex geometry as one solid shape.


<img width="1292" height="179" alt="voxel_proxy_flowchart_test2" src="https://github.com/user-attachments/assets/c757d683-9ae6-4dc6-84b8-ac9be4567d78" />


# Requirements 
* MeshLab 2020.03 (or any with meshlabserver.exe)
* Python 3
* Bifrost 2.0.5 or higher
* Knowledge of Autodesk Maya

  
# Pre-Installation
As mentioned in Requirements, this tool needs [__MeshLab__](https://github.com/cnr-isti-vclab/meshlab) because its rely on MeshLab mesh filtering algorithms to refine the result of __Contour Dual Marching Cubes__ on volumetric data. <br>

You need a `special version with executable file named: "meshlabserver.exe"`, in newer versions its replaced by Python API. <br>

1. Download [MeshLab 2020.03](https://github.com/cnr-isti-vclab/meshlab/releases/tag/Meshlab-2020.03) from original releases.
2. Install or extract (if portable) anywhere you like.

#### Why MeshLab?
* Free and Open Source, has portable version.
* Fast and powerful mesh filters.
* Can be used via console.

# Installation
1. Download the repository.
2. Extract folder __`"voxel_proxy"`__ and __`"voxel_proxy.mod"`__ file to __`"Documents/maya/modules"`__ folder.
<br>

3. Open **Autodesk Maya**.
4. Create a new button on the shelf.
   - __Optional:__ You can set an icon for this button from **voxel_proxy** folder, theres an special folder called "icons".
6. Navigate to the command tab for your button and make sure Language set to **MEL**.
7. Write this as command: **`voxel_proxy();`**
8. Save changes.

At this point, if everything was done properly, by pressing the button will bring up the UI and first thing to do is specify the path to MeshLabServer.exe file.

# Quick Overview
https://github.com/user-attachments/assets/e7829120-70eb-4852-811e-5f1f217e8722


### Parameters: 
* `offset` <br>
  - World-space offset to voxels. Will work like extrude by normal.
    
* `density` <br>
  - A multiplier to apply to voxels detail.
    
* `detail` <br>
  - World-space size of the voxels. The lower values gives more detailed result.

> [!Tip]
> You can __suppress MeshLab execution__ in the UI to save your time and see which voxels settings suit you best. 

*  `Keep contour mesh` <br>
    -  Save the output mesh from bifrost in scene.

* `Single Shell` <br>
  -  Removes all mesh shells expect the biggest one (by polygons count).

> [!Note]
> Repository includes example meshes with optimal settings for a specific case.

# Effective Issue Ticket Guideline
To help me troubleshoot any issue that was suddenly discovered by you please provide the following:

* Detail issue description that includes your actions that yield to this.
* Maya and MeshLab version. 
* Error code, if any. Check in Windows -> Output Window for any `voxelProxy_<function> -> <error>`
* __Optional:__ Your CPU and RAM with system Reader/Writer device (SSD or HDD)

# Known Issues
* Because of using **MeshLab** via console command, **Maya** is completely **unaware** of the current **MeshLab state**. Did it finish? Maybe failed? <br>
  For more details and logic behind this you can read the file named: __`meshlab.mel`__




# Contact me
GMail: <rignocchio@gmail.com> <br>
Telegram: @kofufyre
