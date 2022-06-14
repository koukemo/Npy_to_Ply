# NPY to PLY

Convert npy file to ply file.

## Requirement

---

- Python3.x
    - open3d (pip)
        - python3-testresources

### Installing

Run the following command :

```shell
$ pip3 install open3d
```

<br>

> **Warning** <br>
> If the following error occurs : <br>
    ```
    [ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    launchpadlib 1.10.13 requires testresources, which is not installed.
    ```

Run the following command :

```shell
# Check 
$ pip3 check
launchpadlib 1.10.13 requires testresources, which is not installed. (→ ☓)

$ sudo apt install python3-testresources

# Check again
$ pip3 check
No broken requirements found. (→ OK)

$ pip3 install open3d
```

## Tests

---

**Default Configuration** <br>
input datas (npy) : [input/] <br>
output datas (ply) : [output/] <br>

Run the following command :

```shell
python3 main.py
```

## Results

---

Example of the results of looking at the output data using meshlab.

![meshlab_output](/results/meshlab_0_ply_sample.png)