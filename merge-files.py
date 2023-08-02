import os

def get_files_starting_with_prefix(prefix):
    files = [file for file in os.listdir() if file.startswith(prefix)]
    return files

def write_to_filelist(files, output_filename):
    with open(output_filename, "w") as filelist:
        for file in files:
            filelist.write(f"file '{file}'\n")

def merge_files_for_camera(camera_prefix):
    camera_files = get_files_starting_with_prefix(camera_prefix)
    if camera_files:
        output_filename = f"{camera_prefix.lower()}_merged.mp4"
        write_to_filelist(camera_files, "filelist.txt")
        ffmpeg_cmd = f"ffmpeg -f concat -safe 0 -i filelist.txt -c copy {output_filename}"
        os.system(ffmpeg_cmd)
        print(f"Files for {camera_prefix} merged successfully into {output_filename}.")
    else:
        print(f"No files starting with '{camera_prefix}' found in the current directory.")

if __name__ == "__main__":
    cameras = ["D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11"]
    for camera in cameras:
        merge_files_for_camera(camera)
