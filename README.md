**README**

This Python script automates the process of merging video files from multiple cameras, each identified by a unique prefix. It is designed to simplify the task of concatenating hikvision video recordings from various cameras into individual merged output files for each camera.

**How it works**

The script scans the current directory for video files with filenames starting with user-defined camera prefixes (e.g., "D1", "D2", etc.). It then utilizes FFmpeg, to merge the video files for each camera into separate output files with a naming convention of camera_prefix_merged.mp4 (e.g., d1_merged.mp4, d2_merged.mp4, etc.).

The script consists of the following main functions:

    get_files_starting_with_prefix(prefix): Retrieves a list of video files that start with the specified prefix in the current directory.

    write_to_filelist(files, output_filename): Writes the names of the video files to a temporary text file (filelist.txt) in a format compatible with FFmpeg.

    merge_files_for_camera(camera_prefix): Merges the video files for a given camera prefix using FFmpeg. The script generates a merged output file with a unique name for each camera.

**Prerequisites**

Before using the script, ensure that you have the following:

    Python installed on your system.
    FFmpeg installed and accessible from the command line.

**How to use**

    Place the script (merge_cameras.py) in the directory containing the video files.
    Open a terminal or command prompt, navigate to the script's location, and run the following command:
    python merge_cameras.py

The script will automatically merge video files for each camera prefix (e.g., "D01", "D02", etc.) and create separate merged output files for each camera.

Please note that the script assumes the input video files are located in the same directory as the script. Additionally, you can customize the list of camera prefixes in the script to match your specific naming convention.
