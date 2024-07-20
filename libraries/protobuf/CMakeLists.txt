PROJECT(rpc)
CMAKE_MINIMUM_REQUIRED (VERSION 3.0.0)
SET(CMAKE_CXX_FLAGS "-g -Wall -std=c++11")

# Set the runtime library to /MDd for debug builds
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MDd")
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /MDd")

# Define an empty LIBS variable
set(PROTO_LIBS)

# Read the lib files from the text file and append to the LIBS variable
file(STRINGS "../../lib_files_list.txt" lib_files)
list(APPEND PROTO_LIBS ${lib_files})

find_package(Protobuf REQUIRED)

ADD_SUBDIRECTORY(proto)

message(PROTOBUF_LIBRARIES = ${Protobuf_LIBRARIES})
message(PROTO_LIBS = ${PROTO_LIBS})


INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR})
INCLUDE_DIRECTORIES(${Protobuf_INCLUDE_DIRS})
ADD_EXECUTABLE(main main.cpp)
TARGET_LINK_LIBRARIES(main proto ${Protobuf_LIBRARIES})
TARGET_LINK_LIBRARIES(main proto ${PROTO_LIBS})
