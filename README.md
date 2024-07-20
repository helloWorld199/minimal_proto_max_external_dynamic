Simple max external with a protobuf dependency which gives Error 193 on M4L.

## Dependencies

1. **Install Protobuf**
   - Protobuf has been installed using vcpkg.
   - My Protobuf version is: `25.1.0`.

2. **Install min-api**
   - Use this specific version of the min-api: [min-api @ 4ba9c1b2adb53eab4d9896f0c5005208452d1577](https://github.com/Cycling74/min-api/tree/4ba9c1b2adb53eab4d9896f0c5005208452d1577).

3. **Modify CMakeLists.txt**
   - Modify the `CMakeLists.txt` file in the main folder accordingly to detect min_api, at line 8.

## Installation & Compilation Instructions

1. **Run getlibs.py**
   - Execute `getlibs.py` to generate a text file with all the libraries that need to be linked to the final external. It basically scans the whole vcpkg/lib folder. You should get something like lib_files_list.txt.

3. **Build proto**
   - Go to minimal_proto_max_external/libraries/protobuf
   - run the following command:
     ```sh
     cmake -G "Visual Studio 17 2022" -S . -B solution --preset debug
     ```
   - Open the solution and build proto
     
2. **Run CMake**
   - From the main folder, run the following command:
     ```sh
     cmake -G "Visual Studio 17 2022" -S . -B solution --preset debug
     ```

3. **Build the Visual Studio Solution**
   - Open the generated Visual Studio solution.
   - Build the solution using the `/MTd` flag for Runtime Library and static linking to avoid manually configuring Max to find the DLLs.
  
## Notes
If you are getting this error while building on Visual Studio:
     ```sh
     LNK1107: invalid or corrupt file: cannot read at 0x370
     ```
That's because for some reason vcpkg.cmake is linking libprotobuf.dll instead of libprotobuf.lib. To fix this just go to Properties > Linker > Input and change the C:\vcpkg\installed\x64-windows\debug\bin\libprotobufd.dll C:\vcpkg\installed\x64-windows\debug\lib\protobufd.lib
