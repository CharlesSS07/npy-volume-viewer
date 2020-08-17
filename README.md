# npy-volume-viewer
Open 3D npy array to be viewed in blender3D

# Environment/Install
Blender:
Install Blender3D 2.83, either from a package manager, or https://blender.org.

pyopenvdb:

If you can use docker, install pyopenvdb using that.

Otherwise,
I use conda, with pyopenvdb installed using pip:
`conda create --name vdbenv python=3.7`
`which pip`
Should be the pip in your conda environment.
`pip install pyopenvdb`
Installs files like pyopenvdb.so in your env's lib folder.
`export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/folder/with/pyopenvdb.so/in/it`
For me, pyopenvdb couldn't find libpython3.7m.so.1.0, so I coppied it from my base environment to my vdbenv environment, and added the folder to LD_LIBRARY_PATH.
This will probably not work for other people, however this is what I did:
`export LD_LIBRARY_PATH=$HOME/anaconda3/envs/vdbenv/lib/python3.7/site-packages/:$HOME/anaconda3/envs/vdbenv/lib/`
Note that you might find your conda environments in `~/.conda/envs/` instead of `~/anaconda3/envs/`.

# Running
Run "python ./npy-viewer xxxxx.npy yyyyy.npy nnnnn.npy" to view 3D arrays stored in correspoinding .npy files.
Here, instead of a shebang, the python specified on the commandline is used.
Also works for npz files.
