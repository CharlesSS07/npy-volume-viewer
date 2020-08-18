# npy-volume-viewer
View your 3D numpy arrays in Blender3D. 4D on the way.


![](readme-images/vdb-viewer.001.png)
![](readme-images/vdb-viewer.png)

## Environment/Install
Blender3D: a 3D graphics software that can view vdb files
1. Install Blender3D 2.83 (might work with later or earlier versions but untested), either from a package manager, or https://blender.org.
- pyopenvdb: vdb writer library
1. If you can use docker, install pyopenvdb using that from https://github.com/theNewFlesh/docker_pyopenvdb.
2. If you can't, (no root or other container manager), conda works sometimes. `conda create --name vdbenv python=3.7`
3. `which pip` Should be the pip in your vdb conda environment.
4. `pip install pyopenvdb`
5. `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/folder/with/pyopenvdb.so/in/it`
6. For me, pyopenvdb couldn't find `libpython3.7m.so.1.0`, so I coppied it from my base environment to my vdb environment, and added the folder to `LD_LIBRARY_PATH`. This will probably not work for other people, however I did: `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/anaconda3/envs/vdbenv/lib/python3.7/site-packages/:$HOME/anaconda3/envs/vdbenv/lib/`. Note that you might find your conda environments in `~/.conda/envs/` instead of `~/anaconda3/envs/`.

## Running

Run `python ./npy-viewer xxxxx.npy yyyyy.npz nnnnn.npy` to view 3D arrays stored in correspoinding .npy/.npz files.

Here, instead of a shebang, the python specified on the commandline is used. This assumes you have activated your vdb environment
