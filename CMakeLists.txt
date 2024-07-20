# Copyright 2018 The Min-DevKit Authors. All rights reserved.
# Use of this source code is governed by the MIT License found in the License.md file.

cmake_minimum_required(VERSION 3.0)

project(my_simple_external)

set(C74_MIN_API_DIR "C:/Users/rizzo/OneDrive/Desktop/TESI/MMM4WINDOWS/source/min-api")
include(${C74_MIN_API_DIR}/script/min-pretarget.cmake)

# Set the runtime library to /MDd for debug builds
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MDd")
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /MDd")

#############################################################
# MAX EXTERNAL
#############################################################

###### PROTOBUF ########
#PROTOBUF
set(PROTO_LIBS)

# Read the lib files from the text file and append to the LIBS variable
file(STRINGS "lib_files_list.txt" lib_files)
list(APPEND PROTO_LIBS ${lib_files})

find_package(Protobuf REQUIRED)

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR})
INCLUDE_DIRECTORIES(${Protobuf_INCLUDE_DIRS})
find_package(Protobuf REQUIRED)
######################

include_directories( 
	"${C74_INCLUDES}"
)


set( SOURCE_FILES
	${PROJECT_NAME}.cpp
)


add_library( 
	${PROJECT_NAME} 
	MODULE
	${SOURCE_FILES}
	"libraries/protobuf/proto/message.proto"
)

set(proto_lib "${CMAKE_SOURCE_DIR}/libraries/protobuf/solution/proto/Debug/proto.lib")


include(${C74_MIN_API_DIR}/script/min-posttarget.cmake)

target_link_libraries(
	${PROJECT_NAME}
	PRIVATE
		${Protobuf_LIBRARIES}
        ${PROTO_LIBS}
        ${proto_lib}
)

#############################################################
# UNIT TEST
#############################################################

include(${C74_MIN_API_DIR}/test/min-object-unittest.cmake)
