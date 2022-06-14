import open3d as o3d
import numpy as np
import glob
import os.path

def main():
    # input & output dir setting
    input_dir_path = "./input"
    output_dir_path = "./output"
    datas_mkdirs(input_dir_path)
    datas_mkdirs(output_dir_path)

    # read npy
    input_data_path = "./input/*"
    npy_files = glob.glob(input_data_path)

    # change npy to ply
    pcd = o3d.geometry.PointCloud()
    for index, npy_file in enumerate(npy_files):
        npy_to_np = np.load(npy_file)
        pcd.points = o3d.utility.Vector3dVector(npy_to_np)
        o3d.io.write_point_cloud(os.path.join(output_dir_path, str(index) + "_data.ply"), pcd)

def datas_mkdirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

if __name__ == "__main__":
    main()