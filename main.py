import os
import pathlib
import datetime 

global SYSTEM_PATH, RUN_STAMP
SYSTEM_PATH = pathlib.Path().resolve()
RUN_STAMP = round(datetime.datetime.now().timestamp())

def extract_payload(path, payload_extractor_path="D:\Downloads\payload-dumper-go_1.2.2_windows_amd64.tar"):
    """
    path: accepts full .zip ROM file a archives or directly the payload.bin filepath
    payload_extractor_path: path to the tool
    """
    os.chdir(payload_extractor_path)
    os.system(f"payload-dumper-go {path}")

def get_build_prop(path, crext_path = r"D:\Downloads"):
    """
    path: accepts any system.img file
    crext_path (voluntary): launches crext from path
    """
    os.chdir(crext_path)
    os.mkdir(f"{SYSTEM_PATH._str}/{RUN_STAMP}")
    os.system(f"crext-win32 -f {path} -c cp /system/build.prop {SYSTEM_PATH._str}/{RUN_STAMP}/build.prop")

extract_payload(r"D:\Downloads\miui_JASMINEGlobal_V9.6.15.0.ODIMIFE_7d955203da_8.1.zip")
# get_build_prop(r"D:\Downloads\payload-dumper-go_1.2.2_windows_amd64.tar\extracted_20231216_110304\system.img")